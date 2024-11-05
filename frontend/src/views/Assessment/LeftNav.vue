<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'"
        class="w-16 md:w-60 h-screen fixed top-0 pt-20 left-0 z-20">
        <div class="w-full h-full bg-primary p-2 ">
            <div class="" v-for="[name, items] in Object.entries(menu_list)" :key="name">
                <p class="pl-2 hidden md:block py-2 font-bold border-t text-[11px] text-white">{{ name }}
                </p>
                <router-link :to="`/funder/${el.ref_doctype?.toLowerCase()?.split(' ').join('-')}`" v-for="el in items"
                    :class="route.fullPath == '/funder/'+el.ref_doctype?.toLowerCase()?.split(' ').join('-') ? 'bg-white' : 'text-white'"
                    class="block text-sm px-2 h-10 md:flex gap-2 items-center rounded-md mb-2 hover:bg-white hover:text-black">
                    <img :src="el.icon" alt="" class="w-5 h-5">
                    <p class="hidden md:block">{{ el.label }}</p>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { IndianRupee, PiggyBank, Scale, ChartNoAxesCombined, Handshake } from 'lucide-vue-next'
const route = ref(useRoute())
const store = inject('store')
const call = inject('$call')
const menu_list = ref({})
watch(route, (newVal, oldVal) => {
    route.value = newVal
})

const leftMenu = async () => {
    let res = await call('pwit.controllers.api.left_menu_list', {})
    if (res.code == 200) {
        menu_list.value = res.data
    }
}
onMounted(() => {
    leftMenu()
})
</script>