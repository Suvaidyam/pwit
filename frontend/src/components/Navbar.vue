<template>
    <div
        class="w-full fixed top-0 bg-white z-20 px-4 md:px-8 lg:px-20 h-20 flex justify-between items-center shadow-md">
        <router-link to="/" class="text-2xl font-bold text-primary">
            <!-- <img class="w-32 md:w-40 h-12 md:h-[52px]" src="../assets/navbar.png" alt=""> -->
            <div>
                <svg width="159" height="52" viewBox="0 0 159 52" fill="none" xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink">
                    <rect width="159" height="52" fill="url(#pattern0_2084_87)" />
                    <defs>
                        <pattern id="pattern0_2084_87" patternContentUnits="objectBoundingBox" width="1" height="1">
                            <use xlink:href="#image0_2084_87"
                                transform="matrix(0.00403758 0 0 0.0123457 -0.00469757 0)" />
                        </pattern>
                        <image id="image0_2084_87" width="250" height="81"
                            xlink:href="data:image/png;base64,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" />
                    </defs>
                </svg>

            </div>
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
        }
    } else {
        store.session = cur_session.value?.data?.name
    }
}
onMounted(() => {
    create_session()
})
</script>