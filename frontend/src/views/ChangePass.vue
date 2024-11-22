<template>
    <div class="w-full flex flex-col gap-6 items-center justify-center h-full px-4">
        <img :src="`/files/logo.png`" alt="" class="w-52">
        <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4 md:max-w-xl border rounded-md shadow-md">
            <div class="block justify-center gap-5 items-center">
            </div>
            <div class="space-y-6 container">
                <div>
                    <label for="new_password" class="block text-gray-800 text-sm pb-2">
                        New Password
                    </label>
                    <input v-model="newPassword" id="new_password" type="password" placeholder="Enter New Password"
                        class="w-full px-3 py-2 border-b bg-[#f3f4f8] border-gray-300 shadow-sm outline-none">
                </div>

                <div class="flex flex-col gap-1 w-full relative">
                    <label for="Confirm_pass" class="block text-gray-800 text-sm pb-1">
                        Confirm Password
                    </label>
                    <input v-model="confirmPassword" id="Confirm_pass" :type="show_pass ? 'text' : 'password'"
                        class="outline-none w-full border-b-2  bg-[#f3f4f8] text-sm px-3 h-12 text-h5"
                        placeholder="Confirm New Password">
                    <span class="absolute right-2 top-11 font-semibold text-gray-500 text-xs cursor-pointer"
                        @click="show_pass = !show_pass">
                        <EyeOff class="w-5 h-4 text-gray-500" v-if="show_pass" />
                        <Eye class="w-5 h-4 text-gray-500" v-else />
                    </span>
                </div>
                <div class="flex justify-between">
                    <div>
                        <p v-if="passwordsMatch === false" class="text-red-500 text-sm ">Passwords
                            do not match</p>
                    </div>
                    <button @click="handleClick" class="w-full text-white bg-secondary py-2 px-8 rounded-md">
                        Update
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, inject } from 'vue'
import { Eye, EyeOff } from 'lucide-vue-next'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { useRoute,useRouter } from 'vue-router';


const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const newPassword = ref('');
const confirmPassword = ref('');
const passwordsMatch = ref(null);
const show_pass = ref(false)
const route = useRoute();
const router = useRouter();

const handleClick = async () => {
    passwordsMatch.value = newPassword.value === confirmPassword.value;
    if (!passwordsMatch.value) {
        Confirm_pass.style.borderBottom = '1px solid red';
    } else if (route.query.key) {
        const formData = new FormData();
        formData.append('key', route.query.key);
        formData.append('new_password', newPassword.value);
        formData.append('confirm_password', confirmPassword.value);
        formData.append('logout_all_sessions', 1);
        formData.append('cmd', 'frappe.core.doctype.user.user.update_password');
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
                    router.push('/')
                }, 500);
            } else { 
                toast.error(`Email ${response.statusText}`);
            }
        } catch (error) {
            toast.error('Please setup email settings');
        }
    }
};

</script>