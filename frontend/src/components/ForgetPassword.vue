<template>
    <div class="">
        <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="block justify-center gap-5 items-center">
            </div>
            <div class="space-y-6 container">
                <div>
                    <input v-model="email" id="email" type="email" placeholder="Enter Email Address"
                        class="w-full px-3 py-2 border-b bg-[#f3f4f8] border-gray-300 shadow-sm outline-none">
                </div>
                <div class="flex flex-col items-center gap-2 justify-center">
                    <button :disabled="email ? false : true"
                        :class="email ? 'text-white bg-secondary' : 'bg-gray-300 text-gray-500'" @click="reset_password"
                        class="w-full py-2 px-8 rounded-md">
                        Reset Password
                    </button>
                    <p @click="store.isForgetPas=false" class="text-sm cursor-pointer">Back to Login</p>
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
const store = inject('store');

const reset_password = async () => {
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
                const result = await response.json();
                console.log(result)
                toast.success('Password changed successfully');
            }
        } catch (error) {
            toast.error('Please setup email settings');
        }
    }
};

</script>