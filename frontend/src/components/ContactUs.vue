<template>
    <div class="absolute bg-white shadow-lg py-6 -top-24 w-full lg:w-[65%] px-4 md:px-8 lg:px-20 ">
        <h2 class="text-3xl font-extrabold font-serif text-center text-primary mb-6">Contact Us</h2>
        <div class="space-y-6">
            <div>
                <label class="block text-gray-800 text-sm mb-2">Full Name</label>
                <input v-model="full_name" type="text" placeholder="Enter Full Name"
                    class="w-full px-3 py-2 border-b  bg-[#f3f4f8] border-gray-300 shadow-sm outline-none ">
            </div>
            <div>
                <label class="block text-gray-800 text-sm mb-2">Email Address</label>
                <input v-model="email" type="email" placeholder="Enter Email Address"
                    class="w-full px-3 border-b bg-[#f3f4f8] border-gray-300   shadow-sm py-2 outline-none">
            </div>
            <div>
                <label class="block text-gray-800 text-sm mb-2">Your Message</label>
                <textarea v-model="message" placeholder="Start writing from here"
                    class="w-full px-3 border-b bg-[#f3f4f8] border-gray-300   shadow-sm h-24 resize-none py-2  outline-none"></textarea>
            </div>
            <div class="flex justify-center">
                <button type="button" @click="sendMessage"
                    class="w-44 py-3 rounded-md bg-secondary  text-white text-sm text-center  shadow-md">
                    Send Message
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const full_name = ref('')
const email = ref('')
const message = ref('')

const sendMessage = () => {
    console.log(full_name.value, email.value, message.value)
}
</script>