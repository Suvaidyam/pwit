<template>
    <button @click="open = true">Register</button>
    <TransitionRoot as="template" :show="open">
        <Dialog class="relative z-10" @close="open = false">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class="mt-3 text-center">
                                    <DialogTitle as="h3" class="text-xl font-semibold text-gray-900 text-center">Sign Up
                                    </DialogTitle>
                                    <p class="text-sm pt-2 text-center text-gray-500">Please provide the following
                                        information to continue </p>
                                </div>
                                <div class="flex flex-col gap-3 pt-4">
                                    <div class="flex flex-col gap-2 w-full">
                                        <label for="full_name" class="text-sm text-tatary">Full Name</label>
                                        <input v-model="full_name" type="text" id="full_name"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 py-2 placeholder:text-sm"
                                            placeholder="Enter Full Name">
                                    </div>
                                    <div class="flex flex-col gap-2 w-full">
                                        <label for="" class="text-sm text-tatary">Email Address</label>
                                        <input v-model="email" type="email"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 py-2 placeholder:text-sm"
                                            placeholder="Enter Email Address">
                                    </div>
                                    <div class="flex flex-col gap-2 w-full relative">
                                        <label for="" class="text-sm text-tatary">Password</label>
                                        <input v-model="password" :type="show_pass ? 'text' : 'password'"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 py-2 placeholder:text-sm"
                                            placeholder="******">
                                        <span class="absolute right-2 top-10 text-xs cursor-pointer"
                                            @click="show_pass = !show_pass">{{ show_pass ? 'hide' : 'show' }} </span>
                                    </div>
                                    <div class="w-full border-b h-14">
                                        <button type="button"
                                            class=" w-full justify-center rounded-md bg-secondary px-3 py-2.5 text-sm font-semibold text-white shadow-sm"
                                            @click="login">Sign Up</button>
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
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'

const open = ref(false)
const show_pass = ref(false)
const email = ref('')
const full_name = ref('')
const password = ref('')
const store = inject('store');


watch(() => store.auth, (value) => {
    if (value === 'Sign Up') {
        open.value = true;
    }else{
        open.value = false;
    }
});

const login = () => {
    if (!email.value || !password.value) {
        alert("Please enter both email and password");
        return
    } else {
        console.log("Register in with:", email.value, password.value);
        open.value = false;
    }

};

</script>