<template>
    <ClientOnly>
        <div class="login-form" v-if="!isAuthenticated">
            <input type="text" class="form-control" placeholder="Логин" v-model="userData.username"/>
            <input type="password" class="form-control" placeholder="Пароль" v-model="userData.password"/>
            <p class="text-danger" v-if="loginError">Неверные логин или пароль!</p>
            <button class="btn btn-primary" @click="login()">Войти</button>
        </div>
    </ClientOnly>
</template>

<script setup lang="ts">

    const { isAuthenticated, apiClient, setTokens} = useAxios();

    useHead({
      title: "ВХОД"
    })

    const userData = ref({
        username: '',
        password: ''
    })

    const loginError = ref(false)

    const router = useRouter();

    async function login() {
        loginError.value = false
        await apiClient
            .postForm('/auth/token', userData.value)
            .then((response) => {
                setTokens(response.data['access_token'], response.data['refresh_token'])
                router.push('/')
                router.go(0);
            })
            .catch((error) => {
                console.log(error)
                loginError.value = true
            })
    }

    onMounted(async () => {
        if (isAuthenticated.value) {
            router.push('/')
        }
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