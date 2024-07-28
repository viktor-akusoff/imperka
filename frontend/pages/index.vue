<template>
    <div v-if="isLoading">Загрузка...</div>
    <div v-else-if="pageData">
        <div class="header-block">
            <PageHeader 
                :titleText="pageData.header.title" 
                :mediaType="pageData.header.media_type" 
                :mediaSource="getMedia(pageData.header.media_source)"
            >
                <p v-html="pageData.header.text"></p>
            </PageHeader>
        </div>
        <div class="blocks">
            <div v-for="(block, index) in pageData.blocks" :key="index">
                <template v-if="block.type === 'paragraph'">
                    <PageParagraph
                        :titleText="block.data.title" 
                        :titleAlignment="block.data.alignment"
                    >
                        <p v-html="block.data.text"></p>
                    </PageParagraph>
                </template>
                <template v-else-if="block.type === 'image'">
                    <PageImage :images="block.data"/>
                </template>
                <template v-else-if="block.type === 'html'">
                    <PageHTML :htmlData="block.data"/>
                </template>
            </div>
        </div>
        <router-link class="btn btn-sm btn-success mt-2" :to="`/edit?page=index`" v-if="isAuthenticated">Редактировать</router-link>
    </div>
    <div v-else>Ошибка 404: Страница не найдена</div> 
</template>
  
<script setup lang="ts">
import axios from 'axios'

const pageData = ref(null)
const isLoading = ref(true)
const config = useRuntimeConfig()

const { isAuthenticated } = useAxios()


const { getMedia } = useMedia()

onMounted(async () => {
    
    try {
        const response = await axios.get(`${config.public.apiUrl}/pages/index`);
        pageData.value = response.data;
        let seo = {
            title: pageData.value.header.title.toUpperCase(),
            ogTitle: pageData.value.header.title.toUpperCase(),
            description: pageData.value.header.text.replace(/(<([^>]+)>)/ig, ''),
            ogDescription: pageData.value.header.text.replace(/(<([^>]+)>)/ig, '')
        }
        if (pageData.value.header.media_type == 'video') {
            seo["ogVideo"] = pageData.value.header.media_source
        } else if (pageData.value.header.media_type == 'image') {
            seo["ogImage"] = pageData.value.header.media_source
        }
        useSeoMeta(seo)
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