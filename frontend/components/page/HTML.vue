<template>

    <p v-html="htmlData.html"></p>
    <p class="text-center fs-5 fst-italic mt-3" style="font-family: sans-serif;">{{ htmlData.description }}</p>

</template>

<script setup lang="ts">
    defineProps({
        htmlData: {
            type: Object,
            default: {
                html: '',
                description: ''
            }
        }
    })
</script>

<style scoped lang="scss">

</style>