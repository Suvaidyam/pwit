<template>
    <div class="w-full pt-6">
        <div class="flex gap-2 px-4 md:px-8 lg:px-20">
            <svg @click="store.sidebar = true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                stroke-width="1.5" stroke="currentColor" class="size-6 cursor-pointer block md:hidden">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" />
            </svg>
            <p class="text-gray-800 text-sm">
                <router-link to="/">Home </router-link>
                <span class="text-gray-400">/ Funder Diagnostic</span>
            </p>
        </div>
        <h1 class="text-h2 px-4 md:px-8 lg:px-20 tracking-wide font-serif text-primary font-bold">
            Funder Diagnostic
        </h1>
        <p class="text-sm px-4 md:px-8 lg:px-20   font-serif text-sebase font-normal">
            Please select the degree to which your organization’s mindset and practices agree or disagree with the
            following statements:
        </p>
        <div class="w-full flex flex-col gap-4 px-4 md:px-8 lg:px-20 py-5 mt-4 bg-gray-50">
            <FormView 
                :doctype="'Funder Diagnostic'" 
                :isCard="true" 
                :isDraft="true" 
                :section="true"
                :save_as_draft="save_as_draft"
                isRoute="/recommended" 
            />
        </div>
    </div>
    <FooterNav />
</template>

<script setup>
import { ref ,inject} from 'vue';
import FooterNav from '../components/FooterNav.vue';
import { FormView } from '../../../../sva_form_vuejs/form_view.js';

const store = inject('store');
const auth = inject('$auth');
const save_as_draft = () => {
    if(auth.isLoggedIn){
        console.log('save as draft');
    }else{
        store.auth = 'Log In';
    } 
}
</script>
