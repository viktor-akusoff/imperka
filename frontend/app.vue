<template>
  <div class="background"></div>
  <div class="container pt-5 pb-5 d-flex flex-column gap-5">
    <NuxtPage/>
  </div>
</template>

<script setup lang="ts">
  useHead({
    titleTemplate: 'ИМПЕРКА | %s'
  })
</script>