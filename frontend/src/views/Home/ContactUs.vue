<template>
    <div class="absolute bg-white shadow-lg py-6 -top-24 w-full lg:w-[65%] px-4 md:px-8 lg:px-20 ">
        <h2 class="text-h2 font-bold font-serif text-center text-primary mb-6">Contact Us</h2>
        <div class="space-y-6">
            <div>
                <label class="block text-gray-800 text-sm mb-2">
                    Full Name
                    <span class="text-red-500"> *</span>
                </label>
                <input @keydown.enter="sendMessage" @input="resetBorder" id="inputId1" v-model="data.full_name" type="text" placeholder="Enter Full Name"
                    class="w-full px-3 py-2 border-b  bg-[#f3f4f8] border-gray-300 shadow-sm outline-none ">
            </div>
            <div>
                <label class="block text-gray-800 text-sm mb-2">
                    Email Address
                    <span class="text-red-500">
                        *
                    </span>
                </label>
                <input @keydown.enter="sendMessage" @input="resetBorder" id="inputId2"  v-model="data.email" type="email" placeholder="Enter Email Address"
                    class="w-full px-3 border-b bg-[#f3f4f8] border-gray-300   shadow-sm py-2 outline-none">
            </div>
            <div>
                <label class="block text-gray-800 text-sm mb-2">Your Message <span class="text-red-500"> *</span></label>
                <textarea v-model="data.message" placeholder="Start writing from here"
                    class="w-full px-3 border-b bg-[#f3f4f8] border-gray-300   shadow-sm h-24 resize-none py-2  outline-none"></textarea>
            </div>
            <div class="flex justify-center">
                <button type="button" @click="sendMessage"
                    class="w-[169px] h-12 rounded-md bg-secondary  text-white text-h5 text-center  shadow-md">
                    Send Message
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, inject} from 'vue';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const data = ref({
    full_name: '',
    email: '',
    message: ''
});
    
function validateEmail(email) {
    const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    return emailRegex.test(email);
}
const call = inject('$call');
const sendMessage = async () => {
    let session = JSON.parse(localStorage.getItem('session'));

    const fullName = document.getElementById('inputId1');
    const email = document.getElementById('inputId2');
        let valid = true;
        fullName.style.borderBottom = '';
        email.style.borderBottom = '';

        if (!fullName.value || !email.value || !data.value.message) {
            if (!fullName.value) {
                fullName.style.borderBottom = '1px solid red';  
                valid = false;
            }

            if (!email.value) {
                email.style.borderBottom = '1px solid red'; 
                valid = false;
            }

            if (!data.value.message) {
                toast.error('Please fill all the fields');
                valid = false;
            }
            return; 
        }

        if (!validateEmail(email.value)) {
            email.style.borderBottom = '1px solid red'; 
            toast.error("Invalid email address.");
            valid = false;
            return;  
        }
    
    if (data.value.full_name && data.value.email) {
        try {
            let res = await call('pwit.controllers.api.contact_us', { 
                data: { 
                    ...data.value, 
                    session: session?.data?.name 
                } 
            });

            if (res.code === 200) {
                toast.success('Successfully submitted');
                data.value = {
                    full_name: '',
                    email: '',
                    message: ''
                };
            } else if (res.code === 400) {
                toast.error(res.msg);
            } else {
                toast.error('Something went wrong');
            }
        } catch (error) {
            toast.error('Request failed');
            validateEmail();
            const email = document.getElementById('inputId2').value;
            if (validateEmail(email)) {
                alert("Valid email address.");
            } else {
                toast.error("Invalid email address.");
            }
        }
    } else {
        // toast.error('Please fill all the fields');
    }
};
const resetBorder = (event) => {
    event.target.style.borderBottom = '';  
}
 
</script>
