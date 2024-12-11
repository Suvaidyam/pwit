<template>
    <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4">
        <div class="mt-3 text-center">
            <DialogTitle as="h3" class="text-h3 md:text-h2 font-bold text-sebase font-primary text-center">Sign up and create an account
            </DialogTitle>
            <p class="text-h5 pt-2 text-center text-sebase">Please provide the following
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
                <input @keydown.enter="register" @input="validateName" v-model="full_name" type="text" id="full_name"
                    class="outline-none w-full border-b-2 bg-gray-100 placeholder:text-[#697077] px-3 h-12 text-h5" placeholder="Enter Full Name">
                <span v-if="invalidName" class="text-red-500 text-xs mt-1 -bottom-5">Only letters allowed</span>
                <span v-if="lengthExceeded" class="text-red-500 text-xs mt-1 -bottom-5">Maximum length of 50
                    characters</span>
            </div>
            <div class="flex flex-col gap-2 w-full relative">
                <label for="" class="text-sm text-tatary">
                    Email Address
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="register" @input="emailvalidate" id="emailInputId" v-model="email" type="email"
                    class="outline-none w-full border-b-2 bg-gray-100 placeholder:text-[#697077] px-3 h-12 text-h5"
                    placeholder="Enter Email Address">
                <div class="absolute -bottom-6">
                    <p v-if="errorMessage" class="text-h6 text-red-600">{{ errorMessage }}</p>
                    <p v-else class="text-h6 text-[#697077]">Sign up with work email</p>
                </div>
            </div>

            <div class="flex items-center gap-2 py-2 mt-3">
                <input v-model="remember" type="checkbox" id="remember" class="h-4 w-4" />
                <label for="remember" class="text-sm text-gray-700">Remember me</label>
            </div>
            <div class="w-full border-b h-14">
                <button :disabled="remember ? false : false" type="button"
                    :class="true ? 'bg-secondary text-white' : 'bg-gray-300 text-gray-600'"
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
import { ref, watch, inject, computed } from 'vue'
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
const invalidName = ref(false);
const lengthExceeded = ref(false);

const validateName = () => {
    const regex = /^[A-Za-z ]+$/;
    invalidName.value = !regex.test(full_name.value);
    lengthExceeded.value = full_name.value.length > 50;
};

const remainingCharacters = computed(() => {
    return 50 - full_name.value.length;
});

const emailvalidate = () => {
    const minLength = 3;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!email.value) {
        errorMessage.value = 'Email is required.';
    } else if (email.value.length < minLength) {
        errorMessage.value = `Email must be at least ${minLength} characters.`;
    } else if (!emailPattern.test(email.value)) {
        errorMessage.value = 'Invalid email';
    } else {
        errorMessage.value = '';
    }
};

watch([full_name, email], ([newFullName, newEmail]) => {
    const fullNameEl = document.getElementById('full_name');
    const emailEl = document.getElementById('emailInputId');
    let valid = true;

    fullNameEl.style.borderBottom = emailEl.style.borderBottom = '';
    if (!newFullName) {
        fullNameEl.style.borderBottom = '1px solid red';
        valid = false;
    }

    if (!newEmail) {
        emailEl.style.borderBottom = '1px solid red';
        valid = false;
    }
});


const register = async () => {

    const emailEl = document.getElementById('emailInputId');
    const fullNameEl = document.getElementById('full_name');
    let valid = true;

    fullNameEl.style.borderBottom = emailEl.style.borderBottom = '';
    if (!full_name.value) {
        fullNameEl.style.borderBottom = '1px solid red';
        valid = false;
    }

    if (!email.value) {
        emailEl.style.borderBottom = '1px solid red';
        valid = false;
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
            toast.error('This email is already associated with an account.');
        }
    }
};

</script>