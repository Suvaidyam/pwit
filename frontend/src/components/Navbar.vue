<template>
    <div class="w-full fixed top-0 bg-white z-50 px-4 md:px-8 lg:px-20 h-16 flex justify-between items-center shadow-md">
        <router-link to="/" class="text-2xl font-bold text-primary">
            <img :src="`http://pwit.localhost:8000/files/logo.png`" class="w-32" alt="">
        </router-link>
        <div class="flex gap-3 text-sm">
           <Register/>
           <Login/>
        </div>
    </div>
</template>

<script setup>
import { ref,inject,onMounted } from 'vue'
import Login from './Login.vue'
import Register from './Register.vue'

const call = inject('$call')
const cur_session = ref(JSON.parse(localStorage.getItem('session')))

const create_session = async () => {
    if (!cur_session.value) {
        const response = await call('pwit.controllers.api.create_session', {})
        console.log(response)
        if (response) {
            localStorage.setItem('session', JSON.stringify(response))
        }
    }
}
onMounted(() => {
    create_session()
})
</script>