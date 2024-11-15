<template>
    <div class="p-4 h-full w-full">
        <Breadcrumb />
        <h1 class="text-h2 font-serif font-semibold text-primary">{{ title }}</h1>
        <transition name="fade" mode="out-in">
            <div  class="w-full h-full">
               <FormView :doctype="title" :section="true" :key="title" :isRoute="`${current_path}/results`"/>
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, watch,inject } from 'vue'
import { useRoute } from 'vue-router';
import Breadcrumb from './Breadcrumb.vue'
import {FormView} from '../../../../../sva_form_vuejs/form_view';

const route = useRoute()
const current_path = ref(route.fullPath)
const title = ref(splitAtSecondCapital(route.name));

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    current_path.value = oldVal.path
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
