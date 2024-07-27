<template>
    <div v-if="isLoading">Загрузка...</div>
    <PageEditor v-else-if="pageData" :pageData="pageData"/>
    <div v-else>Ошибка 404: Страница не найдена</div>
</template>
  
<script setup lang="ts">
import axios from 'axios'

const pageData = ref(null)
const isLoading = ref(true)
const config = useRuntimeConfig()

const router = useRouter()
const authenticated = useState('authenticated')

onMounted(async () => {

const url = config.public.apiUrl + '/auth/check'
    await axios
    .get(url)
    .then((response) => {
        authenticated.value = true
    })
    .catch((error) => {
        authenticated.value = false
        router.push('/')
    })  

    const route = useRoute();
    const slug = route.query?.page || 'undefined';
    
    try {
        const response = await axios.get(`${config.public.apiUrl}/pages/${slug}`);
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