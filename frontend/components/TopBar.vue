<template>
    <div class="w-100 d-flex flex-row gap-1 justify-content-start" v-if="authenticated">
        <button class="btn btn-sm btn-primary" @click="router.push('/pages')">Страницы</button>
        <button class="btn btn-sm btn-success" @click="router.push('/new')">Новая страница</button>
        <button class="btn btn-sm btn-danger ms-auto" @click="logout()">Выйти</button>
    </div>
</template>

<script setup lang="ts">

    import axios from 'axios'

    const config = useRuntimeConfig()

    const router = useRouter();

    const access_token = useState('access_token')
    const refresh_token = useState('refresh_token')

    function logout() {
        access_token.value = ""
        refresh_token.value = ""
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        router.go()
    }


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
        })   
    })
</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';
</style>