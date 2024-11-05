<template>
    <button class="w-[74px] h-10 text-h5" @click="openDialog">Register</button>
    <TransitionRoot as="template" :show="open">
        <Dialog class="relative z-20" @close="open = false">
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
                                <div class="mt-3 text-center">
                                    <DialogTitle as="h3" class="text-h3 font-bold text-[#21272A] text-center">Sign Up
                                    </DialogTitle>
                                    <p class="text-h5 pt-2 text-center text-trbase">Please provide the following
                                        information to continue </p>
                                </div>
                                <div class="flex flex-col gap-3 pt-4">
                                    <div class="flex flex-col gap-2 w-full">
                                        <label  for="full_name" class="text-sm text-tatary">
                                            Full Name
                                            <span class="text-red-500">
                                                *
                                            </span>
                                        </label>
                                        <input  @input="resetBorder"  v-model="full_name"  type="text" id="full_name"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                                            placeholder="Enter Full Name">
                                    </div>
                                    <div class="flex flex-col gap-2 w-full">
                                        <label for="" class="text-sm text-tatary">
                                            Email Address
                                            <span class="text-red-500"> *</span>
                                        </label>
                                        <input  @input="resetBorder"  id="emailInputId" v-model="email" type="email"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                                            placeholder="Enter Email Address">
                                    </div>
                                    <div class="flex flex-col gap-2 w-full relative">
                                        <label for="" class="text-sm text-tatary">
                                            Password
                                            <span class="text-red-500"> *</span>
                                        </label>
                                        <input  @input="resetBorder" id="passwordInputId" v-model="password" :type="show_pass ? 'text' : 'password'"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                                            placeholder="******">
                                        <span class="absolute right-2 top-10 text-xs cursor-pointer"
                                            @click="show_pass = !show_pass">
                                            <EyeOff class="w-5 h-5 text-gray-500" v-if="show_pass"/>
                                            <Eye class="w-5 h-5 text-gray-500" v-else/>
                                        </span>
                                    </div>
                                    <div class="w-full border-b h-14">
                                        <button type="button"
                                            class=" w-full justify-center rounded-md bg-secondary px-3 h-12 text-h5 font-normal text-white shadow-sm"
                                            @click="register">Sign Up</button>
                                    </div>
                                    <div class="flex items-center justify-center">
                                        <span class="font-extralight text-gray-600 text-sm">Already a user?
                                            <span class="text-primary cursor-pointer" @click="store.auth='Log In'">Log In</span>
                                        </span>
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
import { ref ,watch,inject} from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import {Eye,EyeOff} from 'lucide-vue-next'

const open = ref(false)
const show_pass = ref(false)
const email = ref('')
const full_name = ref('')
const password = ref('')
const store = inject('store');
const call = inject('$call');

watch(() => store.auth, (value) => {
    if (value === 'Sign Up') {
        open.value = true;
    }else{
        open.value = false;
    }
});
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
        toast.error("Invalid email address.");
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


const openDialog = () => {
    open.value = true;
    store.auth=''
}
const resetBorder = (event) => {
    event.target.style.borderBottom = '';  
}
</script>