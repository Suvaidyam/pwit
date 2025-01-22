<template>
    <TransitionRoot as="template" :show="store.isOpen">
        <Dialog class="relative z-30" @close="store.isOpen = false">
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
                            class="relative transform overflow-hidden md:px-4 bg-white text-left shadow-xl transition-all sm:my-8 w-full sm:max-w-2xl">
                            <div class="bg-white px-4 w-full pb-4 pt-5 sm:p-6 sm:pb-4 relative">
                                <X @click="store.isOpen = false" class="text-sm  cursor-pointer absolute right-5" />
                                <div class="block justify-center gap-5 items-center">
                                    <h1 class="text-center font-primary font-bold text-h3 text-[#21272A]">My Profile
                                    </h1>

                                    <p class="text-center text-[#21272A] font-normal text-h5 pt-2"> Set up or update
                                        your profile</p>
                                </div>

                                <div class="space-y-4 container pt-2">
                                    <div>
                                        <label for="full_name" class="block text-gray-800 text-sm pb-2">
                                            Full Name
                                        </label>
                                        <input v-model="formData.full_name" id="full_name" type="text"
                                            placeholder="Enter Full Name"
                                            class="w-full px-3 py-2 border-b  bg-[#f3f4f8] shadow-sm outline-none">
                                    </div>
                                    <div>
                                        <label for="mobile_no" class="block text-gray-800 text-sm pb-2">
                                            Mobile No.
                                        </label>
                                        <input v-model="formData.mobile_no" id="mobile_no" type="text"
                                            placeholder="Enter your Mobile No. "
                                            class="w-full px-3 py-2 border-b  bg-[#f3f4f8]  shadow-sm outline-none">
                                    </div>
                                    <div>
                                        <label for="email" class="block text-gray-800 text-sm pb-2">
                                            Email Address
                                        </label>
                                        <input v-model="formData.user_id" id="email" type="email"
                                            placeholder="Enter Email Address"
                                            class="w-full px-3 border-b bg-[#f3f4f8] cursor-not-allowed text-gray-500 border-gray-300   shadow-sm py-2 outline-none"
                                            :disabled="true">
                                    </div>

                                    <!-- other details -->
                                    <div class="">
                                        <div class="relative border-b py-3">
                                            <p
                                                class=" absolute left-[27%] sm:left-[40%] top-1 bg-white text-center font-primary font-bold text-h3 text-[#21272A]">
                                                Other Details</p>
                                        </div>
                                        <div class="bg-white pb-4 sm:pb-4 pt-4 flex flex-col gap-2">
                                            <div class="flex flex-col gap-2 relative">
                                                <label for="designation"
                                                    class="text-sm font-normal text-[#21272A]">Designation <span class="text-red-500">*</span></label>
                                                <select name="" id="designation" v-model="otherFormData.designation"
                                                    class="outline-none border-b-2 border-gray-400 bg-gray-50 py-3 text-gray-600 px-2">
                                                    <option value="">Select</option>
                                                    <option
                                                        value="Executive Director/Chief Executive Officer/Head of CSR">
                                                        Executive Director/Chief Executive Officer/Head of CSR
                                                    </option>
                                                    <option value="Director of Philanthropy">Director of Philanthropy
                                                    </option>
                                                    <option value="Chief Operating Officer">Chief Operating Officer
                                                    </option>
                                                    <option value="Programme Lead/Programme Officer">Programme
                                                        Lead/Programme
                                                        Officer
                                                    </option>
                                                    <option value="Third party supporting funder organisation">Third
                                                        party
                                                        supporting funder organisation
                                                    </option>
                                                    <option value="Other">Other</option>
                                                </select>
                                                <p v-if="errors.designation"
                                                    class="absolute -bottom-5 text-red-500 text-h6 mt-1">
                                                    {{
                                                        errors.designation }}</p>
                                            </div>
                                            <div class="pt-3 relative">
                                                <p class=" text-sm font-normal text-[#21272A]">
                                                    Funder type organisation <span class="text-red-500">*</span>
                                                </p>
                                                <label
                                                    class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                                                    <input type="radio" id="option"
                                                        value="Corporate Social Responsibility (CSR)"
                                                        v-model="otherFormData.funder_type" class="cursor-pointer" />
                                                    <p class="text-secondary font-normal text-sm cursor-pointer">
                                                        Corporate Social Responsibility (CSR)
                                                    </p>
                                                </label>
                                                <label
                                                    class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                                                    <input type="radio" id="option" value="Domestic Foundation"
                                                        v-model="otherFormData.funder_type" class="cursor-pointer" />
                                                    <p class="text-secondary font-normal text-sm cursor-pointer">
                                                        Domestic Foundation
                                                    </p>
                                                </label>
                                                <label
                                                    class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3 border-[#255B97]">
                                                    <input type="radio" id="option" value="Global Foundation"
                                                        v-model="otherFormData.funder_type" class="cursor-pointer" />
                                                    <p class="text-secondary font-normal text-sm cursor-pointer">
                                                        Global Foundation
                                                    </p>
                                                </label>
                                                <p v-if="errors.funder_type"
                                                    class="absolute -bottom-5 text-red-500 text-h6 mt-1">
                                                    {{
                                                        errors.funder_type }}</p>
                                            </div>
                                            <div class="flex flex-col gap-2 pt-3 relative">
                                                <label for="annual_budget" class="text-sm font-normal text-[#21272A]">
                                                    Organisation’s
                                                    approximate annual budget allocation <span class="text-red-500">*</span></label>
                                                <select name="" id="annual_budget" v-model="otherFormData.annual_budget"
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
                                                    <option value="INR 301 Cr. and above">INR 301 Cr. and above
                                                    </option>
                                                </select>
                                                <p v-if="errors.annual_budget"
                                                    class="absolute -bottom-5 text-red-500 text-h6 mt-1">
                                                    {{
                                                        errors.annual_budget }}</p>
                                            </div>
                                            <!-- <div class="flex justify-end pt-2">
                                                <button @click="submitSelection"
                                                    class="bg-secondary text-white rounded-md w-28 h-12 text-h5">Submit</button>
                                            </div> -->
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-end pt-3">
                                    <button type="button" @click="saveUserProfile"
                                        class="text-white bg-secondary py-2 px-8 rounded-md">
                                        Save
                                    </button>
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
import { ref, inject, watch, onMounted } from 'vue'
import { TransitionChild, TransitionRoot, Dialog, DialogPanel } from '@headlessui/vue'
import { X } from 'lucide-vue-next';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import router from '../router';

const isReadonly = ref(true);
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const formData = ref(auth.cookie);
const otherFormData = ref({
    designation: '',
    funder_type: '',
    annual_budget: ''
})
const errors = ref({
    designation: '',
    funder_type: '',
    annual_budget: ''
});
// const uploadedImage = ref(null);
const imgUrl = ref('');
const props = defineProps({
    isOpen: {
        type: Boolean,
        required: false,
        default: false
    }
})

const get_other = async () => {
    let res = await call('pwit.controllers.api.get_other_details', { session: store.session })
    if (res?.code == 200) {
        otherFormData.value = res.data
    }
}
const user_mobile = async () => {
    let res = await call('pwit.controllers.api.user_mobile_no', {})
    if (res?.code == 200) {
        formData.value.mobile_no = res.data
    }
}

const saveUserProfile = async () => {
    let data = {
        user: formData.value.user_id,
        first_name: formData.value.full_name?.split(' ')[0],
        last_name: formData.value?.full_name?.split(' ')[1],
        mobile_no: formData.value.mobile_no,
        user_image: imgUrl.value
    }
    if (!validateForm()) {
        return;
    }
    let res = await call('pwit.controllers.api.update_user_dt', { data: data })
    if (res?.code == 200) {
        await submitSelection()
        store.isOpen = false
        toast.success(res.message)
    }
}
const validateForm = () => {
    errors.value.designation = otherFormData.value.designation ? '' : 'Designation is required.';
    errors.value.funder_type = otherFormData.value.funder_type ? '' : 'Funder type. is required.';
    errors.value.annual_budget = otherFormData.value.annual_budget ? '' : 'Annual budget is required.';
    return !errors.value.designation && !errors.value.funder_type && !errors.value.annual_budget;
};
const submitSelection = async () => {
    if (!validateForm()) {
        return;
    }
    try {
        let res = await call('pwit.controllers.api.save_user_details', { data: otherFormData.value, session: store.session })
        if (res?.code == 200 && store.checkLogin) {
            router.push('/')
        }
    } catch (error) {

    }
}

watch(() => store.isOpen, async (val) => {
    if (val) {
        if (auth.isLoggedIn) {
            await user_mobile()
            await get_other()
        }
    }
}, { immediate: true, deep: true })

</script>