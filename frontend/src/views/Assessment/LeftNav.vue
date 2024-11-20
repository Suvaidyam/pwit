<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'"
        class="w-16 md:w-60 h-screen fixed top-0 left-0 z-20">
            <div class="flex justify-end  bg-white fixed px-4 md:px-10 lg:px-20 h-20 items-center">
                <router-link to="/" class="text-2xl font-bold text-primary">
                    <img :src="`/files/logo.png`" class="w-40 h-14" alt="">
                </router-link>
            </div>
        <div class="w-full h-full bg-primary p-2 pt-24 ">
            <div class="w-full text-white opacity-40 block md:hidden text-center py-2 hover:bg-white hover:text-black rounded-md mb-1 cursor-pointer" @click="store.sidebar=false">X</div>
            <div class="" v-for="(items,index) in menu_list" :key="items.name">
                <!-- <p :class="['pl-2 hidden md:block py-2 font-bold text-[11px] text-white', { 'border-t': index !== 0 }]">
                    {{ items.name }}
                </p> -->
                <router-link :to="`/funder/${items.ref_doctype?.toLowerCase()?.split(' ').join('-')}`" 
                    :class="['/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-'),'/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-')+'/results'].includes(route.fullPath) ? 'bg-white' : 'text-white'"
                    class="text-sm px-2 h-10 flex gap-2 items-center justify-center md:justify-normal rounded-md mb-2 hover:bg-white hover:text-black">
                    <img :src="items.icon" alt="" class="w-5 h-5">
                    <p class="hidden md:block">{{ items.label }}</p>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue'
import { useRoute } from 'vue-router'
const route = ref(useRoute())
const store = inject('store')
const call = inject('$call')
const menu_list = ref({})

watch(route, (newVal, oldVal) => {
    route.value = newVal
})
console.log(menu_list)
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