<template>
    <button @click="openDialog" class="w-[74px] h-10 text-h5 rounded-md bg-secondary text-white">Login</button>
    <TransitionRoot as="template" :show="open">
        <Dialog class="relative z-20" @close="open = false">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full justify-center p-4 text-center items-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class="sm:flex sm:items-start">
                                    <div class="mt-3 text-center sm:mt-0 sm:text-left">
                                        <DialogTitle as="h3" class="text-h3 font-bold text-[#21272A]">Login to
                                            PAY-WHAT-IT-TAKES INDIA INITIATIVE </DialogTitle>
                                        <p class="text-h5 pt-2 text-center text-trbase font-normal">Please provide the following
                                            information to continue </p>
                                    </div>
                                </div>
                                <div class="flex flex-col gap-3 pt-4">
                                    <div class="flex flex-col gap-2 w-full">
                                        <label for="" class="text-sm text-tatary">Email Address</label>
                                        <input v-model="email" type="email"
                                            class="outline-none w-full border-b-2 bg-gray-50 px-3 h-12 text-h5"
                                            placeholder="Enter Email Address">
                                    </div>
                                    <div class="flex flex-col gap-2 w-full relative">
                                        <label for="" class="text-sm text-tatary">Password</label>
                                        <input v-model="password" :type="show_pass ? 'text' : 'password'"
                                            class="outline-none w-full border-b-2 bg-gray-50 text-sm px-3 h-12 text-h5"
                                            placeholder="******">
                                        <span class="absolute right-2 top-10 font-semibold text-gray-500 text-xs cursor-pointer"
                                            @click="show_pass = !show_pass">
                                        <EyeOff class="w-5 h-5 text-gray-500" v-if="show_pass"/>
                                        <Eye class="w-5 h-5 text-gray-500" v-else/>
                                        </span>
                                    </div>
                                    <div class="w-full border-b h-14">
                                        <button type="button"
                                            class=" w-full justify-center rounded-md bg-secondary px-3 h-12 text-h5 font-normal text-white shadow-sm"
                                            @click="login">Log In</button>
                                    </div>
                                    <div class="flex items-center justify-center">
                                        <span class="font-extralight text-gray-600 text-sm">No account yet?
                                            <span class="text-primary cursor-pointer" @click="store.auth = 'Sign Up'">Sign
                                                Up</span>
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
import { ref, inject, watch ,onMounted} from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import {Eye,EyeOff} from 'lucide-vue-next'

const open = ref(false)
const show_pass = ref(false)
const email = ref('')
const password = ref('')
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const cur_session = ref(JSON.parse(localStorage.getItem('session'))?.data?.name)

watch(() => cur_session.value, (value) => {
    cur_session.value = value
});
console.log(cur_session.value)
watch(() => store.auth, (value) => {
    if (value === 'Log In') {
        open.value = true;
    } else {
        open.value = false;
    }
});
const login = async () => {
    if (!email.value || !password.value) {
        alert("Please enter both email and password");
        return
    } else {
        open.value = false;
        let res = await auth.login(email.value, password.value);
        if (res && cur_session.value) {
            const response = await call('pwit.controllers.api.set_user_session', {name:cur_session.value, user:email.value})
            if(response){
                toast.success('Login Successful');
                setTimeout(() => {
                    window.location.reload()
                }, 500);
            }
        }
    }

};
const openDialog = () => {
    open.value = true;
    store.auth = ''
}

</script>