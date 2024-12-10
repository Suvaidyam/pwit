<template>
    <div class="flex w-full h-full" v-if="Object.entries(menu_list).length > 0">
        <LeftNav :menu_list="menu_list"/>
        <div :class="route.name=='Results'?'md:pr-8':'md:pr-8 lg:pr-20'" class="md:pl-60 w-full h-full">
            <router-view />
        </div>
    </div>
    <div class="w-full h-full flex justify-center items-center text-4xl text-gray-600" v-else>
        <Loader />
    </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue';
import LeftNav from './LeftNav.vue';
import { useRoute } from 'vue-router';
import Loader from '../../components/Loader.vue';

const route = useRoute()
const call = inject('$call')
const menu_list = ref({})


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