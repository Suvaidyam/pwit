<template>
    <button @click="auth.isLoggedIn?download_results():confirmation=true" :disabled="props.disabled"
        :class="[props.disabled ? 'cursor-not-allowed' : 'cursor-pointer']"
        class="border flex items-center justify-center gap-2 px-2 md:px-4 h-7 md:h-9 text-sm border-[#27853F] text-[#27853F] rounded-md">
        <span class="hidden lg:block truncate">Download Result </span>
        <div class="h-5 w-5" v-if="down_loading">
            <div class="animate-spin h-full w-full rounded-full border-[2px] flex justify-center items-center border-dotted border-[#002C77]">
                <div class="w-3 h-3 rounded-full border-dashed border-[1px] border-[#002C77]"></div>
            </div>
        </div>
        <Download class="w-4" v-else />
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
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4 relative">
                                <div class="flex justify-between">
                                    <h1 class="text-h3 font-primary font-bold text-primary">Provide the following
                                        information</h1>
                                    <X @click="userDetailsPop = false" class="text-sm cursor-pointer" />
                                </div>
                                <p class="text-[13px] font-normal text-[#21272A] py-1">
                                    Your responses are confidential and your information and individual responses will
                                    not be shared or made public. Any trends inferred from this data will only be made
                                    at an aggregate level (e.g., based on the type of funder).
                                </p>
                                <hr class="pb-2 mt-2">
                                <div class="flex flex-col gap-2 relative">
                                    <label for="designation" class="text-h5 font-normal text-[#21272A]">
                                        Please share your designation
                                        <span class="text-red-500">*</span>
                                    </label>
                                    <select id="designation" v-model="formData.designation"
                                        class="outline-none border-b-2 bg-gray-50 py-3 text-black px-2"
                                        :class="[!errors.designation ? 'border-gray-400' : 'border-red-500']">
                                        <option value="">Select</option>
                                        <option value="Executive Director/Chief Executive Officer/Head of CSR">Executive
                                            Director/Chief Executive Officer/Head of CSR</option>
                                        <option value="Director of Philanthropy">Director of Philanthropy</option>
                                        <option value="Chief Operating Officer">Chief Operating Officer</option>
                                        <option value="Programme Lead/Programme Officer">Programme Lead/Programme
                                            Officer
                                        </option>
                                        <option value="Third party supporting funder organisation">Third-party
                                            supporting funder organisation</option>
                                        <option value="Other">Other</option>
                                    </select>
                                    <p v-if="errors.designation" class="absolute -bottom-5 text-red-500 text-h6 mt-1">{{
                                        errors.designation
                                    }}</p>
                                </div>

                                <div class="pt-5 relative">
                                    <p class="text-h5 font-normal text-[#21272A]">
                                        Please select which funder type your organisation identifies as
                                        <span class="text-red-500">*</span>
                                    </p>
                                    <label
                                        class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                                        <input type="radio" id="option" value="Corporate Social Responsibility (CSR)"
                                            v-model="formData.funder_type" class="cursor-pointer" />
                                        <p class="text-secondary font-normal text-sm cursor-pointer">
                                            Corporate Social Responsibility (CSR)
                                        </p>
                                    </label>
                                    <label
                                        class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                                        <input type="radio" id="option" value="Domestic Foundation"
                                            v-model="formData.funder_type" class="cursor-pointer" />
                                        <p class="text-secondary font-normal text-sm cursor-pointer">
                                            Domestic Foundation
                                        </p>
                                    </label>
                                    <label
                                        class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                                        <input type="radio" id="option" value="Global Foundation"
                                            v-model="formData.funder_type" class="cursor-pointer" />
                                        <p class="text-secondary font-normal text-sm cursor-pointer">
                                            Global Foundation
                                        </p>
                                    </label>
                                    <p v-if="errors.funder_type" class="absolute -bottom-5 text-red-500 text-h6 mt-1">{{
                                        errors.funder_type
                                    }}</p>
                                </div>

                                <div class="flex flex-col gap-2 pt-5 relative">
                                    <label for="annual_budget" class="text-h5 font-normal text-[#21272A]">
                                        Your organisation’s approximate annual budget allocation
                                        <span class="text-red-500">*</span>
                                    </label>
                                    <select id="annual_budget" v-model="formData.annual_budget"
                                        class="outline-none border-b-2 bg-gray-50 py-3 text-gray-900 px-2"
                                        :class="[!errors.annual_budget ? 'border-gray-400' : 'border-red-500']">
                                        <option value="">Select</option>
                                        <option value="Less than INR 10 Cr.">Less than INR 10 Cr.</option>
                                        <option value="INR 10-50 Cr.">INR 10-50 Cr.</option>
                                        <option value="INR 51-100 Cr.">INR 51-100 Cr.</option>
                                        <option value="INR 101-300 Cr.">INR 101-300 Cr.</option>
                                        <option value="INR 301 Cr. and above">INR 301 Cr. and above</option>
                                    </select>
                                    <p v-if="errors.annual_budget" class="absolute -bottom-5 text-red-500 text-h6 mt-1">
                                        {{
                                            errors.annual_budget }}</p>
                                </div>

                                <div class="flex justify-end pt-2">
                                    <button @click="submitSelection"
                                        class="bg-secondary text-white rounded-md w-28 h-12 text-h5">
                                        Submit
                                    </button>
                                </div>

                            </div>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
    <!--  -->
    <TransitionRoot as="template" :show="confirmation">
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
                            <div class="p-4">
                                <div class="flex justify-between">
                                    <h1 class="text-h3 font-primary font-bold text-primary">Download as Guest</h1>
                                    <X @click="confirmation = false" class="text-sm cursor-pointer" />
                                </div>
                                <p class="text-sm font-normal text-[#21272A] py-1">
                                    You can download the result now. However, creating an account lets you save results
                                    and access them anytime.
                                </p>
                                <hr class="pb-2 mt-2">
                                <div class="flex justify-end gap-2 pt-2">
                                    <button @click="confirmationDn('guest')"
                                        class="bg-secondary text-white rounded-md w-28 h-10 text-h5">Guest</button>
                                    <button @click="confirmationDn('login')"
                                        class="bg-secondary text-white rounded-md w-36 h-10 text-h5">Login /
                                        Register</button>
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
import { X } from 'lucide-vue-next'

const auth = inject('$auth')
const call = inject('$call')
const store = inject('store')
const userDetailsPop = ref(false)
const confirmation = ref(false)
const down_loading = ref(false);
const formData = ref({
    designation: '',
    funder_type: '',
    annual_budget: ''
})
const errors = ref({
    designation: '',
    funder_type: '',
    annual_budget: ''
});
// Props
const props = defineProps({
    disabled: {
        type: Boolean,
        default: false
    }, 
})


const validateForm = () => {
    errors.value.designation = formData.value.designation ? '' : 'Designation is required.';
    errors.value.funder_type = formData.value.funder_type.length ? '' : 'Please select at least one funder type.';
    errors.value.annual_budget = formData.value.annual_budget ? '' : 'Annual budget is required.';
    return !errors.value.designation && !errors.value.funder_type && !errors.value.annual_budget;
};
// Submit selected options
const submitSelection = async () => {
    if (!validateForm()) {
        return;
    }
    let res = await call('pwit.controllers.api.save_user_details', { data: formData.value, session: store.session })
    if (res.code == 200) {
        userDetailsPop.value = false
        await download_results()
    }
}

const download_results = async () => {

    let value = await check_user_details()
    if (value) {
        down_loading.value = true
        let link = document.createElement('a')
        link.href = `/api/method/pwit.controllers.funder_results.download_funder?session=${store.session}`;
        link.click()
        sessionStorage.removeItem('authPopup');
        setTimeout(() => {
            down_loading.value = false
        }, 500)
    }
}
const check_user_details = async () => {
    const response = await call('pwit.controllers.api.check_user_details', { session: store.session })
    if (response.code == 400) {
        if (auth.isLoggedIn) {
            userDetailsPop.value = true
        }
        return false
    } else {
        formData.value = response.data
        return true
    }
}
const confirmationDn = async(value) => {
    confirmation.value = false
    if (value == 'guest') {
        await check_user_details()
        userDetailsPop.value = true
    } else {
        store.authPopup = true;
        sessionStorage.setItem('authPopup', true);
    }
}
onMounted(() => {
    if (auth.isLoggedIn && sessionStorage.getItem('authPopup') == 'true') {
        download_results()
    }
})
</script>

<style scoped>
/* Add any custom styles if necessary */
</style>
