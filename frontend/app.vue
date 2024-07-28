<template>
  <div class="background"></div>
  <div class="container pt-5 pb-5 d-flex flex-column gap-5">
    <TopBar/>
    <NuxtPage/>
    <div class="footer">
      <hr/>
      <p style="font-family: sans-serif;" class="text-center">
        © Copyright 2024 Кирилл Волошин, Все права защищены.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
  import axios from 'axios'
  const refresh_token = useState('refresh_token')
  const access_token = useState('access_token')
  onBeforeMount(() => {
    refresh_token.value = localStorage.getItem('refresh_token') || ''
    access_token.value = localStorage.getItem('access_token') || ''
    axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`
  }),
  useHead({
    titleTemplate: 'ИМПЕРКА | %s'
  })
</script>