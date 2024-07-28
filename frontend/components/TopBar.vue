<template>
<ClientOnly>
<nav class="navbar navbar-expand-lg navbar-light bg-white">
  <div class="container-fluid">
    <router-link class="navbar-brand" to="/">
        <img :src="imperka" style="max-width: 64px;"/>
    </router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <router-link class="nav-link imperka-link" aria-current="page" to="/">Главная</router-link>
        </li>
        <li class="nav-item" v-for="(page, index) in pages" :key="index">
          <router-link class="nav-link imperka-link" :to="`/${page.slug}`">{{page.header.title}}</router-link>
        </li>
      </ul>
      <form class="d-flex">
        <div v-if="isAuthenticated" class="d-flex gap-2">
            <router-link to="/new" class="btn btn-outline-success btn-sm" title="Новая страница"><FontAwesomeIcon icon="file-text" /> + </router-link>
            <button class="btn btn-outline-danger btn-sm" @click="logout()" title="Выйти"><FontAwesomeIcon icon="sign-out" /></button>
        </div>
        <router-link to="/login" class="btn btn-outline-warning btn-sm" v-else title="Войти"><FontAwesomeIcon icon="sign-in" /></router-link>
      </form>
    </div>
  </div>
</nav>
</ClientOnly>
</template>

<script setup lang="ts">
    
    import imperka from 'assets/png/imperka.png'

    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import { library } from '@fortawesome/fontawesome-svg-core'
    import { faFileText, faSignIn, faSignOut } from '@fortawesome/free-solid-svg-icons'

    library.add(faFileText, faSignIn, faSignOut)

    const { isAuthenticated, clearTokens, apiClient } = useAxios();
    const router = useRouter()

    const pages = ref([])

    function logout() {
        clearTokens()
        router.go()
    }

    onMounted(async () => {
      await apiClient
        .get('/pages/menu')
        .then((response) => {
          pages.value = response.data
        })
    })

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .imperka-link {
        @extend .text-uppercase;
        font-family: 'Title Font';
    }
</style>