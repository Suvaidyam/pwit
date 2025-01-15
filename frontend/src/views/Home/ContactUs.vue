<template>
    <div class="absolute bg-white shadow-lg py-6 -top-24 w-full lg:w-[65%] px-4 md:px-8 lg:px-20">
        <h2 class="text-h2 font-bold font-primary text-center text-primary mb-6">Contact Us</h2>
        <div class="space-y-6">
            <div class="relative">
                <label class="block text-gray-800 text-sm mb-2">
                    Full Name <span class="text-red-500">*</span>
                </label>
                <input v-model="data.full_name" @input="clearError('full_name')" type="text"
                    placeholder="Enter full name" :class="[
                        'w-full px-3 py-2 border-b bg-[#f3f4f8] border-gray-300 shadow-sm outline-none',
                        { 'border-red-500': errors.full_name }
                    ]" />
                <p v-if="errors.full_name" class="text-red-500 text-h6 absolute -bottom-5 mt-1">{{ errors.full_name }}</p>
            </div>
            <div class="relative">
                <label class="block text-gray-800 text-sm mb-2">
                    Email Address <span class="text-red-500">*</span>
                </label>
                <input v-model="data.email" @input="clearError('email')" type="email" placeholder="Enter email address"
                    :class="[
                        'w-full px-3 py-2 border-b bg-[#f3f4f8] border-gray-300 shadow-sm outline-none',
                        { 'border-red-500': errors.email }
                    ]" />
                <p v-if="errors.email" class="text-red-500 text-h6 absolute -bottom-5 mt-1">{{ errors.email }}</p>
            </div>
            <div class="relative">
                <label class="block text-gray-800 text-sm mb-2">
                    Your Message <span class="text-red-500">*</span>
                </label>
                <textarea v-model="data.message" @input="clearError('message')" placeholder="Start writing from here"
                    :class="[
                        'w-full px-3 py-2 h-24 border-b bg-[#f3f4f8] border-gray-300 shadow-sm outline-none',
                        { 'border-red-500': errors.message }
                    ]"></textarea>
                <p v-if="errors.message" class="text-red-500 text-h6  absolute -bottom-5 ">{{ errors.message }}</p>
            </div>
            <div class="flex justify-center">
                <button type="button" @click="sendMessage" :disabled="loading"
                    class="w-full sm:w-[169px] h-12 rounded-md bg-secondary text-white text-h5 text-center shadow-md">
                    <p v-if="loading"> Sending...</p>
                    <p v-if="!loading">Send Message</p>
                </button>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, inject } from 'vue';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const data = ref({
    full_name: '',
    email: '',
    message: ''
});

const errors = ref({
    full_name: '',
    email: '',
    message: ''
});
const loading = ref(false);
const clearError = (field) => {
    errors.value[field] = '';
};

// Validates the form inputs
const validateForm = () => {
    let isValid = true;

    if (!data.value.full_name.trim()) {
        errors.value.full_name = 'Full Name is required.';
        isValid = false;
    } else if (!/^[A-Za-z\s]+$/.test(data.value.full_name.trim())) {
        errors.value.full_name = 'Full Name can only contain letters and spaces.';
        isValid = false;
    }

    if (!data.value.email.trim()) {
        errors.value.email = 'Email Address is required.';
        isValid = false;
    } else if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(data.value.email.trim())) {
        errors.value.email = 'Invalid Email Address.';
        isValid = false;
    }

    if (!data.value.message.trim()) {
        errors.value.message = 'Message is required.';
        isValid = false;
    } else {
        const wordCount = data.value.message.trim().split(/\s+/).length;
        if (wordCount < 1) {
            errors.value.message = 'Message must contain at least 10 words.';
            isValid = false;
        }
    }
    return isValid;
};

const call = inject('$call');
const sendMessage = async () => {
    if (!validateForm()) {
        toast.error('Please fill in all required fields');
        return;
    }

    const session = (() => {
        try {
            return JSON.parse(sessionStorage.getItem('session')) || {};
        } catch (err) {
            console.error('Invalid session data', err);
            return {};
        }
    })();

    try {
        loading.value = true;
        const res = await call('pwit.controllers.api.contact_us', {
            data: {
                ...data.value,
                session: session?.data?.name || ''
            }
        });
        switch (res.code) {
            case 200:
                toast.success('Successfully submitted');
                loading.value = false;
                // Clear the form fields
                data.value = {
                    full_name: '',
                    email: '',
                    message: ''
                };
                break;
            case 400:
                toast.error(res.msg || 'Validation error occurred');
                break;
            default:
                toast.error('Something went wrong');
        }
    } catch (error) {
        toast.error('Request failed.');
    }
};
</script>
