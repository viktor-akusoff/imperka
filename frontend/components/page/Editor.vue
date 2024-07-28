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
                :mediaSource="getMedia(header.data.mediaSource)"
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
                    <button class="blocks__remove-button" @click="removeBlock(index)" title="Удалить">
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
                <template v-else-if="block.type == BlockType.Suggestion">
                    <PageEditorSuggestion v-if="block.mode == BlockStatus.Edit" v-model="block.data"/>
                    <PageSuggestion v-else-if="block.mode == BlockStatus.Preview" :hashtags="block.data"/>
                </template>
            </div>
        </div>
        <PageEditorBlocks 
            @addParagraph="pushTextBlock()" 
            @addImage="pushImageBlock()"
            @addHTML="pushHTMLBlock()"
            @addSuggestion="pushSuggestionBlock()"
        />
        <div class="d-flex flex-row gap-2 w-100 flex-wrap">
            <div :key="hashtagsKey">
                <span class="me-3">Хэштеги:</span>
                <span class="badge bg-primary me-1" v-for="(h, index) in hashtags" :key="index">
                    {{ h }} <button class="btn-close" @click="deleteHashtag(index)">x</button>
                </span>
            </div>
            <div class="input-group input-group-sm w-25">
                <input type="text" class="form-control" placeholder="хэштег" v-model="hashtag">
                <button class="btn btn-secondary" :disabled="!hashtag" type="button" @click="addHashtag()">+</button>
            </div>
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text">slug</span>
            <input type="text" class="form-control" placeholder="Введите url страницы" v-model="slug">
        </div>
        <div class="d-flex flex-row gap-2 align-items-center">
            <div class="input-group mb-3 w-25">
                <span class="input-group-text">Порядок</span>
                <input type="number" class="form-control" v-model="order">
            </div>
            <div class="form-check">
                <input 
                    class="form-check-input" 
                    type="checkbox" 
                    id="flexCheckMenu"
                    v-model="isInMenu"/> 
                <label class="form-check-label" for="flexCheckMenu">
                    Отображать в меню
                </label>
            </div>
        </div>
        <div class="d-flex flex-row gap-2" v-if="!isSaving">
            <button class="btn btn-success flex-grow-1" @click="save()">Сохранить</button>
            <button class="btn btn-danger" v-if="!!pageData" @click="deletePage()"><FontAwesomeIcon icon="trash" title="Удалить страницу"/></button>
        </div>
        <div v-else>
            Идёт сохранение
        </div>
    </ClientOnly>
</template>

<script setup lang="ts">
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import { library } from '@fortawesome/fontawesome-svg-core'
    import { faTrash, faEye, faPencil, faArrowUp, faArrowDown } from '@fortawesome/free-solid-svg-icons'

    library.add(faTrash, faEye, faPencil, faArrowUp, faArrowDown)

    const { apiClient } = useAxios();

    const { getMedia } = useMedia()

    const props = defineProps({
        pageData: {
            type: Object,
            default: null
        }
    })

    enum BlockStatus {
        Preview = 'preview',
        Edit = 'edit'
    }

    enum BlockType {
        Header = 'header',
        Paragraph = 'paragraph',
        Image = 'image',
        HTML = 'html',
        Suggestion = 'suggestion'
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
            mediaType: "image",
            mediaSource: ""
        }
    }

    const router = useRouter()

    const haveChanges = ref(false)

    const defaultBlocks: IBlock[] = []
    const defaultHashtags: String[] = []

    const header = ref(defaultHeaderBlock)

    const blocks = ref(defaultBlocks)

    const hashtags = ref(defaultHashtags)

    const hashtag = ref('')

    const listKey = ref(false)
    const hashtagsKey = ref(false)

    const slug = ref('')

    const isInMenu = ref(true)

    const order = ref(0)

    const isSaving = ref(false)

    onMounted(() => {
        if (props.pageData) {
            header.value.data.title = props.pageData.header.title
            header.value.data.mediaType = props.pageData.header.media_type
            header.value.data.mediaSource = props.pageData.header.media_source
            header.value.data.text = props.pageData.header.text
            slug.value = props.pageData.slug
            isInMenu.value = props.pageData.is_in_menu
            order.value = props.pageData.order
            hashtags.value = props.pageData.hashtags
            console.log(props.pageData.blocks)
            blocks.value = props.pageData.blocks.map((block) => {
                return { type: block.type, data: block.data, mode: BlockStatus.Edit }
            })
        }
    })

    function deleteHashtag(index) {
        hashtags.value.splice(index, 1)
        hashtagsKey.value = !hashtagsKey.value
    }

    function addHashtag() {
        if (hashtag.value) {
            hashtags.value.push(hashtag.value)
            hashtagsKey.value = !hashtagsKey.value
            hashtag.value = ""
        }
    }

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

    function pushSuggestionBlock() {
        blocks.value.push({
            type: BlockType.Suggestion,
            mode: BlockStatus.Edit,
            data: []
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

    function dataURLtoBlob(dataurl) {
        const arr = dataurl.split(',');
        const mime = arr[0].match(/:(.*?);/)[1];
        const bstr = atob(arr[1]);
        let n = bstr.length;
        const u8arr = new Uint8Array(n);

        while (n--) {
            u8arr[n] = bstr.charCodeAt(n);
        }

        return new Blob([u8arr], { type: mime });
    }

    async function uploadMedia() {
        if (header.value.data.mediaSource.startsWith('data:')) {
            const headerFormData = new FormData();
            headerFormData.append('media', dataURLtoBlob(header.value.data.mediaSource));
            try {
                const response = await apiClient.post('/media/upload', headerFormData, {
                    headers: { 'Content-Type': 'multipart/form-data' }
                });
                header.value.data.mediaSource = response.data.media_id;
            } catch (error) {
                console.error('Header image upload failed:', error);
            }
        }

        for (let i = 0; i < blocks.value.length; i++) {
            if (blocks.value[i].type === BlockType.Image) {
                for (let j = 0; j < blocks.value[i].data.length; j++) {
                    if (blocks.value[i].data[j].url.startsWith('data:')) {
                        const formData = new FormData();
                        formData.append('media', dataURLtoBlob(blocks.value[i].data[j].url));
                        try {
                            const response = await apiClient.post('/media/upload', formData, {
                                headers: { 'Content-Type': 'multipart/form-data' }
                            });
                            blocks.value[i].data[j].url = response.data.media_id;
                        } catch (error) {
                            console.error('Image upload failed:', error);
                        }
                    }
                }
            }
        }
    }

    async function savePage () {
        try {
            const pageData = {
                header: {
                    title: header.value.data.title,
                    text: header.value.data.text,
                    media_type: header.value.data.mediaType,
                    media_source: header.value.data.mediaSource
                },
                blocks: blocks.value.map((block) => {
                    return { type: block.type, data: block.data };
                }),
                hashtags: hashtags.value,
                slug: slug.value,
                order: order.value,
                is_in_menu: isInMenu.value
            };
            
            if (props.pageData) {
                const response = await apiClient.put(`/pages/${props.pageData.slug}`, pageData)
                await router.push(`/${response.data.slug}`)
                router.go()
            } else {
                const response = await apiClient.post('/pages/', pageData)
                await router.push(`/${response.data.slug}`)
                router.go()
            }
        } catch (error) {
            console.error("Error saving page:", error);
        }
    }

    async function save() {
        isSaving.value = true
        await uploadMedia().then(() => {
            savePage()
        })
        isSaving.value = false
    }

    async function deletePage() {
        if(confirm('Вы действительно хотите удалить страницу?')) {
            await apiClient
                .delete(`/pages/${props.pageData.slug}`)
            router.push('/')
        }
    } 

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

    .btn-close {
        border: none;
        background: none;
        font-weight: bold;
        color: white;
    }

</style>