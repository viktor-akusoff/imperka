<template>
    <div class="edit-image-block">
        <div class="edit-image-block__list">
            <div class="edit-image-block__element" v-for="(image, index) in imageList">
                <img :src="image.url" :key="index">
                <div class="input-group">
                    <span class="input-group-text" id="edit-image-block__description">Подпись</span>
                    <input type="text" class="form-control" placeholder="Описание картинки" aria-describedby="edit-image-block__description" v-model="image.description"/>
                </div>
                <div class="edit-image-block__buttons">
                    <button @click="moveImageLeft(index)" class="edit-image-block__arrow-button" :disabled="index === 0" title="Вверх">
                        <FontAwesomeIcon icon="arrow-left" />
                    </button>
                    <button @click="moveImageRight(index)" class="edit-image-block__arrow-button" :disabled="index === imageList.length - 1" title="Вниз">
                        <FontAwesomeIcon icon="arrow-right" />
                    </button>
                    <button class="edit-image-block__remove-button" @click="removeImage(index)">
                        <FontAwesomeIcon icon="trash"/>
                    </button>
                </div>
            </div>
        </div>
        <div class="edit-image-block__upload">
            <div class="col">
                <div class="input-group mb-3">
                    <input 
                        type="file"
                        @change="onImageMediaUpload" 
                        class="form-control"
                        aria-describedby="edit-header-block__media"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import { library } from '@fortawesome/fontawesome-svg-core'
    import { faTrash, faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons'

    library.add(faTrash, faArrowLeft, faArrowRight)

    type Image = {
        image: String,
        description: String,
    }

    const model = defineModel()
    const imageList: any = ref([])

    const onImageMediaUpload = (event: any) => {
        const file = event.target.files[0]
        const reader = new FileReader()
        reader.onload = (e: any) => {
            imageList.value.push(
                { 
                    url: e.target.result,
                    description: ""
                }
            )
        }
        reader.readAsDataURL(file)
    }

    function moveImageLeft (index: number) {
        if (index > 0) {
            const temp = imageList.value[index]
            imageList.value.splice(index, 1)
            imageList.value.splice(index - 1, 0, temp)
        }
    }

    function moveImageRight (index: number) {
        if (index < imageList.value.length - 1) {
            const temp = imageList.value[index]
            imageList.value.splice(index, 1)
            imageList.value.splice(index + 1, 0, temp)
        }
    }

    function removeImage(index: number) {
        if (confirm('Вы уверены, что хотите удалить эту картинку?')) {
            imageList.value.splice(index, 1)
        }
    }

    function updateImageBlockData() {
        model.value = imageList.value
    }

    onMounted(() => {
        imageList.value = model.value || []
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .edit-image-block {
        @extend .rounded;
        @extend .p-3;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }
    
    .edit-image-block__list {
        @extend .mb-3;
        @extend .d-flex;
        @extend .flex-row;
        @extend .flex-wrap;
        @extend .gap-3;
    }

    .edit-image-block__element {
        @extend .d-flex;
        @extend .flex-column;
        @extend .gap-1;
        max-width: 35%;

        img {
            @extend .rounded;
            @extend .overflow-hidden;
        }
    }

    .edit-image-block__buttons {
        @extend .m-1;
        @extend .w-100;
        @extend .d-flex;
        @extend .flex-row;
        @extend .gap-1;
        @extend .justify-content-start;
    }

    .edit-image-block__remove-button {
        @extend .text-white;
        @extend .btn;
        @extend .btn-sm;
        @extend .btn-danger;
        margin-left: auto;
    }

    .edit-image-block__arrow-button {
        @extend .btn;
        @extend .btn-sm;
        @extend .btn-secondary;
    }

</style>