<template>
    <PageEditor v-if="isAuthenticated"/>
</template>

<script setup lang="ts">

    const { isAuthenticated } = useAxios();

    useHead({
        title: "НОВАЯ СТРАНИЦА"
    })

    const router = useRouter();

    onMounted(async () => {
        if (!isAuthenticated.value) {
            router.push('/')
        } 
    })
</script>