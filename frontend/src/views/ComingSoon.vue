<template>
    <div class="w-full h-full">
        <div class="flex flex-col items-center gap-2">
            <img src="../assets/navbar.png" alt="" class="w-52">
            <p class="text-secondary text-h4 font-semibold">Assistive Funder Toolkit</p>
        </div>
        <div class="w-full flex flex-col gap-6 items-center justify-center h-1/2 px-4">
            <p class="text-h3 text-trbase">The Assistive Funder Tooklit will be launched soon!</p>
            <div class="flex flex-col md:flex-row gap-2 items-center">
                <p class="text-xl text-trbase">Be the first to know when we go live:</p>
                <div class="flex gap-2 items-center">
                    <input v-model="email" type="email" name="" id="" placeholder="test@example.com"
                    class="outline-none border-2 py-1.5 px-2 rounded-md border-primary text-h5">
                <button :disabled="loading" @click="handleClick()"
                    class="px-4 flex items-center gap-2 py-2 bg-secondary text-white rounded-md">Submit
                    <div v-if="loading"
                        class="animate-spin h-full w-full rounded-full border-[2px] flex justify-center items-center border-dotted border-[#002C77]">
                        <div class="w-3 h-3 rounded-full border-dashed border-[1px] border-[#002C77]"></div>
                    </div>
                </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, inject } from 'vue';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { useRoute, useRouter } from 'vue-router';



const loading = ref(false)
const email = ref('')
// const route = useRoute();
// const router = useRouter();
const call = inject('$call');
// const session = inject('$session');
// const store = inject('store');

const validateEmail = (email) => {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
}

const handleClick = async () => {
    if (!validateEmail(email.value)) {
        toast.error('Please enter a valid email address.')
        return
    }
    loading.value = true
    try {
        const res = await call('pwit.controllers.api.subscribe', { email: email.value })
        if (res.code == 200) {
            toast.success(res.message)
            email.value = ''
            setTimeout(() => {
                loading.value = false
            }, 1000);
        } else if (res.code == 201) {
            toast.error(res.message)
            loading.value = false
        }
    } catch (error) {
        loading.value = false
        toast.error('Something went wrong. Please try again later.')

    }
};

</script>