<template>
    <ClientOnly>
        <div class="login-form">
            <input type="text" class="form-control" placeholder="Логин" v-model="userData.login"/>
            <input type="password" class="form-control" placeholder="Пароль" v-model="userData.password"/>
            <button class="btn btn-primary">Войти</button>
        </div>
    </ClientOnly>
</template>

<script setup lang="ts">
    useHead({
      title: "ВХОД"
    })

    const userData = ref({
        login: '',
        password: ''
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