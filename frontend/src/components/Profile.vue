<template>
    <TransitionRoot as="template" :show="store.isOpen">
        <Dialog class="relative z-20" @close="store.isOpen = false">
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
                                    <h1 class="text-center font-serif font-bold text-h3 text-[#21272A]">My Profile</h1>
                                    <p class="text-center text-[#21272A] font-normal text-h5 pt-2"> Set up or update
                                        your profile</p>
                                </div>
                                <div class=" flex justify-center items-center pt-4 relative">
                                    <div>
                                        <div
                                            class="w-24 h-24 rounded-full bg-slate-300 flex items-center justify-center relative">
                                            <img v-if="formData.user_image" :src="formData.user_image" alt="User Image"
                                                class="w-full h-full rounded-full object-cover" />
                                            <p class="text-h2" v-else>{{ formData.full_name?.[0]?.toUpperCase() }}</p>

                                            <div v-if="!isReadonly"
                                                class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50 rounded-full">
                                                <label for="upload"
                                                    class="cursor-pointer text-white text-sm">Upload</label>
                                                <input id="upload" type="file" class="hidden" @change="imageUpload"
                                                    accept="image/*" />
                                            </div>
                                        </div>
                                        <div class="flex items-end justify-end absolute top-16 pl-[4.5rem]">
                                            <button @click="Editable" class="p-2 rounded-full bg-secondary">
                                                <svg width="14" height="13" viewBox="0 0 14 13" fill="none"
                                                    xmlns="http://www.w3.org/2000/svg">
                                                    <path
                                                        d="M0.5 12.75V10.2116L10.3929 0.323062C10.5063 0.220062 10.6314 0.1405 10.7684 0.084375C10.9056 0.028125 11.0493 0 11.1997 0C11.3501 0 11.4957 0.0266879 11.6366 0.0800629C11.7776 0.133438 11.9024 0.218312 12.011 0.334687L12.9269 1.26206C13.0433 1.37069 13.1263 1.49569 13.1758 1.63706C13.2253 1.77844 13.25 1.91981 13.25 2.06119C13.25 2.21206 13.2243 2.356 13.1728 2.493C13.1213 2.63013 13.0393 2.75538 12.9269 2.86875L3.03838 12.75H0.5ZM11.039 3.14569L12.125 2.06681L11.1832 1.125L10.1043 2.211L11.039 3.14569Z"
                                                        fill="white" />
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                <div class="space-y-4 container">
                                    <div>
                                        <label for="full_name" class="block text-gray-800 text-sm pb-2">
                                            Full Name
                                        </label>
                                        <input v-model="formData.full_name" id="full_name" type="text"
                                            placeholder="Enter Full Name"
                                            class="w-full px-3 py-2 border-b  bg-[#f3f4f8] border-gray-300 shadow-sm outline-none"
                                            :readonly="isReadonly">
                                    </div>
                                    <div>
                                        <label for="mobile_no" class="block text-gray-800 text-sm pb-2">
                                            Mobile No.
                                        </label>
                                        <input ref="formData.mobile_no" id="mobile_no" type="text"
                                            placeholder="Enter your Mobile No. "
                                            class="w-full px-3 py-2 border-b  bg-[#f3f4f8] border-gray-300 shadow-sm outline-none"
                                            :readonly="isReadonly">
                                    </div>
                                    <div>
                                        <label for="email" class="block text-gray-800 text-sm pb-2">
                                            Email Address
                                        </label>
                                        <input v-model="formData.user_id" id="email" type="email"
                                            placeholder="Enter Email Address"
                                            class="w-full px-3 border-b bg-[#f3f4f8] border-gray-300   shadow-sm py-2 outline-none"
                                            :disabled="true">
                                    </div>
                                    <div class="flex justify-end">
                                        <button type="button" @click="saveUserProfile"
                                            class="text-white bg-secondary py-2 px-8 rounded-md">
                                            Save
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
import { ref, inject } from 'vue'
import { TransitionChild, TransitionRoot, Dialog, DialogPanel } from '@headlessui/vue'

const mobile_no = ref('')
const isReadonly = ref(true);
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const formData = ref(auth.cookie);
const uploadedImage = ref(null);
const imgUrl = ref('');
const props = defineProps({
    isOpen: {
        type: Boolean,
        required: false,
        default: false
    }
})
const Editable = () => {
    isReadonly.value = !isReadonly.value;
};

const imageUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = (e) => {
            uploadedImage.value = e.target.result;
        };
        reader.readAsDataURL(file);

        const formData1 = new FormData();
        formData1.append("file", file);
        formData1.append("is_private", 1);
        formData1.append("folder", "Home");
        formData1.append("doctype", "User");
        formData1.append("docname", formData.value.user_id);
        formData1.append("fieldname", "user_image");

        try {
            const response = await fetch('/api/method/upload_file', {
                method: 'POST',
                body: formData1,
                headers: {
                },
            });

            if (response.ok) {
                const result = await response.json();
                imgUrl.value = result.message.file_url
            } else {
                console.error('Upload failed', response.status, response.statusText);
            }
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    }

};
const saveUserProfile = async () => {
    let data = {
        user: formData.value.user_id,
        first_name: formData.value.full_name?.split(' ')[0],
        last_name: formData.value?.full_name?.split(' ')[1],
        mobile_no: formData.value.mobile_no,
        user_image: imgUrl.value
    }
    await call('pwit.controllers.api.save_image', { data: data })
}


</script>