<template>
    <div class="paragraph-block">
        <h1 :class="['paragraph-block__title', titleAlignment]">{{ titleText }}</h1>
        <div class="paragraph-block__container ql-editor" ref="slotContent" v-show="slotLength">
            <slot></slot>
        </div>
    </div>
</template>

<script setup lang="ts">
    defineProps({
        titleText: {
            type: String,
            default: 'Стандартный заголовок'
        },
        titleAlignment: {
            type: String,
            default: 'text-start',
            validator: (value: string) => ['text-start', 'text-center', 'text-end'].includes(value)
        }
    })

    const defaultContent: any = null

    const slotContent = ref(defaultContent)

    const slotLength = computed(() => {
        return slotContent.value ? slotContent.value.innerHTML.replace(/(<([^>]+)>)/ig, '').length : 0
    })
</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';

    .paragraph-block__container {
        @extend .rounded;
        @extend .p-5;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }

    .paragraph-block__title {
        @extend .title-text;
        @extend .pb-3;

        font-size: 1.5rem;

        @media (min-width: 576px) {
            font-size: 1.8rem;
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
            font-size: 3.2rem;
        }
    }
</style>