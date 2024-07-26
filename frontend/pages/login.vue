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

    async function login() {
        loginError.value = false
        const url = config.public.apiUrl + '/auth/token'
        await axios
            .postForm(url, userData.value)
            .then((response) => {
                console.log(response.data)
            })
            .catch((error) => {
                console.log(error)
                loginError.value = true
            })
    }

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