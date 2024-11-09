<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'"
        class="w-16 md:w-60 h-screen fixed top-0 pt-20 left-0 z-20">
        <div class="w-full h-full bg-primary p-2 ">
            <div class="w-full text-white opacity-40 block md:hidden text-center py-2 hover:bg-white hover:text-black rounded-md mb-1 cursor-pointer" @click="store.sidebar=false">X</div>
            <div class="" v-for="([name, items],index) in Object.entries(menu_list)" :key="name">
                <p :class="['pl-2 hidden md:block py-2 font-bold text-[11px] text-white', { 'border-t': index !== 0 }]">
                    {{ name }}
                </p>
                <router-link :to="`/funder/${el.ref_doctype?.toLowerCase()?.split(' ').join('-')}`" v-for="el in items"
                    :class="route.fullPath == '/funder/' + el.ref_doctype?.toLowerCase()?.split(' ').join('-') ? 'bg-white' : 'text-white'"
                    class="text-sm px-2 h-10 flex gap-2 items-center justify-center md:justify-normal rounded-md mb-2 hover:bg-white hover:text-black">
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
const route = ref(useRoute())
const store = inject('store')
const call = inject('$call')
const props = defineProps(['menu_list'])
const menu_list = ref(props.menu_list) 

watch(route, (newVal, oldVal) => {
    route.value = newVal
}) 
watch(() => props.menu_list, (newVal, oldVal) => {
    menu_list.value = newVal
}, { deep: true, immediate: true })

</script>