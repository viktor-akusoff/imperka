<template>
    <div class="edit-html-block">
        <div class="container p-0">
            <div class="row">
                <div class="col">
                    <textarea class="w-100" v-model="htmlBlockData.html" @change="updateHTMLBlockData()"></textarea>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="edit-html-block__title">Подпись</span>
                        <input type="text" class="form-control" placeholder="Описание HTML-блока" aria-describedby="edit-html-block__title" v-model="htmlBlockData.description" @change="updateHTMLBlockData()"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

    const htmlBlockData: any = ref({
        html: '',
        description: ''
    })

    const model = defineModel<Object>()

    function updateHTMLBlockData() {
        model.value = htmlBlockData.value
    }

    onMounted(() => {
        htmlBlockData.value = model.value || {}
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .edit-html-block {
        @extend .rounded;
        @extend .p-3;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }

    .edit-html-block__title {
        @extend .form-control;
        @extend .mb-3;
    }
</style>