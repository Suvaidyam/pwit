<template>
    <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4">
        <div class="mt-3 text-center">
            <DialogTitle as="h3" class="text-h3 font-bold text-[#21272A] text-center">Sign Up
            </DialogTitle>
            <p class="text-h5 pt-2 text-center text-trbase">Please provide the following
                information to continue </p>
        </div>
        <div class="flex flex-col gap-3 pt-4">
            <div class="flex flex-col gap-2 w-full">
                <label for="full_name" class="text-sm text-tatary">
                    Full Name
                    <span class="text-red-500">
                        *
                    </span>
                </label>
                <input @keydown.enter="register" @input="resetBorder" v-model="full_name" type="text" id="full_name"
                    class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5" placeholder="Enter Full Name">
            </div>
            <div class="flex flex-col gap-2 w-full">
                <label for="" class="text-sm text-tatary">
                    Email Address
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="register" @input="resetBorder" id="emailInputId" v-model="email" type="email"
                    class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                    placeholder="Enter Email Address">
            </div>
            <div class="flex flex-col gap-2 w-full relative">
                <label for="" class="text-sm text-tatary">
                    Password
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="register" @input="validatePassword" id="passwordInputId" v-model="password"
                    :type="show_pass ? 'text' : 'password'"
                    class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5" placeholder="******">
                <span class="absolute right-2 top-10 text-xs cursor-pointer" @click="show_pass = !show_pass">
                    <EyeOff class="w-5 h-5 text-gray-500" v-if="show_pass" />
                    <Eye class="w-5 h-5 text-gray-500" v-else />
                </span>
                <p v-if="errorMessage" class="text-red-500 text-xs mt-1 absolute -bottom-5">{{ errorMessage }}</p>
            </div>
            <div class="flex items-center gap-2 py-2">
                <input v-model="remember" type="checkbox" id="remember" class="h-4 w-4" />
                <label for="remember" class="text-sm text-gray-500">Remember me</label>
            </div>
            <div class="w-full border-b h-14">
                <button :disabled="remember ? false : true" type="button"
                    :class="remember ? 'bg-secondary text-white' : 'bg-slate-300 text-gray-500'"
                    class=" w-full justify-center rounded-md px-3 h-12 text-h5 font-normal shadow-sm"
                    @click="register">Sign Up</button>
            </div>
            <div class="flex items-center justify-center">
                <span class="font-extralight text-gray-600 text-sm">Already a user?
                    <span class="text-primary cursor-pointer" @click="store.auth =false">Log
                        In</span>
                </span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject } from 'vue'
import {  DialogTitle } from '@headlessui/vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { Eye, EyeOff } from 'lucide-vue-next'

const open = ref(false)
const show_pass = ref(false)
const remember = ref(false)
const email = ref('')
const full_name = ref('')
const password = ref('')
const errorMessage = ref('')
const store = inject('store');
const call = inject('$call');

const validateEmail = (email) => {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

const register = async () => {
    const emailEl = document.getElementById('emailInputId');
    const passwordEl = document.getElementById('passwordInputId');
    const fullNameEl = document.getElementById('full_name');
    let valid = true;

    fullNameEl.style.borderBottom = emailEl.style.borderBottom = passwordEl.style.borderBottom = '';

    if (!full_name.value || !email.value || !password.value) {

        if (!full_name.value) {
            fullNameEl.style.borderBottom = '1px solid red';
            valid = false;
        }

        if (!email.value) {
            emailEl.style.borderBottom = '1px solid red';
            valid = false;
        }

        if (!password.value) {
            passwordEl.style.borderBottom = '1px solid red';
            valid = false;
        }
        return;
    }

    if (!validateEmail(email.value)) {
        emailEl.style.borderBottom = '1px solid red';
        toast.error("Invalid Email Address.");
        valid = false;
        return
    }
    open.value = false;
    const res = await call('pwit.controllers.api.register', {
        data: {
            email: email.value,
            full_name: full_name.value,
            password: password.value,
        }
    });

    if (res.code === 200) {
        toast.success('Registration Successful');
        store.auth = 'Log In';
    } else {
        toast.error('Registration Failed');
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
// const resetBorder = (event) => {
//     event.target.style.borderBottom = '';
// }
</script>