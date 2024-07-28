<template>
    <div>
        {{ isAuthenticated }}
    </div>
</template>

<script setup lang="ts">
    const { isAuthenticated } = useAxios();
    useHead({
        title: 'ГЛАВНАЯ'
    })
</script>