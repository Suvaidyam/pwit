<template>
    <div class="w-full fixed top-0 bg-white z-20 px-4 md:px-8 lg:px-20 h-16 flex justify-between items-center shadow-md">
        <router-link to="/" class="text-2xl font-bold text-primary">
            <img :src="`http://pwit.localhost:8000/files/logo.png`" class="w-32" alt="">
        </router-link>
        <div class="flex gap-3 text-sm" v-if="!auth.isLoggedIn">
           <Register/>
           <Login/>
        </div>
        <div class="flex gap-2 items-center" v-else>{{ auth?.cookie?.full_name }}
            <ProfileDrop/>
        </div>
    </div>
</template>

<script setup>
import { ref,inject,onMounted,watch } from 'vue'
import Login from './Login.vue'
import Register from './Register.vue'
import ProfileDrop from './ProfileDrop.vue';
const call = inject('$call')
const auth = inject('$auth');
const cur_session = ref(JSON.parse(localStorage.getItem('session')))

watch(() => auth.cookie, (value) => {
    auth.cookie = value
});
const create_session = async () => {
    if (!cur_session.value) {
        const response = await call('pwit.controllers.api.create_session', {})
        if (response) {
            localStorage.setItem('session', JSON.stringify(response))
        }
    }
}
onMounted(() => {
    create_session()
})
</script>