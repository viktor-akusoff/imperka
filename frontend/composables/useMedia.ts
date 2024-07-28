export default function () {

    const config = useRuntimeConfig()

    function getMedia(address: String) {
        if (address.startsWith('data:')) {
            return address
        } else {
            return `${config.public.apiUrl}/media/${address}`
        }
    }

    return {
        getMedia
    }
}