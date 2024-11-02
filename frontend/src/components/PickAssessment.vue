<template>
    <button @click="openDialog"
        class="bg-secondary text-white w-full md:w-1/3 py-4 text-sm font-semibold rounded-md">Start the
        Assessment</button>
    <!--  -->
    <TransitionRoot as="template" :show="open">
        <Dialog class="relative z-30" @close="open = false">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class="flex px-4 md:px-6 flex-col gap-2 items-center justify-center">
                                    <div class="w-12 h-12 bg-green-500 rounded-full flex justify-center items-center">
                                        <ExclamationTriangleIcon class="h-8 w-8 text-white" />
                                    </div>
                                    <h2 class="text-2xl font-serif tracking-wider text-primary font-semibold">Data Security
                                        Policy/Consent</h2>
                                    <p class="text-sm text-center">Please indicate that you consent to your information
                                        being stored, processed and analyzed for the purpose of strengthening this
                                        tool’s offerings.</p>
                                    <div class="flex gap-2 items-center">
                                        <input type="checkbox" v-model="condision" name="" id="tc">
                                        <label class="text-sm" for="tc">I understand and agree to the above.</label>
                                    </div>
                                    <button :disabled="!condision" @click="assessment" :class="condision?'bg-secondary':'bg-gray-700'" class="px-16 py-3 mt-5 rounded-md text-white">Continue </button>
                                </div>
                            </div>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
    <!--  -->
    <TransitionRoot as="template" :show="open_ass">
        <Dialog class="relative z-30" @close="open_ass = false">
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
                                                <p class="text-sm font-medium">Develop multiyear funder-nonprofit
                                                    partnerships</p>
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
                                                <p class="text-sm font-medium">Embed diversity, equity and inclusion in
                                                    grantmaking</p>
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
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { ExclamationTriangleIcon } from '@heroicons/vue/24/outline'

const open = ref(false)
const open_ass = ref(false)
const condision = ref(false)


const openDialog = () => {
    open.value = true;
}
const assessment = () => {
    open.value = false;
    open_ass.value = true;
}

</script>