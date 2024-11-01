<template>
    <div class="w-52 h-screen fixed top-0 pt-16 left-0 z-20">
        <div class="w-full h-full bg-primary p-2">
            <p class="pl-2 py-2 font-bold text-[11px] text-white">RECOMMENDED PRINCIPLES</p>
            <router-link to="/funder/multi-year-artnerships" :class="route.fullPath == '/funder/multi-year-artnerships' ? 'bg-white' : 'text-white'"
                class="block text-sm py-2 px-3 rounded-md mb-2 hover:bg-white hover:text-black">Multi-year Partnerships</router-link>
            <router-link to="/funder/core-costs" :class="route.fullPath == '/funder/core-costs' ? 'bg-white' : 'text-white'"
                class="block text-sm py-2 px-3 rounded-md mb-2 hover:bg-white hover:text-black">Core Costs</router-link>
            <router-link to="/funder/organization-development" :class="route.fullPath == '/funder/organization-development' ? 'bg-white' : 'text-white'"
                class="block text-sm py-2 px-3 rounded-md mb-2 hover:bg-white hover:text-black">Organization Development</router-link>
            <p class="pl-2 py-2 font-bold border-t text-[11px] text-white">ADDITIONAL PWIT PRINCIPLES</p>
            <router-link to="/funder/rinancial-resilience" :class="route.fullPath == '/funder/rinancial-resilience' ? 'bg-white' : 'text-white'"
                class="block text-sm py-2 px-3 rounded-md mb-2 hover:bg-white hover:text-black">Financial Resilience</router-link>
            <router-link to="/funder/diversity-equity-inclusion" :class="route.fullPath == '/funder/diversity-equity-inclusion' ? 'bg-white' : 'text-white'"
                class="block text-sm py-2 px-3 rounded-md mb-2 hover:bg-white hover:text-black">Diversity Equity Inclusion</router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = ref(useRoute())

watch(route, (newVal, oldVal) => {
    route.value = newVal
})

</script>