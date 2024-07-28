<template>
    <div class="edit-header-block">
        <div class="container p-0">
            <div class="row">
                <div class="input-group mb-3">
                    <span class="input-group-text" id="edit-header-block__title">Заголовок</span>
                    <input type="text" class="form-control" placeholder="Название блока" aria-describedby="edit-header-block__title" v-model="headerBlockData.title" @change="updateHeaderBlockData()"/>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="edit-header-block__media-type">Тип</span>
                        <select class="form-select" aria-describedby="edit-header-block__media-type" v-model="headerBlockData.mediaType" @change="updateHeaderBlockData()">
                            <option value="image" selected>Картинка</option>
                            <option value="video">Видео</option>
                        </select>
                    </div>
                </div>
                <div class="col">
                    <div class="input-group mb-3">
                        <input 
                            type="file"
                            @change="onHeaderBlockMediaUpload" 
                            class="form-control"
                            aria-describedby="edit-header-block__media"
                        />
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col mb-3">
                    <img
                        v-if="headerBlockData.mediaType === 'image' && headerBlockData.mediaSource"
                        :src="getMedia(headerBlockData.mediaSource)"
                        alt="Preview"
                        height="100"
                        class="inline-block"
                    />
                    <video
                        v-if="headerBlockData.mediaType === 'video' && headerBlockData.mediaSource"
                        :src="getMedia(headerBlockData.mediaSource)"
                        controls
                        width="300"
                        class="inline-block"
                    ></video>
                </div>
            </div>
        </div>
        <QuillEditor 
            theme="snow" 
            v-model:content="headerBlockData.text" 
            content-type="html" @update:content="updateHeaderBlockData()"
            :toolbar="[
                [{ header: [1, 2, 3, 4, 5, 6, false] }],
                ['bold', 'italic', 'underline', 'strike'],
                [{ list: 'ordered' }, { list: 'bullet' }],
                [{ script: 'sub' }, { script: 'super' }],
                [{ indent: '-1' }, { indent: '+1' }],
                [{ direction: 'rtl' }], 
                [{ size: ['small', false, 'large', 'huge'] }],
                [{ header: 1 }, { header: 2 }],
                ['link'],
                [{ color: [] }, { background: [] }],
                [{ font: [] }],
                [{ align: [] }],
                ['clean'], 
            ]"
        />
    </div>
</template>

<script setup lang="ts">
    import { QuillEditor } from '@vueup/vue-quill'
    import '@vueup/vue-quill/dist/vue-quill.snow.css'

    const { getMedia } = useMedia()

    const defaultHeaderBlockData: any = {}

    const headerBlockData = ref(defaultHeaderBlockData)

    const model = defineModel<Object>()

    function updateHeaderBlockData() {
        model.value = headerBlockData.value
    }

    const onHeaderBlockMediaUpload = (event: any) => {
        const file = event.target.files[0]
        const reader = new FileReader()
        reader.onload = (e: any) => {
            headerBlockData.value.mediaSource = e.target.result
        }
        reader.readAsDataURL(file)
        updateHeaderBlockData()
    }

    onMounted(() => {
        headerBlockData.value = model.value || defaultHeaderBlockData
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .edit-header-block {
        @extend .rounded;
        @extend .p-3;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }

    .edit-header-block__title {
        @extend .form-control;
        @extend .mb-3;
    }
</style>