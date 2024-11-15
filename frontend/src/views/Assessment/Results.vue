<template>
    <div class="w-full h-screen p-4">
        <div class="flex gap-2">
            <Text  @click="store.sidebar=true" class="w-6 min-w-6 cursor-pointer block md:hidden"/>
            <p class="text-gray-800 text-sm">
                <router-link to="/">Home</router-link>
                / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> / <router-link
                    to="/recommended">Recommended Principles</router-link> /
                <router-link :to="`/funder/${route.params.category}`">{{ title }}</router-link>
                <span class="text-gray-400 truncate"> / Results and Recommendtions</span>
            </p>
        </div>
        <div class="flex justify-between items-center">
            <h1 class="text-h3 md:text-h2 text-primary">Results and Recommendtions</h1>
            <DownloadResults />
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router';
import DownloadResults from './DownloadResults.vue';
import { Text } from 'lucide-vue-next'

const route = useRoute()
const title = ref(splitAtSecondCapital(route.path));

watch(route, (newVal) => {
    title.value = splitAtSecondCapital(newVal.path)
})
function splitAtSecondCapital(input) {
    input = input.split('/')[2]
    return input
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ')
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .trim();
}
</script>