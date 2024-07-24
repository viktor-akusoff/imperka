<template>
    <swiper-container 
        slides-per-view="1" 
        speed="500" loop="true"  
        navigation="true"
        pagination="true"
        @swiperslidechange="onSlideChange"
        :injectStyles="[
            `
                .swiper-button-next, .swiper-button-prev {
                    color: #ffbb00;
                    width: 55px;
                    height: 55px;
                }
                    
                path {
                    stroke: black;
                    stroke-width: 0.25px;
                    stroke-linejoin: round;
                }
                .swiper-pagination-bullet{
                    background-color: #ffbb00;
                    border: 1px solid black;
                }
            `
        ]"
        :zoom="{
            containerClass: 'swiper__image',
            minRatio: 1,
            maxRatio: 3
        }"
    >
        <swiper-slide v-for="(image, index) in images" :key="index">
            <div class="swiper__image">
                <img :src="image.url">
            </div>
        </swiper-slide>
    </swiper-container>
    <p class="text-center fs-5 fst-italic mt-3" style="font-family: sans-serif;">{{ description }}</p>
</template>

<script setup lang="ts">

    const props: any = defineProps({
        images: {
            type: Array,
            default: []
        }
    })

    const description = ref('')

    function onSlideChange(e: any) {
        description.value = props.images[e.detail[0].realIndex].description
    }

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .swiper__image {
        @extend .w-100;
        @extend .d-flex;
        @extend .flex-row;
        @extend .justify-content-around;
        @extend .align-items-center;
        height: 60vh;
        object-fit: contain;
        img {
            @extend .rounded;
            max-height: 100%;
            max-width: 100%;
        }
    }
</style>