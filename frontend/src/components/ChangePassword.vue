<template>
    <TransitionRoot as="template" :show="store.isOpenPas">
        <Dialog class="relative z-20" @close="store.isOpenPas = false">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full justify-center text-center items-center px-4 sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 w-full sm:max-w-2xl">
                            <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class="block justify-center gap-5 items-center">
                                </div>
                                <div class="space-y-3 container">
                                    <div>
                                        <label for="new_password" class="block text-gray-800 text-sm pb-2">
                                            New Password
                                        </label>
                                        <input v-model="newPassword" id="new_password" type="password"
                                            placeholder="Enter New Password"
                                            class="w-full px-3 py-2 border-b bg-[#f3f4f8] border-gray-300 shadow-sm outline-none">
                                    </div>
                                   
                                    <div class="flex flex-col gap-1 w-full relative">
                                        <label for="Confirm_pass" class="block text-gray-800 text-sm pb-1">
                                            Confirm Password
                                        </label>
                                        <input @keyup="onchange"  v-model="confirmPassword" id="Confirm_pass" :type="show_pass ? 'text' : 'password'"
                                            class="outline-none w-full border-b-2  bg-[#f3f4f8] text-sm px-3 h-12 text-h5"
                                            placeholder="Confirm New Password">
                                        <span
                                            class="absolute right-2 top-11 font-semibold text-gray-500 text-xs cursor-pointer"
                                            @click="show_pass = !show_pass">
                                            <EyeOff class="w-5 h-4 text-gray-500" v-if="show_pass" />
                                            <Eye class="w-5 h-4 text-gray-500" v-else />
                                        </span>
                                        <div>
                                            <p v-if="passwordsMatch === false" class="text-red-500 text-sm ">Passwords
                                                do not match</p>
                                        </div>
                                    </div>
                                    <div class="flex justify-between">
                                        <button @click="handleClick"
                                            class="text-white w-full bg-secondary py-2 px-8 rounded-md">
                                            Update
                                        </button>

                                    </div>
                                </div>
                            </div>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
</template>

<script setup>
import { ref, watch, inject } from 'vue'
import { TransitionChild, TransitionRoot, Dialog, DialogPanel } from '@headlessui/vue'
import {Eye,EyeOff} from 'lucide-vue-next'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const newPassword = ref('');
const confirmPassword = ref('');
const passwordsMatch = ref(null);
const show_pass = ref(false)
const props = defineProps({
    isOpen: {
        type: Boolean,
        required: false,
        default: false
    }
})
const onchange = () => {
    passwordsMatch.value = newPassword.value === confirmPassword.value;
};
const handleClick = async() => {
    if (passwordsMatch.value && newPassword.value.length > 5 && confirmPassword.value.length > 5) {
        let res = await call('pwit.controllers.api.change_password', {
            user: auth.cookie.user_id,
            new_password: newPassword.value,
        });
        if (res.code === 200) {
            toast.success('Password changed successfully');
            newPassword.value = '';
            confirmPassword.value = '';
            store.isOpenPas = false;
        }
    } else {
        Confirm_pass.style.borderBottom = '1px solid red';
    }
};

</script>