<template>
    <div v-if="isLoading">Идёт загрузка</div>
    <div v-else-if="error">Ошибка 404!</div>
    <div v-else class="d-flex flex-row flex-wrap gap-3 justify-content-center">
        <router-link :to="`/${page.slug}`" v-for="(page, index) in pages" :key="index">
            <div class="card bg-dark text-white" >
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
                <div class="card-img-overlay d-flex flex-column">
                    <h4 class="card-title d-block mt-auto text-uppercase">{{ page.header.title }}</h4>
                </div>
            </div>
        </router-link>
    </div>
</template>

<script setup lang="ts">

    const { getMedia } = useMedia()

    const { apiClient } = useAxios()

    const props = defineProps({
        hashtags: {
            type: Array,
            default: []
        }
    })

    const pages = ref([])

    const isLoading = ref(true)
    const error = ref(false)

    onMounted(() => {

        const params = {};

        if (props.hashtags && props.hashtags.length > 0) { 
            props.hashtags.forEach((hashtag) => {
                params[`hashtags`] = hashtag; // Use the same key for each hashtag
            });
        }

        apiClient
            .get('/pages', {
                params: params
            })
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

<style scoped lang="scss">

    @import '/assets/scss/main.scss';

    .card {
        width: 360px;
        height: 240px;
    }
    .card-img-overlay {
        font-family: 'Header Font';
        background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.7) 35%, rgba(0,0,0,0.1) 60%, rgba(0,0,0,0.2) 100%);
    }
    .card-img-top {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
</style>