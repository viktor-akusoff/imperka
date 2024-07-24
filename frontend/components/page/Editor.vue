<template>
    <ClientOnly>
        <div class="header-block">
            <div class="blocks__buttons">
                <template v-if="header.mode == BlockStatus.Edit">
                    <button class="blocks__preview-button" @click="header.mode = BlockStatus.Preview" title="Предпросмотр">
                        <FontAwesomeIcon icon="eye" />
                    </button>
                </template>
                <template v-else-if="header.mode == BlockStatus.Preview">
                    <button class="blocks__edit-button" @click="header.mode = BlockStatus.Edit" title="Редактировать">
                        <FontAwesomeIcon icon="pencil" />
                    </button>
                </template>
            </div>
            <PageEditorHeader  v-if="header.mode == BlockStatus.Edit" v-model="header.data"/>
            <PageHeader 
                v-else-if="header.mode == BlockStatus.Preview"
                :titleText="header.data.title" 
                :mediaType="header.data.mediaType" 
                :mediaSource="header.data.mediaSource"
            >
                <p v-html="header.data.text"></p>
            </PageHeader>
        </div>
        <div class="blocks" :key="listKey">
            <div v-for="(block, index) in blocks" :key="index">
                <div class="blocks__buttons">
                    <template v-if="block.mode == BlockStatus.Edit">
                        <button class="blocks__preview-button" @click="block.mode = BlockStatus.Preview" title="Предпросмотр">
                            <FontAwesomeIcon icon="eye" />
                        </button>
                    </template>
                    <template v-else-if="block.mode == BlockStatus.Preview">
                        <button class="blocks__edit-button" @click="block.mode = BlockStatus.Edit" title="Редактировать">
                            <FontAwesomeIcon icon="pencil" />
                        </button>
                    </template>
                    <button @click="moveBlockUp(index)" class="blocks__arrow-button" :disabled="index === 0" title="Вверх">
                        <FontAwesomeIcon icon="arrow-up" />
                    </button>
                    <button @click="moveBlockDown(index)" class="blocks__arrow-button" :disabled="index === blocks.length - 1" title="Вниз">
                        <FontAwesomeIcon icon="arrow-down" />
                    </button>
                    <button class="blocks__remove-button" @click="removeBlock(index)">
                        <FontAwesomeIcon icon="trash"/>
                    </button>
                </div>
                <template v-if="block.type == BlockType.Paragraph">
                    <PageEditorParagraph v-if="block.mode == BlockStatus.Edit" v-model="block.data"/>
                    <PageParagraph 
                        v-else-if="block.mode == BlockStatus.Preview"
                        :titleText="block.data.title" 
                        :titleAlignment="block.data.alignment">
                        <p v-html="block.data.text"></p>
                    </PageParagraph>
                </template>
                <template v-else-if="block.type == BlockType.Image">
                    <PageEditorImage v-if="block.mode == BlockStatus.Edit" v-model="block.data"/>
                    <PageImage v-else-if="block.mode == BlockStatus.Preview" :images="block.data"/>
                </template>
                <template v-else-if="block.type == BlockType.HTML">
                    <PageEditorHTML v-if="block.mode == BlockStatus.Edit" v-model="block.data"/>
                    <PageHTML v-else-if="block.mode == BlockStatus.Preview" :htmlData="block.data"/>
                </template>
            </div>
        </div>
        <PageEditorBlocks @addParagraph="pushTextBlock()" @addImage="pushImageBlock()" @addHTML="pushHTMLBlock()"/>
    </ClientOnly>
</template>

<script setup lang="ts">
    import imperka from 'assets/webm/imperka.webm'
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import { library } from '@fortawesome/fontawesome-svg-core'
    import { faTrash, faEye, faPencil, faArrowUp, faArrowDown } from '@fortawesome/free-solid-svg-icons'

    library.add(faTrash, faEye, faPencil, faArrowUp, faArrowDown)

    enum BlockStatus {
        Preview = 'preview',
        Edit = 'edit'
    }

    enum BlockType {
        Header = 'header',
        Paragraph = 'paragraph',
        Image = 'image',
        HTML = 'html'
    }

    interface IBlock {
        type: BlockType,
        mode: BlockStatus,
        data: Object
    }
    

    const defaultHeaderBlock: IBlock = {
        type: BlockType.Header,
        mode: BlockStatus.Edit,
        data: {
            title: "Новая страница",
            text: "Вступительный текст новой страницы",
            mediaType: "video",
            mediaSource: imperka
        }
    }

    const defaultBlocks: IBlock[] = []

    const header = ref(defaultHeaderBlock)

    const blocks = ref(defaultBlocks)

    const listKey = ref(false)

    function pushTextBlock() {
        blocks.value.push({
            type: BlockType.Paragraph,
            mode: BlockStatus.Edit,
            data: {
                title: "Новый блок",
                alignment: "text-start",
                text: "<p>Техт нового блока</p>"
            }
        })
    }

    function pushImageBlock() {
        blocks.value.push({
            type: BlockType.Image,
            mode: BlockStatus.Edit,
            data: []
        })
    }

    function pushHTMLBlock() {
        blocks.value.push({
            type: BlockType.HTML,
            mode: BlockStatus.Edit,
            data: {
                html: '',
                description: ''
            }
        })
    }

    function removeBlock(index: number) {
        if (confirm('Вы уверены, что хотите удалить этот блок?')) {
            blocks.value.splice(index, 1)
            listKey.value = !listKey.value
        }
    }

    function moveBlockUp (index: number) {
        if (index > 0) {
            const temp = blocks.value[index]
            blocks.value.splice(index, 1)
            blocks.value.splice(index - 1, 0, temp)
            listKey.value = !listKey.value
        }
    };

    function moveBlockDown (index: number) {
        if (index < blocks.value.length - 1) {
            const temp = blocks.value[index]
            blocks.value.splice(index, 1)
            blocks.value.splice(index + 1, 0, temp)
            listKey.value = !listKey.value
        }
    };

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .blocks {
        @extend .d-flex;
        @extend .flex-column;
        @extend .gap-5;
    }

    .blocks__buttons {
        @extend .m-1;
        @extend .w-100;
        @extend .d-flex;
        @extend .flex-row;
        @extend .gap-1;
        @extend .justify-content-start;
    }

    .blocks__preview-button {
        @extend .text-black;
        @extend .btn;
        @extend .btn-sm;
        @extend .btn-warning;
    }

    .blocks__remove-button {
        @extend .text-white;
        @extend .btn;
        @extend .btn-sm;
        @extend .btn-danger;
        margin-left: auto;
    }

    .blocks__edit-button {
        @extend .text-white;
        @extend .btn;
        @extend .btn-sm;
        @extend .btn-success;
    }

    .blocks__arrow-button {
        @extend .btn;
        @extend .btn-sm;
        @extend .btn-secondary;
    }

</style>