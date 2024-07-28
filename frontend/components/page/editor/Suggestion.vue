<template>
    <div class="edit-suggestion-block">
        <div class="d-flex flex-row gap-2 w-100 flex-wrap">
            <div :key="hashtagsKey">
                <span class="me-3">Хэштеги:</span>
                <span class="badge bg-primary me-1" v-for="(h, index) in suggestionBlockData" :key="index">
                    {{ h }} <button class="btn-close" @click="deleteHashtag(index)">x</button>
                </span>
            </div>
            <div class="input-group input-group-sm w-25">
                <input type="text" class="form-control" placeholder="хэштег" v-model="hashtag">
                <button class="btn btn-secondary" :disabled="!hashtag" type="button" @click="addHashtag()">+</button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

    const model = defineModel()

    const suggestionBlockData = ref({})

    const hashtag = ref('')

    const hashtagsKey = ref(false)

    function deleteHashtag(index) {
        suggestionBlockData.value.splice(index, 1)
        hashtagsKey.value = !hashtagsKey.value
        updateSuggestionBlockData() 
    }

    function addHashtag() {
        if (hashtag.value) {
            suggestionBlockData.value.push(hashtag.value)
            hashtagsKey.value = !hashtagsKey.value
            hashtag.value = ""
        }
        updateSuggestionBlockData() 
    }

    function updateSuggestionBlockData() {
        model.value = suggestionBlockData.value
    }

    onMounted(() => {
        suggestionBlockData.value = model.value || {}
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .edit-suggestion-block {
        @extend .rounded;
        @extend .p-3;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }

    .btn-close {
        border: none;
        background: none;
        font-weight: bold;
        color: white;
    }

</style>