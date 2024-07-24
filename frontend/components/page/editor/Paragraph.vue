<template>
    <div class="edit-paragraph-block">
        <div class="container p-0">
            <div class="row">
                <div class="col">
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="edit-paragraph-block__title">Заголовок</span>
                        <input type="text" class="form-control" placeholder="Название блока" aria-describedby="edit-paragraph-block__title" v-model="textBlockData.title" @change="updateTextBlockData()"/>
                    </div>
                </div>
                <div class="col">
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="edit-paragraph-block__position">Ориентация</span>
                        <select class="form-select" aria-describedby="edit-paragraph-block__position" v-model="textBlockData.alignment" @change="updateTextBlockData()">
                            <option value="text-start" >По левой стороне</option>
                            <option value="text-center">По центру</option>
                            <option value="text-end">По правой стороне</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <QuillEditor 
            theme="snow" 
            v-model:content="textBlockData.text" 
            content-type="html" @update:content="updateTextBlockData()"
            :toolbar="[
                [{ header: [1, 2, 3, 4, 5, 6, false] }],
                ['bold', 'italic', 'underline', 'strike'],
                [{ list: 'ordered' }, { list: 'bullet' }],
                [{ script: 'sub' }, { script: 'super' }],
                [{ indent: '-1' }, { indent: '+1' }],
                [{ direction: 'rtl' }], 
                [{ size: ['small', false, 'large', 'huge'] }],
                [{ header: 1 }, { header: 2 }],
                ['link', 'image', 'video'],
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

    const textBlockData = ref({})

    const model = defineModel<Object>()

    function updateTextBlockData() {
        model.value = textBlockData.value
    }

    onMounted(() => {
        textBlockData.value = model.value || {}
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .edit-paragraph-block {
        @extend .rounded;
        @extend .p-3;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }

    .edit-paragraph-block__title {
        @extend .form-control;
        @extend .mb-3;
    }
</style>