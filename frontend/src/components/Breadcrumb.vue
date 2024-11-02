<template>
    <div class="flex gap-2">
        <svg @click="store.sidebar=true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="size-6 cursor-pointer block md:hidden">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12" />
        </svg>
        <p class="text-gray-800 text-sm">
            <router-link to="/">Home</router-link>
            / <router-link to="/recommended">Recommended Principles</router-link> <span class="text-gray-400">/ {{ title }}</span>
        </p>
    </div>
</template>

<script setup>
import { ref ,inject} from 'vue'

const store = inject('store')
const props = defineProps(['name']);
const title = ref(props.name)
</script>