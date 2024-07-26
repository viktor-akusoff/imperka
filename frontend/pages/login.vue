<template>
    <ClientOnly>
        <div class="login-form">
            <input type="text" class="form-control" placeholder="Логин" v-model="userData.username"/>
            <input type="password" class="form-control" placeholder="Пароль" v-model="userData.password"/>
            <p class="text-danger" v-if="loginError">Неверные логин или пароль!</p>
            <button class="btn btn-primary" @click="login()">Войти</button>
        </div>
    </ClientOnly>
</template>

<script setup lang="ts">

    import axios from 'axios'

    useHead({
      title: "ВХОД"
    })

    const userData = ref({
        username: '',
        password: ''
    })

    const loginError = ref(false)

    const config = useRuntimeConfig()

    const router = useRouter();

    const refreshToken = useState('refresh_token')
    const accessToken = useState('access_token')
    const authenticated = useState('authenticated')

    async function login() {
        loginError.value = false
        const url = config.public.apiUrl + '/auth/token'
        await axios
            .postForm(url, userData.value)
            .then((response) => {
                refreshToken.value = response.data['refresh_token']
                accessToken.value = response.data['access_token']
                localStorage.setItem('refresh_token', refreshToken.value)
                localStorage.setItem('access_token', accessToken.value)
                axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`
                authenticated.value = true
                router.push('/')
            })
            .catch((error) => {
                console.log(error)
                loginError.value = true
            })
    }

    onMounted(async () => {
      const url = config.public.apiUrl + '/auth/check'
      await axios
        .get(url)
        .then((response) => {
            router.push('/')
        })
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .login-form {
        @extend .rounded;
        @extend .p-5;
        @extend .d-flex;
        @extend .flex-column;
        @extend .gap-3;
        @include with_border;
        margin: auto;
        box-sizing: border-box;
        background: white;
        font-family: sans-serif;
    }

</style>