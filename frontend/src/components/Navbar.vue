<template>
    <div
        class="w-full fixed top-0 bg-white z-30 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center shadow-md">
        <router-link to="/" class="text-2xl font-bold text-primary">
            <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/navbar.png" alt="">

        </router-link>
        <div class="flex gap-3 text-sm" v-if="!auth.isLoggedIn">
            <AuthPop />
        </div>
        <div class="flex gap-2 items-center" v-else>{{ auth?.cookie?.full_name }}
            <ProfileDrop />
        </div>
    </div>
</template>

<script setup>
import { ref, inject, onMounted, watch } from 'vue'
import AuthPop from './AuthPop.vue';
import ProfileDrop from './ProfileDrop.vue';
import router from '../router';
const call = inject('$call')
const auth = inject('$auth');
const store = inject('store');
const cur_session = ref(JSON.parse(sessionStorage.getItem('session')))

watch(() => auth.cookie, (value) => {
    auth.cookie = value
});
const create_session = async () => {
    if (!cur_session.value) {
        const response = await call('pwit.controllers.api.create_session', {})
        if (response) {
            sessionStorage.setItem('session', JSON.stringify(response))
            store.session = response?.data?.name
            if (auth.isLoggedIn) {
                const email = auth.cookie.user_id
                await call('pwit.controllers.api.set_user_session', {
                    name: response?.data?.name,
                    user: email
                });
            }
        }
    } else {
        store.session = cur_session.value?.data?.name
    }
}
onMounted(async () => {
    create_session()
    let res = await call('pwit.controllers.api.page_switch', {});
    if (res.data.show_m_page == 1) {
        router.push('/coming-soon')
    } else {
        if (router.currentRoute.value.path == '/coming-soon') {
            router.push('/')
        }
    }
})
</script>