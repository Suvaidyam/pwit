<template>
    <div class="flex gap-2">
        <Text  @click="store.sidebar=true" class="w-6 min-w-6 cursor-pointer block md:hidden"/>
        <p class="text-gray-800 text-sm">
            <router-link to="/">Home</router-link>
           / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> / <router-link to="/recommended">Recommended Principles</router-link> <span class="text-gray-400 truncate">/ {{ title=='Organization Development'?' Organisation Development':title }}</span>
        </p>
    </div>
</template>

<script setup>
import { ref ,inject, watch} from 'vue'
import { useRoute } from 'vue-router';
import {Text} from 'lucide-vue-next'

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