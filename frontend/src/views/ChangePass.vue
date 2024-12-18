<template>
    <div class="w-full flex flex-col gap-6 items-center justify-center h-full px-4">
        <img src="../assets/navbar.png" alt="" class="w-52">
        <!-- <div class="flex flex-col items-center">
            <p class="text-secondary text-h4 font-semibold">Assistive Funder Toolkit</p>
            <p class="text-h5">(Developed by the Pay-What-It-Takes India Initiative)</p>
        </div> -->
        <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4 md:max-w-xl border rounded-md shadow-md">
            <div class="block justify-center gap-5 items-center">
            </div>
            <div class="space-y-6 container">
                <div>
                    <label for="new_password" class="block text-gray-800 text-sm pb-2">
                        New Password
                    </label>
                    <input v-model="newPassword" @input="validatePassword" id="new_password" type="password"
                        placeholder="Enter New Password"
                        class="w-full px-3 py-2 border-b bg-gray-100 placeholder:text-[#697077] border-gray-300 shadow-sm outline-none">
                    <p v-if="errorMessage" class="text-red-500 text-xs mt-1 -bottom-5">{{ errorMessage }}</p>
                </div>

                <div class="flex flex-col gap-1 w-full relative">
                    <label for="Confirm_pass" class="block text-gray-800 text-sm pb-1">
                        Confirm Password
                    </label>
                    <input v-model="confirmPassword" @input="confirm_password" id="Confirm_pass"
                        :type="show_pass ? 'text' : 'password'"
                        class="outline-none w-full border-b-2  bg-gray-100 placeholder:text-[#697077] text-sm px-3 h-12 text-h5"
                        placeholder="Confirm New Password">
                    <span class="absolute right-2 top-11 font-semibold text-gray-500 text-xs cursor-pointer"
                        @click="show_pass = !show_pass">
                        <EyeOff class="w-5 h-4 text-gray-500" v-if="show_pass" />
                        <Eye class="w-5 h-4 text-gray-500" v-else />
                    </span>
                    <p v-if="errorCofirm" class="text-red-500 text-xs mt-1 -bottom-5">{{ errorCofirm }}</p>
                </div>
                <button @click="handleClick"
                    class="w-full flex items-center justify-center gap-2 text-white bg-secondary py-2 px-8 rounded-md">
                    <div v-if="loading" class="h-5 w-5 ">
                        <div
                            class="animate-spin h-full w-full rounded-full border-2 border-t-[#00A0DC] border-b-[#00A0DC]">
                        </div>
                    </div>
                    Update
                </button>

            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { Eye, EyeOff } from 'lucide-vue-next'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { useRoute, useRouter } from 'vue-router';



const newPassword = ref('');
const confirmPassword = ref('');
const show_pass = ref(false)
const loading = ref(false)
const route = useRoute();
const router = useRouter();
const errorMessage = ref('')
const errorCofirm = ref('')

const validatePassword = () => {
    const minLength = 8;
    const hasNumber = /\d/.test(newPassword.value);
    const hasSpecialChar = /[!@#$%^&*]/.test(newPassword.value);

    if (!newPassword.value) {
        errorMessage.value = 'Password is required.';
    } else if (newPassword.value.length < minLength) {
        errorMessage.value = `Password must be at least ${minLength} characters.`;
    } else if (!hasNumber) {
        errorMessage.value = 'Password must include at least one number.';
    } else if (!hasSpecialChar) {
        errorMessage.value = 'Password must include at least one special character.';
    } else {
        errorMessage.value = '';
    }
}
const confirm_password = () => {
    if (newPassword.value == confirmPassword.value) {
        errorCofirm.value = '';
    } else {
        errorCofirm.value = 'Passwords do not match';
    }
}
const handleClick = async () => {
    if (route.query.key) {
        const formData = new FormData();
        formData.append('key', route.query.key);
        formData.append('new_password', newPassword.value);
        formData.append('confirm_password', confirmPassword.value);
        formData.append('logout_all_sessions', 1);
        formData.append('cmd', 'frappe.core.doctype.user.user.update_password');
        if (errorCofirm.value == '' && errorMessage.value == '' && newPassword.value != '' && confirmPassword.value != '') {
            loading.value = true;
            try {
                const response = await fetch('/', {
                    method: 'POST',
                    body: formData,
                    headers: {
                    },
                });

                if (response.ok) {
                    const result = await response.json();
                    toast.success('Password updated successfully');
                    newPassword.value = '';
                    confirmPassword.value = '';
                    setTimeout(() => {
                        loading.value = false;
                        router.push('/')
                    }, 500);
                } else {
                    toast.error(`Email ${response.statusText}`);
                    setTimeout(() => {
                        loading.value = false;
                    }, 500);
                }
            } catch (error) {
                toast.error('Please setup email settings');
                setTimeout(() => {
                    loading.value = false;
                }, 500);
            }
        }
    }
};

</script>