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
                                <div class="space-y-6 container">
                                    <div>
                                        <label for="new_password" class="block text-gray-800 text-sm pb-2">
                                            New Password
                                        </label>
                                        <input v-model="new_password" id="new_password" type="password" placeholder="Enter New Password"
                                            class="w-full px-3 py-2 border-b  bg-[#f3f4f8] border-gray-300 shadow-sm outline-none ">
                                    </div>
                                    <div>
                                        <label for="Confirm_pass" class="block text-gray-800 text-sm pb-2">
                                            Confirm Password
                                        </label>
                                        <input v-model="Confirm_pass" id="Confirm_pass" type="password" placeholder="Enter New Password"
                                            class="w-full px-3 py-2 border-b  bg-[#f3f4f8] border-gray-300 shadow-sm outline-none ">
                                    </div>
                                 
                                    <div class="flex justify-end">
                                        <button class="text-white bg-secondary py-2 px-8 rounded-md">
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

const store = inject('store');

const new_password = ref('')
const props = defineProps({
    isOpen: {
        type: Boolean,
        required: false,
        default: false
    }
})

</script>