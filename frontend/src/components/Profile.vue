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
                                    <div class="flex justify-end">
                                        <button type="button" @click="saveUserProfile"
                                            class="text-white bg-secondary py-2 px-8 rounded-md">
                                            Save
                                        </button>
                                    </div>
                                </div>
                                <!-- other details -->
                                <div class=""
                                    v-if="otherFormData.designation && otherFormData.funderType && otherFormData.annual_budget">
                                    <div class="relative border-b py-3">
                                        <p class="py-2 text-h3 absolute left-[40%] top-0 bg-white text-secondary">Other
                                            Details</p>
                                    </div>
                                    <div class="bg-white pb-4 sm:pb-4 pt-4">
                                        <div class="flex flex-col gap-2">
                                            <label for="designation"
                                                class="text-h5 font-normal text-[#21272A]">Designation</label>
                                            <select disabled name="" id="designation"
                                                v-model="otherFormData.designation"
                                                class="outline-none border-b-2 border-gray-400 bg-gray-50 py-3 text-gray-600 px-2">
                                                <option value="">Select</option>
                                                <option value="Executive Director/Chief Executive Officer/Head of CSR">
                                                    Executive
                                                    Director/Chief Executive Officer/Head of CSR
                                                </option>
                                                <option value="Director of Philanthropy">Director of Philanthropy
                                                </option>
                                                <option value="Chief Operating Officer">Chief Operating Officer
                                                </option>
                                                <option value="Program Lead/Program Officer">Program Lead/Program
                                                    Officer
                                                </option>
                                                <option value="Third party supporting funder organisation">Third party
                                                    supporting funder organisation
                                                </option>
                                                <option value="Other">Other</option>
                                            </select>
                                        </div>
                                        <div class="pt-3">
                                            <p class=" text-h5 font-normal text-[#21272A]">
                                                Funder type organization
                                            </p>
                                            <label :for="option.id" v-for="option in options" :key="option" :class="[
                                                'w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer mt-3',
                                                otherFormData.funderType.includes(option) ? 'border-[#255B97]' : 'border-gray-300'
                                            ]">
                                                <input disabled type="checkbox" :id="option" :value="option"
                                                    v-model="otherFormData.funderType" class="cursor-pointer" />
                                                <p
                                                    :class="[otherFormData.funderType.includes(option) ? 'text-secondary' : 'text-slate-600', 'font-normal text-sm cursor-pointer']">
                                                    {{ option }}
                                                </p>
                                            </label>
                                        </div>
                                        <div class="flex flex-col gap-2 pt-3">
                                            <label for="annual_budget" class="text-h5 font-normal text-[#21272A]">
                                                Organisation’s
                                                approximate annual budget allocation</label>
                                            <select disabled name="" id="annual_budget"
                                                v-model="otherFormData.annual_budget"
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
                                        <!-- <div class="flex justify-end pt-2">
                                            <button @click="submitSelection"
                                                class="bg-secondary text-white rounded-md w-28 h-12 text-h5">Submit</button>
                                        </div> -->
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
import { ref, inject, watch, onMounted } from 'vue'
import { TransitionChild, TransitionRoot, Dialog, DialogPanel } from '@headlessui/vue'
import { X } from 'lucide-vue-next';

const isReadonly = ref(true);
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const formData = ref(auth.cookie);
const otherFormData = ref({
    designation: '',
    funderType: [],
    annual_budget: ''
})
const options = ref([])
// const uploadedImage = ref(null);
const imgUrl = ref('');
const props = defineProps({
    isOpen: {
        type: Boolean,
        required: false,
        default: false
    }
})
const get_funder_type = async () => {
    let res = await call('pwit.controllers.api.get_funder_type', {})
    options.value = res
}
const get_other = async () => {
    let res = await call('pwit.controllers.api.get_other_details', { session: store.session })
    if (res?.code == 200) {
        otherFormData.value = res.data
        otherFormData.value.funderType = res.data.funder_type.map((e) => e.funder_type)
    }
}
const user_mobile = async () => {
    let res = await call('pwit.controllers.api.user_mobile_no', {})
    if (res?.code == 200) {
        formData.value.mobile_no = res.data
    }
}

onMounted(() => {
    get_funder_type()
})
// const imageUpload = async (event) => {
//     const file = event.target.files[0];
//     if (file) {
//         const reader = new FileReader();

//         reader.onload = (e) => {
//             uploadedImage.value = e.target.result;
//         };
//         reader.readAsDataURL(file);

//         const formData1 = new FormData();
//         formData1.append("file", file);
//         formData1.append("is_private", 1);
//         formData1.append("folder", "Home");
//         formData1.append("doctype", "User");
//         formData1.append("docname", formData.value.user_id);
//         formData1.append("fieldname", "user_image");

//         try {
//             const response = await fetch('/api/method/upload_file', {
//                 method: 'POST',
//                 body: formData1,
//                 headers: {
//                 },
//             });

//             if (response.ok) {
//                 const result = await response.json();
//                 imgUrl.value = result.message.file_url
//             } else {
//                 console.error('Upload failed', response.status, response.statusText);
//             }
//         } catch (error) {
//             console.error('Error uploading file:', error);
//         }
//     }

// };
const saveUserProfile = async () => {
    let data = {
        user: formData.value.user_id,
        first_name: formData.value.full_name?.split(' ')[0],
        last_name: formData.value?.full_name?.split(' ')[1],
        mobile_no: formData.value.mobile_no,
        user_image: imgUrl.value
    }
    let res = await call('pwit.controllers.api.update_user_dt', { data: data })
    store.isOpen = false
}
watch(() => store.isOpen, async (val) => {
    if (val) {
        if (auth.isLoggedIn) {
            try {
                await call('pwit.controllers.api.check_user_details', { session: store.session })
                await user_mobile()
                await get_other()
            } catch (error) {
                console.log(error)
            }
        }
    }
}, { immediate: true, deep: true })

</script>