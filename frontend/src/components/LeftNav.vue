<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'"
        class="w-16 md:w-60 h-screen fixed top-0 pt-20 left-0 z-20">
        <div class="w-full h-full bg-primary p-2 ">
            <p title="close" @click="store.sidebar = false" class="bg-primary py-1 hover:bg-white hover:text-black rounded-md cursor-pointer mb-1 block md:hidden text-white w-full text-center">X</p>
            <p class="pl-2 py-2 font-bold text-[11px] hidden md:block text-white">RECOMMENDED PRINCIPLES</p>
            <router-link to="/funder/multi-year-artnerships"
                :class="route.fullPath == '/funder/multi-year-artnerships' ? 'bg-white' : 'text-white'"
                class="block text-sm px-2 h-10 md:flex gap-2 items-center rounded-md mb-2 hover:bg-white hover:text-black">
                <Handshake class="w-5"/>
                <p class="hidden md:block">Multi-year Partnerships</p>
            </router-link>
            <router-link to="/funder/core-costs"
                :class="route.fullPath == '/funder/core-costs' ? 'bg-white' : 'text-white'"
                class="block text-sm px-2 h-10 md:flex gap-2 items-center rounded-md mb-2 hover:bg-white hover:text-black">
                <IndianRupee class="w-5"/>
                <p class="hidden md:block">Core Costs</p>
            </router-link>
            <router-link to="/funder/organization-development"
                :class="route.fullPath == '/funder/organization-development' ? 'bg-white' : 'text-white'"
                class="block text-sm px-2 h-10 md:flex gap-2 items-center rounded-md mb-2 hover:bg-white hover:text-black ">
               <ChartNoAxesCombined class="w-5"/>

                <p class="hidden md:block">Organization Development</p>
            </router-link>
            <p class="pl-2 hidden md:block py-2 font-bold border-t text-[11px] text-white">ADDITIONAL PWIT PRINCIPLES
            </p>
            <router-link to="/funder/rinancial-resilience"
                :class="route.fullPath == '/funder/rinancial-resilience' ? 'bg-white' : 'text-white'"
                class="block text-sm px-2 h-10 md:flex gap-2 items-center rounded-md mb-2 hover:bg-white hover:text-black">
                <PiggyBank class="w-5"/>
                <p class="hidden md:block">Financial Resilience</p>
            </router-link>
            <router-link to="/funder/diversity-equity-inclusion"
                :class="route.fullPath == '/funder/diversity-equity-inclusion' ? 'bg-white' : 'text-white'"
                class="block text-sm px-2 h-10 md:flex gap-2 items-center rounded-md mb-2 hover:bg-white hover:text-black">
               <Scale class="w-5"/>
                <p class="hidden md:block">Diversity Equity Inclusion</p>
            </router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router'
import {IndianRupee,PiggyBank,Scale,ChartNoAxesCombined,Handshake} from 'lucide-vue-next'
const route = ref(useRoute())
const store = inject('store')

watch(route, (newVal, oldVal) => {
    route.value = newVal
})

</script>