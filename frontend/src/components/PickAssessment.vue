<template>
    <button @click="openDialog" class="bg-secondary text-white w-96 py-3 text-sm font-semibold rounded-md">Start the Assessment</button>
    <TransitionRoot as="template" :show="open">
        <Dialog class="relative z-30" @close="open = false">
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
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class=" border-b w-full py-2">
                                    <DialogTitle as="h3" class="text-xl font-semibold text-primary font-serif">Pick an
                                        Assessment </DialogTitle>
                                </div>
                                <div class="flex flex-col gap-3 pt-4">
                                    <div class="flex flex-col gap-2">
                                        <h2 class="font-serif font-semibold text-gray-800 tracking-wider">Funder
                                            diagnostic</h2>
                                        <p class="text-xs text-gray-600">Lorem ipsum dolor sit amet consectetur
                                            adipisicing elit. veniam, reprehenderit</p>
                                        <div class="flex justify-between items-center gap-1 border-b pb-4">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <ExclamationTriangleIcon class="h-4 w-4 text-[#27853F]" />
                                                </div>
                                                <p class="text-sm font-medium">Funding practics diagnostic</p>
                                            </div>
                                            <router-link to="/funder-diagnostic"
                                                class="text-primary text-sm cursor-pointer">View</router-link>
                                        </div>
                                    </div>
                                    <div class="flex flex-col gap-2">
                                        <h2 class="font-serif font-semibold text-gray-800 tracking-wider">Assistive
                                            Guides</h2>
                                        <p class="text-xs text-gray-600">Lorem ipsum dolor sit amet consectetur
                                            adipisicing elit. veniam, reprehenderit</p>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <ExclamationTriangleIcon class="h-4 w-4 text-[#27853F]" />
                                                </div>
                                                <p class="text-sm font-medium">Develop multiyear funder-nonprofit partnerships</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <ExclamationTriangleIcon class="h-4 w-4 text-[#27853F]" />
                                                </div>
                                                <p class="text-sm font-medium">Pay a fair share of core costs</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <ExclamationTriangleIcon class="h-4 w-4 text-[#27853F]" />
                                                </div>
                                                <p class="text-sm font-medium">Invest in organizational development</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <ExclamationTriangleIcon class="h-4 w-4 text-[#27853F]" />
                                                </div>
                                                <p class="text-sm font-medium">Build financial resilience</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <ExclamationTriangleIcon class="h-4 w-4 text-[#27853F]" />
                                                </div>
                                                <p class="text-sm font-medium">Embed diversity, equity and inclusion in grantmaking</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
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
import { ref, inject, watch } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'

const open = ref(false)
const show_pass = ref(false)
const email = ref('')
const password = ref('')
const store = inject('store');

watch(() => store.auth, (value) => {
    if (value === 'Log In') {
        open.value = true;
    } else {
        open.value = false;
    }
});
const login = () => {
    if (!email.value || !password.value) {
        alert("Please enter both email and password");
        return
    } else {
        console.log("Logging in with:", email.value, password.value);
        open.value = false;
    }

};
const openDialog = () => {
    open.value = true;
    store.auth = ''
}

</script>