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
                <input @keydown.enter="register" @input="emailvalidate" id="emailInputId" v-model="email" type="email"
                    class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                    placeholder="Enter Email Address">
                <p v-if="errorMessage" class="text-red-500 text-xs mt-1   -bottom-5">{{ errorMessage }}</p>
            </div>

            <div class="flex items-center gap-2 py-2">
                <input v-model="remember" type="checkbox" id="remember" class="h-4 w-4" />
                <label for="remember" class="text-sm text-gray-500">Remember me</label>
            </div>
            <div class="w-full border-b h-14">
                <button :disabled="remember ? false : true" type="button"
                    :class="remember ? 'bg-secondary text-white' : 'bg-gray-300 text-gray-600'"
                    class=" w-full flex items-center gap-2 justify-center rounded-md px-3 h-12 text-h5 font-normal shadow-sm"
                    @click="register">
                    <div v-if="loading" class="h-5 w-5 ">
                        <div
                            class="animate-spin h-full w-full rounded-full border-2 border-t-[#00A0DC] border-b-[#00A0DC]">
                        </div>
                    </div>
                    <p v-if="loading"> verifying...</p>
                    <p v-if="!loading">Sign Up</p>
                </button>
            </div>
            <div class="flex items-center justify-center">
                <span class="font-extralight text-gray-600 text-sm">Already a user?
                    <span class="text-primary cursor-pointer" @click="store.auth = false">Log
                        In</span>
                </span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject } from 'vue'
import { DialogTitle } from '@headlessui/vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const open = ref(false)
const loading = ref(false)
const remember = ref(false)
const email = ref('')
const full_name = ref('')
const errorMessage = ref('')
const store = inject('store');
const call = inject('$call');

const emailvalidate = () => {
    const minLength = 3;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!email.value) {
        errorMessage.value = 'Email is required.';
    } else if (email.value.length < minLength) {
        errorMessage.value = `Email must be at least ${minLength} characters.`;
    } else if (!emailPattern.test(email.value)) {
        errorMessage.value = 'Invalid email format.';
    } else {
        errorMessage.value = ''; 
    }
};

const register = async () => {

    const emailEl = document.getElementById('emailInputId');
    const fullNameEl = document.getElementById('full_name');
    let valid = true;

    fullNameEl.style.borderBottom = emailEl.style.borderBottom = '';

    if (!full_name.value || !email.value) {

        if (!full_name.value) {
            fullNameEl.style.borderBottom = '1px solid red';
            valid = false;
        }

        if (!email.value) {
            emailEl.style.borderBottom = '1px solid red';
            valid = false;
        }

        return;
    }
    open.value = false;
    if (errorMessage.value == '') {
        loading.value = true;

        const res = await call('pwit.controllers.api.register', {
            data: {
                email: email.value,
                full_name: full_name.value,
            }
        });

        if (res.code === 200) {
            toast.success(res.msg); 
            loading.value = false; 
            store.authPopup = false;
        } else {
            setTimeout(() => {
                loading.value = false;
            }, 1000);
            toast.error(res.msg);
        }
    }
};

</script>