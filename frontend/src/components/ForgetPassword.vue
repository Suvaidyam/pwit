<template>
    <div class="">
        <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="block justify-center gap-5 items-center">
            </div>
            <div class="space-y-6 container">
                <div>
                    <input v-model="email" id="email" type="email" placeholder="Enter Email Address"
                        class="w-full px-3 py-2.5 border-b bg-gray-100 placeholder:text-[#697077] border-gray-300 shadow-sm outline-none">
                </div>
                <div class="flex flex-col items-center gap-2 justify-center">
                    <button :disabled="email ? false : true"
                        :class="email ? 'text-white bg-secondary' : 'bg-gray-300 text-gray-500'" @click="reset_password"
                        class="w-full py-2 px-8 rounded-md flex items-center justify-center gap-2">
                        <div v-if="loading" class="h-5 w-5 ">
                            <div
                                class="animate-spin h-full w-full rounded-full border-2 border-t-[#00A0DC] border-b-[#00A0DC]">
                            </div>
                        </div>
                        <p v-if="loading"> verifying...</p>
                        <p v-if="!loading">Reset Password</p>
                    </button>
                    <p @click="store.isForgetPas = false" class="text-sm cursor-pointer">Back to Login</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, inject } from 'vue'
// import {} from 'lucide-vue-next'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const email = ref('');
const loading = ref(false);
const store = inject('store');

const reset_password = async () => {
    loading.value = true;
    if (email.value) {
        const formData = new FormData();
        formData.append('cmd', 'frappe.core.doctype.user.user.reset_password');
        formData.append('user', email.value);
        try {
            const response = await fetch('/', {
                method: 'POST',
                body: formData,
                headers: {
                },
            });

            if (response.ok) {
                loading.value = false;
                const result = await response.json();
                toast.success('Password reset instructions have been sent to your email');
                store.authPopup=false;
                email.value = '';
            } else {
                loading.value = false;
                toast.error(`Email ${response.statusText}`);
            }
        } catch (error) {
            loading.value = false;
            toast.error('Please setup email settings');
        }
    }
};

</script>