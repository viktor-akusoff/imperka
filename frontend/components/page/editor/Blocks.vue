<template>
    <div class="blocks-panel">
        <button @click="$emit('addParagraph')" class="blocks-panel__button" title="Добавить параграф">
            <font-awesome-icon icon="paragraph" />+
        </button>
        <button @click="$emit('addImage')" class="blocks-panel__button"  title="Добавить картинки">
            <FontAwesomeIcon icon="image" />+
        </button>
        <button @click="$emit('addHTML')" class="blocks-panel__button"  title="Добавить HTML">
            <FontAwesomeIcon icon="code" />+
        </button>
        <button @click="$emit('addSuggestion')" class="blocks-panel__button"  title="Добавить рекомендации">
            <FontAwesomeIcon icon="newspaper" />+
        </button>
    </div>
</template>

<script setup lang="ts">
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { library } from '@fortawesome/fontawesome-svg-core';
    import { faParagraph, faImage, faCode, faNewspaper } from '@fortawesome/free-solid-svg-icons';
    library.add(faImage, faParagraph, faCode, faNewspaper);

    defineEmits(['addParagraph', 'addImage', 'addHTML', 'addSuggestion'])

</script>

<style scoped lang="scss">
    @import '/assets/scss/main.scss';
    
    .blocks-panel {
        @extend .rounded;
        @extend .p-3;
        @extend .d-flex;
        @extend .flex-row;
        @extend .justify-content-around;
        @include with_border;
        background: white;
        font-family: sans-serif;
    }
    .blocks-panel__button {
        font-size: large;
        background: none;
        border: none;
        cursor: pointer;
    }
</style>