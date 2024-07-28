<template>
    <div v-if="isLoading">Идёт загрузка</div>
    <div v-else-if="error">Ошибка 404!</div>
    <div v-else class="d-flex flex-row flex-wrap gap-3">
        <div class="card" style="width: 18rem;" v-for="(page, index) in pages" :key="index">
            <img
                v-if="page.header.media_type === 'image' && page.header.media_source"
                :src="getMedia(page.header.media_source)"
                alt="Preview"
                class="card-img-top"
            />
            <video
                v-if="page.header.media_type === 'video' && page.header.media_source"
                :src="getMedia(page.header.media_source)"
                class="card-img-top"
                muted loop autoplay
            ></video>
            <div class="card-body">
                <h5 class="card-title">{{page.header.title}}</h5>
                <p class="card-text">{{ previewText(page.header.text.replace(/(<([^>]+)>)/ig, '')) }}</p>
                <router-link :to="`/${page.slug}`" class="btn btn-primary ье">Открыть</router-link>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    const { isAuthenticated, apiClient } = useAxios()

    const { getMedia } = useMedia()

    const pages = ref([])

    const isLoading = ref(true)
    const error = ref(false)

    onMounted(() => {
        apiClient
            .get('/pages')
            .then((response) => {
                pages.value = response.data
                isLoading.value = true
            })
            .catch(() => {
                error.value = true
            })
            .finally(() => {
                isLoading.value = false
            })
    })

</script>

<style lang="scss">

</style>