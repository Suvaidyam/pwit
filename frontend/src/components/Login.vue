<template>
    <div v-if="!store.isForgetPas" class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
        <div class="">
            <div class="mt-3 text-center ">
                <p class="text-h3 md:text-h2 text-center leading-[26px] font-bold font-primary text-sebase">Login to the Assistive Funder Toolkit </p>
                <p class="text-h5 pt-2 text-center text-sebase leading-4 tracking-[5%] font-normal">Please provide the
                    following
                    information to continue </p>
            </div>
        </div>
        <div class="flex flex-col gap-4 pt-4">
            <div class="flex flex-col gap-2 w-full relative">
                <label for="" class="text-sm text-sebase">Email Address
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="login" @input="(e) => validateEmail(e.target.value)" id="emailInputId"
                    v-model="email" type="email" class="outline-none w-full border-b-2 bg-gray-100 placeholder:text-[#697077] px-3 h-12 text-h5"
                    placeholder="Enter email address">
                <div class="absolute -bottom-6">
                    <p v-if="errorMessage" class="text-sm text-red-600">{{ errorMessage }}</p>
                </div>
            </div>
            <div class="flex flex-col gap-2 w-full relative pt-2">
                <label for="" class="text-sm text-sebase">Password
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="login" id="passwordInputId" v-model="password"
                    :type="show_pass ? 'text' : 'password'"
                    class="outline-none w-full border-b-2 bg-gray-100 placeholder:text-[#697077] text-sm px-3 h-12 text-h5" placeholder="******">
                <span class="absolute right-2 top-12 font-semibold text-gray-500 text-xs cursor-pointer"
                    @click="show_pass = !show_pass">
                    <EyeOff class="w-5 h-5 text-gray-500" v-if="show_pass" />
                    <Eye class="w-5 h-5 text-gray-500" v-else />
                </span>
            </div>
            <div class="flex justify-between py-2">
                <div class="flex items-center gap-2">
                    <input v-model="remember" type="checkbox" id="remember" class="h-4 w-4" />
                    <label for="remember" class="text-sm text-gray-700">Remember me</label>
                </div>
                <p @click="store.isForgetPas = true" class="text-blue-600 text-sm cursor-pointer">Forgot Password?</p>
            </div>
            <div class="w-full border-b h-14">
                <button :disabled="isValid ? false : false" type="button"
                    :class="true ? 'bg-secondary text-white' : 'bg-gray-300 text-gray-600'"
                    class=" w-full flex items-center gap-2 justify-center rounded-md px-3 h-12 text-h5 font-normal  shadow-sm"
                    @click="login">
                    <div v-if="loading" class="h-5 w-5 ">
                        <div
                            class="animate-spin h-full w-full rounded-full border-2 border-t-[#00A0DC] border-b-[#00A0DC]">
                        </div>
                    </div>
                    <p v-if="loading"> verifying...</p>
                    <p v-if="!loading"> Log In</p>
                </button>
            </div>
            <div class="flex items-center justify-center">
                <span class="font-extralight text-gray-600 text-sm">No account yet?
                    <span class="text-primary cursor-pointer" @click="store.auth = true">Sign
                        Up</span>
                </span>
            </div>
        </div>
    </div>
    <ForgetPassword v-if="store.isForgetPas" />
</template>

<script setup>
import { ref, inject, watch } from 'vue'
import { DialogTitle } from '@headlessui/vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { Eye, EyeOff } from 'lucide-vue-next'
import ForgetPassword from './ForgetPassword.vue';

const show_pass = ref(false)
const remember = ref(false)
const loading = ref(false)
const email = ref('')
const password = ref('')
const errorMessage = ref('')

const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');

const validateEmail = (email) => {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    let valid = emailPattern.test(email);
    if (!valid && email.length > 5) {
        errorMessage.value = 'Invalid Email Address.';
    } else {
        errorMessage.value = '';
    }
}

const login = async () => {
    let res
    try {
        if (errorMessage.value == '') {
            loading.value = true;
            res = await auth.login(email.value, password.value);
            if (res) {
                store.auth = false;
                store.authPopup = false;
                toast.success('Login Successful');
                loading.value = false;
            }
        }

    } catch (error) {
        toast.error('Invalid login credentials');
        loading.value = false;
    }
    if (res && store.session) {
        const response = await call('pwit.controllers.api.set_user_session', {
            name: store.session,
            user: email.value
        });

        if (response) {
            setTimeout(() => {
                window.location.reload();
            }, 500);
        }
    }
};


watch(() => store.session, (value) => {
    store.session = value
});
</script>