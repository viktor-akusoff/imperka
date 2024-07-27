<template>
    <div class="header-block">
        <div class="header-block__media-container">
            <div class="header-block__overlay"></div>
            <video muted loop autoplay class="header-block__media-element" v-if="mediaType == 'video'">
                <source :src="mediaSource">
            </video>
            <img class="header-block__media-element" v-if="mediaType =='image'" :src="mediaSource">
            <h1 class="header-block__title">{{ titleText }}</h1>
        </div>
        <div class="header-block__text-container">
            <hr class="header-block__separator">
            <div class="ql-editor">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    defineProps({
        mediaType: {
            type: String,
            default: 'video',
            validator: (value: string) => ['video', 'image'].includes(value)
        },
        mediaSource: {
            type: String,
            required: true
        },
        titleText: {
            type: String,
            default: 'Стандартный заголовок'
        }
    })
</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .header-block {
        @extend .rounded;
        @include with_border;
        @extend .mb-5;
        background: white;
    }

    .header-block__title {
        @extend .header-text;
        @extend .p-3;
        @extend .w-100;
        @extend .text-center;
        @include text_cast_shadow(0, 1);
        position: absolute;
        z-index: 100;
        bottom: 0;
        left: 0;
        text-transform: uppercase;
        font-size: 1.8rem;

        @media (min-width: 576px) {
            font-size: 2rem;
        }

        @media (min-width: 768px) {
            font-size: 2.25rem;
        }

        @media (min-width: 960px) {
            font-size: 2.5rem;
        }

        @media (min-width: 1140px) {
            font-size: 3rem;
        }

        @media (min-width: 1320px) {
            font-size: 4.2rem;
        }

    }

    .header-block__media-container {
        @extend .rounded-top;
        position: relative;
        overflow: hidden;
        z-index: 100;
        padding: 0;
    }

    .header-block__media-element {
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        padding: 0;
    }
    
    .header-block__overlay {
        @include linear_gradient;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0; 
    }

    .header-block__separator {
        @extend .d-block;
        @extend .pb-4;
    }

    .header-block__text-container {
        @extend .rounded-bottom;
        @extend .p-5;
        @extend .pt-0;
        font-family: sans-serif;
        line-height: 1.5rem;
    }
</style>