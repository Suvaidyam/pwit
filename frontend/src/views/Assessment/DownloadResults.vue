<template>
    <button @click="download_results" :disabled="props.disabled"
        :class="[props.disabled ? 'cursor-not-allowed' : 'cursor-pointer']"
        class="border flex items-center justify-center gap-2 px-2 md:px-4 h-7 md:h-9 text-sm border-[#27853F] text-[#27853F] rounded-md">
        <span class="hidden lg:block truncate">Download Result </span>
        <Download class="w-4" />
    </button>
    <TransitionRoot as="template" :show="userDetailsPop">
        <Dialog class="relative z-30">
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
                            class="relative transform overflow-hidden bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class="flex justify-between">
                                    <h1 class="text-h3 font-serif font-bold text-primary">Provide the following
                                        information</h1>
                                    <X @click="userDetailsPop = false" class="text-sm cursor-pointer" />
                                </div>
                                <p class="text-sm font-normal text-[#21272A] py-1">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                                    eiusmod tempor incididunt ut labore et dolore magna aliqua.
                                </p>
                                <hr class="pb-2 mt-2">
                                <div class="flex flex-col gap-2">
                                    <label for="designation" class="text-h5 font-normal text-[#21272A]">Please share
                                        your
                                        designation</label>
                                    <select name="" id="designation" v-model="formData.designation"
                                        class="outline-none border-b-2 border-gray-400 bg-gray-50 py-3 text-gray-600 px-2">
                                        <option value="">Select</option>
                                        <option value="Executive Director/Chief Executive Officer/Head of CSR">Executive
                                            Director/Chief Executive Officer/Head of CSR
                                        </option>
                                        <option value="Director of Philanthropy">Director of Philanthropy
                                        </option>
                                        <option value="Chief Operating Officer">Chief Operating Officer
                                        </option>
                                        <option value="Program Lead/Program Officer">Program Lead/Program Officer
                                        </option>
                                        <option value="Third party supporting funder organisation">Third party
                                            supporting funder organisation
                                        </option>
                                        <option value="Other">Other</option>
                                    </select>
                                </div>
                                <div class="pt-3">
                                    <p class=" text-h5 font-normal text-[#21272A]">
                                        Please select which funder type your organization identifies as
                                    </p>
                                    <label :for="option.id" v-for="option in options" :key="option" :class="[
                                        'w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3',
                                        formData.funderType.includes(option) ? 'border-[#255B97]' : 'border-gray-300'
                                    ]">
                                        <input type="checkbox" :id="option" :value="option"
                                            v-model="formData.funderType" class="cursor-pointer" />
                                        <p
                                            :class="[formData.funderType.includes(option) ? 'text-secondary' : 'text-slate-600', 'font-normal text-sm cursor-pointer']">
                                            {{ option }}
                                        </p>
                                    </label>
                                </div>
                                <div class="flex flex-col gap-2 pt-3">
                                    <label for="annual_budget" class="text-h5 font-normal text-[#21272A]">Your
                                        organisation’s
                                        approximate annual budget allocation</label>
                                    <select name="" id="annual_budget" v-model="formData.annual_budget"
                                        class="outline-none border-b-2 border-gray-400 bg-gray-50 py-3 text-gray-600 px-2">
                                        <option value="">Select</option>
                                        <option value="Less than INR 10 Cr.">Less than INR 10 Cr.
                                        </option>
                                        <option value="INR 10-50 Cr.">INR 10-50 Cr.
                                        </option>
                                        <option value="INR 51-100 Cr.">INR 51-100 Cr.
                                        </option>
                                        <option value="INR 101-300 Cr.">INR 101-300 Cr.
                                        </option>
                                        <option value="INR 301 and above">INR 301 and above
                                        </option>
                                    </select>
                                </div>
                                <div class="flex justify-end pt-2">
                                    <button @click="submitSelection"
                                        class="bg-secondary text-white rounded-md w-28 h-12 text-h5">Submit</button>
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
import { inject, onMounted, ref } from 'vue'
import { Download } from 'lucide-vue-next'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import {  X } from 'lucide-vue-next'

const call = inject('$call')
const store = inject('store')
const userDetailsPop = ref(false)
const formData = ref({
    designation: '',
    funderType: [],
    annual_budget: ''
})
const options = ref([])
// Props
const props = defineProps({
    disabled: {
        type: Boolean,
        default: false
    },
    ref_doctype: {
        type: String,
        mandatory: true
    }
})
const get_funder_type = async () => {
    let res = await call('pwit.controllers.api.get_funder_type', {})
    options.value = res
}

// Submit selected options
const submitSelection = async () => {
    let res = await call('pwit.controllers.api.save_user_details', { data: formData.value, session: store.session })
    if (res.code == 200) {
        userDetailsPop.value = false
        await download_results()
    }
}
const download_results = async () => {
    let value = await check_user_details()
    if (value) {
        let res = await call('pwit.controllers.api.download_results', { ref_doctype: props.ref_doctype })
        console.log(res)
    }
}
const check_user_details = async () => {
    const response = await call('pwit.controllers.api.check_user_details', { session: store.session })
    if (response.code == 400) {
        userDetailsPop.value = true
        return false
    }else{
        return true
    }
}
onMounted(() => {
    get_funder_type()
})
</script>

<style scoped>
/* Add any custom styles if necessary */
</style>
