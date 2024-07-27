<template>
    <PageEditor/>
</template>

<script setup lang="ts">

    import axios from 'axios'

    const config = useRuntimeConfig()

    useHead({
        title: "НОВАЯ СТРАНИЦА"
    })

    const router = useRouter();

    const authenticated = useState('authenticated')

    onMounted(async () => {
      const url = config.public.apiUrl + '/auth/check'
      await axios
        .get(url)
        .then((response) => {
            authenticated.value = true
        })
        .catch((error) => {
            authenticated.value = false
            router.push('/')
        })   
    })
</script>