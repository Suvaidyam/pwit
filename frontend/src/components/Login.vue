<template>
    <div v-if="!store.isForgetPas" class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
        <div class="sm:flex sm:items-start">
            <div class="mt-3 text-center sm:mt-0 sm:text-left">
                <DialogTitle as="h3" class="text-h3 font-bold text-[#21272A]">Login to
                    PAY-WHAT-IT-TAKES INDIA INITIATIVE </DialogTitle>
                <p class="text-h5 pt-2 text-center text-trbase font-normal">Please provide the
                    following
                    information to continue </p>
            </div>
        </div>
        <div class="flex flex-col gap-3 pt-4">
            <div class="flex flex-col gap-2 w-full">
                <label for="" class="text-sm text-tatary">Email Address
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="login" @input="resetBorder" id="emailInputId" v-model="email" type="email"
                    class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                    placeholder="Enter Email Address">
            </div>
            <div class="flex flex-col gap-2 w-full relative">
                <label for="" class="text-sm text-tatary">Password
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="login" @input="validatePassword" id="passwordInputId" v-model="password"
                    :type="show_pass ? 'text' : 'password'"
                    class="outline-none w-full border-b-2 bg-gray-50 text-sm px-3 h-12 text-h5" placeholder="******">
                <span class="absolute right-2 top-10 font-semibold text-gray-500 text-xs cursor-pointer"
                    @click="show_pass = !show_pass">
                    <EyeOff class="w-5 h-5 text-gray-500" v-if="show_pass" />
                    <Eye class="w-5 h-5 text-gray-500" v-else />
                </span>
                <p v-if="errorMessage" class="text-red-500 text-xs mt-1 absolute -bottom-5">{{ errorMessage }}</p>
            </div>
            <div class="flex justify-between py-3">
                <div class="flex items-center gap-2">
                    <input v-model="remember" type="checkbox" id="remember" class="h-4 w-4" />
                    <label for="remember" class="text-sm text-gray-500">Remember me</label>
                </div>
                <p @click="store.isForgetPas = true" class="text-green-400 text-sm cursor-pointer">Forgot Password?</p>
            </div>
            <div class="w-full border-b h-14">
                <button :disabled="remember ? false : true" type="button"
                    :class="remember ? 'bg-secondary text-white' : 'bg-slate-300 text-gray-500'"
                    class=" w-full justify-center rounded-md px-3 h-12 text-h5 font-normal  shadow-sm"
                    @click="login">Log In</button>
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
const email = ref('')
const password = ref('')
const errorMessage = ref('')
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const cur_session = ref(JSON.parse(localStorage.getItem('session'))?.data?.name)

const validateEmail = (email) => {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

const login = async () => {
    const email = document.getElementById('emailInputId');
    const password = document.getElementById('passwordInputId');
    let valid = true;

    email.style.borderBottom = '';
    password.style.borderBottom = '';

    if (!email.value || !password.value) {
        // alert("Please enter both email and password");

        if (!email.value) {
            email.style.borderBottom = '1px solid red';
            valid = false;
        }
        if (!password.value) {
            password.style.borderBottom = '1px solid red';
            valid = false;
        }
        return;
    }
    if (!validateEmail(email.value)) {
        email.style.borderBottom = '1px solid red';
        toast.error("Invalid Email Address.");
        valid = false;
        return;
    }
    let res
    try {
        if(errorMessage.value == ''){
            res = await auth.login(email.value, password.value);
            if (res) {
                store.auth = false;
                toast.success('Login Successful');
            }
        }

    } catch (error) {
        toast.error('Invalid login credentials');
    }
    if (res && cur_session.value) {
        const response = await call('pwit.controllers.api.set_user_session', {
            name: cur_session.value,
            user: email.value
        });

        if (response) {
            setTimeout(() => {
                window.location.reload();
            }, 500);
        }
    }
};

const validatePassword = () => {
    const minLength = 8;
    const hasNumber = /\d/.test(password.value);
    const hasSpecialChar = /[!@#$%^&*]/.test(password.value);

    if (!password.value) {
        errorMessage.value = 'Password is required.';
    } else if (password.value.length < minLength) {
        errorMessage.value = `Password must be at least ${minLength} characters.`;
    } else if (!hasNumber) {
        errorMessage.value = 'Password must include at least one number.';
    } else if (!hasSpecialChar) {
        errorMessage.value = 'Password must include at least one special character.';
    } else {
        errorMessage.value = '';
    }
}

watch(() => cur_session.value, (value) => {
    cur_session.value = value
});
</script>