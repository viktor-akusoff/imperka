<template>
    <div v-if="isLoading">Загрузка...</div>
    <PageEditor v-else-if="pageData" :pageData="pageData"/>
    <div v-else>Ошибка 404: Страница не найдена</div>
</template>
  
<script setup lang="ts">
import axios from 'axios'

const pageData = ref(null)
const isLoading = ref(true)

const router = useRouter()

const { isAuthenticated, apiClient } = useAxios();

onMounted(async () => {

    if (!isAuthenticated.value) {
        router.push('/')
    }  

    const route = useRoute();
    const slug = route.query?.page || 'undefined';
    
    try {
        const response = await apiClient.get(`/pages/${slug}`);
        pageData.value = response.data;
        useHead({
            title: "РЕДАКТИРОВАНИЕ СТРАНИЦЫ"
        })
    } catch (error) {
        console.error("Error fetching page data:", error);
        pageData.value = null; 
        useHead({
            title: "ОШИБКА 404"
        })
    } finally {
        isLoading.value = false; 
    }
});
</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .blocks {
        @extend .d-flex;
        @extend .flex-column;
        @extend .gap-5;
    }
</style>