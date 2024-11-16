<template>
    <div class="p-4 w-full">
        <Breadcrumb />
        <h1 class="text-h2 font-serif font-semibold text-primary">{{ title }}</h1>
        <transition name="fade" mode="out-in">
            <div  class="w-full h-full">
               <FormView 
                    :doctype="title" 
                    :isTable="true" 
                    :isDraft="true" 
                    :section="true"
                    :save_as_draft="save_as_draft"
                    :key="title" 
                    :isRoute="`${current_path}/results`"
                />
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
const store = inject('store');
const auth = inject('$auth');

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    current_path.value = oldVal.path
})

const save_as_draft = () => {
    if(auth.isLoggedIn){
        console.log('save as draft');
    }else{
        store.auth = 'Log In';
    } 
}

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
