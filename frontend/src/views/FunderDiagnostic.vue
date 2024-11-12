<template>
    <div class="w-full h-full pt-6">
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
        <div class="w-full flex flex-col gap-4 px-4 md:px-8 lg:px-20 py-5 mt-4 bg-gray-100">
            <FormView :doctype="'Funder Diagnostic'" :section="true" isRoute="/recommended" />
            <!-- <div v-for="(item, index) in data" :key="item.name">
                <div class="flex gap-3">
                    <div class="w-6 h-6 flex items-center justify-center text-xs rounded-full bg-gray-800 text-white">
                        {{ index + 1 }}
                    </div>
                    <h1 class="text-h5 font-normal ">{{ item.name1 }}</h1>
                </div>
                <div class="flex flex-col md:flex-row gap-3 pl-9 pt-2">
                    <div v-for="el in item.option" :key="el.name"
                        class="flex gap-2 bg-white items-center px-4 py-1.5 border rounded-md"
                        :class="{ 'border-[#3086c4]': el.checked }">
                        <input type="checkbox" :id="el.name" v-model="el.checked" class="cursor-pointer" />
                        <label :for="el.name" class="text-sm w-full truncate cursor-pointer">{{ el.name1 }}</label>
                    </div>
                </div>
            </div> -->
        </div>
        <!-- <div class="px-4 md:px-8 lg:px-20 py-4 flex gap-4 items-center">
            <button @click="submit"
                class="bg-secondary text-white px-6 py-2.5 text-sm border rounded-md">Submit</button>
            <button class="px-6 py-2.5 text-sm border rounded-md">Save as Draft</button>
        </div> -->
        <FooterNav />
    </div>
</template>

<script setup>
import FooterNav from '../components/FooterNav.vue'; 
import {FormView} from '../../../../sva_form_vuejs/form_view.js';

// const submit = () => {
//     // console.log(data.value)
//     router.push('/recommended')
// }
</script>
