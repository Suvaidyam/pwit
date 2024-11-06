<template>
    <div class="p-4 h-full w-full">
        <Breadcrumb />
        <h1 class="text-h2 font-serif font-semibold text-primary">{{ title }}</h1>
        <Loader v-if="store.loading" />
        <transition name="fade" mode="out-in">
            <div v-if="!store.loading" class="w-full h-full">
               <Questoin />
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, watch,inject } from 'vue'
import { useRoute } from 'vue-router';
import Questoin from './Questoin.vue';
import Breadcrumb from './Breadcrumb.vue'
import Loader from './Loader.vue'

const route = useRoute()
const title = ref(splitAtSecondCapital(route.name));
const store = inject('store')

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
})
function splitAtSecondCapital(input) {
    return input
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .trim();
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
</style>
