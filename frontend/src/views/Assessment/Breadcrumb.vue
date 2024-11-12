<template>
    <div class="flex gap-2">
        <svg @click="store.sidebar=true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="size-6 cursor-pointer block md:hidden">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" />
        </svg>
        <p class="text-gray-800 text-sm">
            <router-link to="/">Home</router-link>
           / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> / <router-link to="/recommended">Recommended Principles</router-link> <span class="text-gray-400 truncate">/ {{ title }}</span>
        </p>
    </div>
</template>

<script setup>
import { ref ,inject, watch} from 'vue'
import { useRoute } from 'vue-router';

const route = useRoute() 
const store = inject('store')
const title = ref(splitAtSecondCapital(route.name));

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
})

function splitAtSecondCapital(input) {
  return input
    .replace(/([a-z])([A-Z])/g, '$1 $2')
    .trim(); 
}

</script>