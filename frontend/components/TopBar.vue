<template>
    <div class="w-100 d-flex flex-row gap-1 justify-content-start" v-if="isAuthenticated">
        <button class="btn btn-sm btn-primary" @click="router.push('/pages')">Страницы</button>
        <button class="btn btn-sm btn-success" @click="router.push('/new')">Новая страница</button>
        <button class="btn btn-sm btn-danger ms-auto" @click="logout()">Выйти</button>
    </div>
</template>

<script setup lang="ts">
    const { isAuthenticated, clearTokens } = useAxios();
    const router = useRouter()

    function logout() {
        clearTokens()
        router.go()
    }
</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';
</style>