<template>
    <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4">
        <div class="mt-3 text-center">
            <DialogTitle as="h3" class="text-h3 md:text-h2 font-bold text-sebase font-primary text-center">Sign up and
                create an account
            </DialogTitle>
            <p class="text-h5 pt-2 text-center text-primary">Please provide the following
                information to continue </p>
            <p class="text-h6 pt-2 text-justify text-sebase">The Assistive Funder Toolkit has been designed to maintain
                complete anonymity of
                respondent. Significant precautions have been taken in the design architecture to
                ensure that Bridgespan, ISDM or any other party involved cannot correlate the
                responses with personally identifiable information. Any analysis conducted or trends
                inferred from the data collected through this toolkit will exclusively be done at an
                aggregate level. </p>
        </div>
        <div class="flex flex-col gap-3 pt-4">
            <div class="flex flex-col gap-2 w-full relative">
                <label for="full_name" class="text-sm text-tatary">
                    Full Name
                    <span class="text-red-500">
                        *
                    </span>
                </label>
                <input @keydown.enter="register" v-model="formData.full_name" type="text" id="full_name"
                    class="outline-none w-full border-b-2 bg-gray-100 placeholder:text-[#697077] px-3 h-12 text-h5"
                    placeholder="Enter full name">
                <p v-if="errors.full_name" class="absolute -bottom-5 text-red-500 text-h6 mt-1">{{
                    errors.full_name
                }}</p>
            </div>
            <div class="flex flex-col gap-2 w-full relative pt-2">
                <label for="" class="text-sm text-tatary">
                    Email Address
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="register" id="emailInputId" v-model="formData.email" type="email"
                    class="outline-none w-full border-b-2 bg-gray-100 placeholder:text-[#697077] px-3 h-12 text-h5"
                    placeholder="Enter email address">
                <div class="absolute -bottom-6">
                    <p v-if="errors.email" class="text-h6 text-red-600">{{ errors.email }}</p>
                    <p v-else class="text-h6 text-[#697077]">Sign up with work email</p>
                </div>
            </div>
            <div class="flex flex-col gap-5 pt-3">
                <div class="flex flex-col gap-2 relative">
                    <label for="designation" class="text-h5 font-normal text-[#21272A]">
                        Please share your designation
                        <span class="text-red-500">*</span>
                    </label>
                    <select id="designation" v-model="formData.designation"
                        class="outline-none border-b-2 bg-gray-50 py-3 text-black px-2"
                        :class="[!errors.designation ? 'border-gray-400' : 'border-red-500']">
                        <option value="">Select</option>
                        <option v-for="item in dropdown_options.designation" :value="item" :key="item">{{ item }}</option>
                    </select>
                    <p v-if="errors.designation" class="absolute -bottom-5 text-red-500 text-h6 mt-1">{{
                        errors.designation
                    }}</p>
                </div>

                <div class="relative">
                    <p class="text-h5 font-normal text-[#21272A]">
                        Please select which funder type your organisation identifies as
                        <span class="text-red-500">*</span>
                    </p>
                    <label v-for="item in dropdown_options.funder_type" :key="item"
                        class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                        <input type="radio" id="option" :value="item" v-model="formData.funder_type"
                            class="cursor-pointer" />
                        <p class="text-secondary font-normal text-sm cursor-pointer">
                            {{ item }}
                        </p>
                    </label>
                    <p v-if="errors.funder_type" class="absolute -bottom-5 text-red-500 text-h6 mt-1">{{
                        errors.funder_type
                    }}</p>
                </div>

                <div class="flex flex-col gap-2 relative">
                    <label for="annual_budget" class="text-h5 font-normal text-[#21272A]">
                        Your organisation’s approximate annual budget allocation
                        <span class="text-red-500">*</span>
                    </label>
                    <select id="annual_budget" v-model="formData.annual_budget"
                        class="outline-none border-b-2 bg-gray-50 py-3 text-gray-900 px-2"
                        :class="[!errors.annual_budget ? 'border-gray-400' : 'border-red-500']">
                        <option value="">Select</option>
                        <option v-for="item in dropdown_options.annual_budget" :value="item" :key="item">{{item}}</option> 
                    </select>
                    <p v-if="errors.annual_budget" class="absolute -bottom-5 text-red-500 text-h6 mt-1">
                        {{
                            errors.annual_budget }}</p>
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
import { ref, watch, inject, onMounted } from 'vue'
import { DialogTitle } from '@headlessui/vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const open = ref(false)
const loading = ref(false)
const remember = ref(false)
const store = inject('store');
const call = inject('$call');
const formData = ref({
    email: '',
    full_name: '',
    designation: '',
    funder_type: '',
    annual_budget: ''
})
const errors = ref({
    email: '',
    full_name: '',
    designation: '',
    funder_type: '',
    annual_budget: ''
});
const dropdown_options = ref({})
const validateForm = () => {
    errors.value.full_name = formData.value.full_name ? '' : 'Full name is required.';
    errors.value.email = formData.value.email ? '' : 'Email is required.';
    errors.value.designation = formData.value.designation ? '' : 'Designation is required.';
    errors.value.funder_type = formData.value.funder_type.length ? '' : 'Funder type is required';
    errors.value.annual_budget = formData.value.annual_budget ? '' : 'Annual budget is required.';
    return !errors.value.full_name && !errors.value.email && !errors.value.designation && !errors.value.funder_type && !errors.value.annual_budget;
};
const emailvalidate = () => {
    const minLength = 3;
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!formData.value.email) {
        errors.value.email = 'Email is required.';
    } else if (formData.value.email.length < minLength) {
        errors.value.email = `Email must be at least ${minLength} characters.`;
    } else if (!emailPattern.test(formData.value.email)) {
        errors.value.email = 'Invalid email';
    } else {
        errors.value.email = '';
    }
};
const dropdown_option = async () => {
    let res = await call('pwit.controllers.api.profile_dropdown_options', {})
    if (res.code === 200) {
        dropdown_options.value = res.data
    }
}
const register = async () => {
    open.value = false;
    if (validateForm()) {
        loading.value = true;

        const res = await call('pwit.controllers.api.register', {
            data: formData.value
        });

        if (res.code === 200) {
            toast.success('A verification email has been sent on the email address provided, please follow the link to set up your password.');
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
onMounted(() => {
    dropdown_option()
})
</script>