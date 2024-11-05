<template>
    <div class="w-full h-full pt-6">
        <p @click="router.back(-1)" class="cursor-pointer text-sm px-4 md:px-8 lg:px-20">
            <ArrowLeftIcon class="h-4 w-4 inline-block " />
            Back
        </p>
        <h1 class="text-h2 px-4 md:px-8 lg:px-20 tracking-wide font-serif text-primary font-bold">
            Funder Diagnostic
        </h1>
        <p class="text-sm px-4 md:px-8 lg:px-20   font-serif text-sebase font-normal">
            Please select the degree to which your organization’s mindset and practices agree or disagree with the following statements:
        </p>
        <div class="w-full flex flex-col gap-4 px-4 md:px-8 lg:px-20 py-5 mt-4 bg-gray-100">
            <div v-for="(item, index) in data" :key="item.name">
                <div class="flex gap-3">
                    <div class="w-6 h-6 flex items-center justify-center text-xs rounded-full bg-gray-800 text-white">
                        {{ index + 1 }}
                    </div>
                    <h1 class="text-h5 font-normal ">{{ item.name1 }}</h1>
                </div>
                <div class="flex flex-col md:flex-row gap-3 pl-9 pt-2">
                    <div v-for="el in item.option" :key="el.name"
                        class="flex gap-2 bg-white items-center px-4 py-1.5 border rounded-md"
                        :class="{ 'border-[#3086c4]': el.checked }">
                        <input type="checkbox" :id="el.name" v-model="el.checked" class="cursor-pointer" />
                        <label :for="el.name" class="text-sm w-full truncate cursor-pointer">{{ el.name1 }}</label>
                    </div>
                </div>
            </div>
        </div>
        <div class="px-4 md:px-8 lg:px-20 py-4 flex gap-4 items-center">
            <button @click="submit"
                class="bg-secondary text-white px-6 py-2.5 text-sm border rounded-md">Submit</button>
            <button class="px-6 py-2.5 text-sm border rounded-md">Save as Draft</button>
        </div>
        <FooterNav />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { ArrowLeftIcon } from '@heroicons/vue/24/outline'
import { useRouter } from 'vue-router'
import FooterNav from '../components/FooterNav.vue';

const router = useRouter()
const data = ref([
    {
        name: 1,
        name1: 'Funder Diagnostic',
        option: [
            { name: 11, name1: 'Funder Diagnostic', checked: false },
            { name: 12, name1: 'Funder Diagnostic', checked: false },
            { name: 13, name1: 'Funder Diagnostic', checked: false },
            { name: 14, name1: 'Funder Diagnostic', checked: false }
        ]
    },
    {
        name: 2,
        name1: 'Funder Diagnostic',
        option: [
            { name: 21, name1: 'Funder Diagnostic', checked: false },
            { name: 22, name1: 'Funder Diagnostic', checked: false },
            { name: 23, name1: 'Funder Diagnostic', checked: false },
            { name: 24, name1: 'Funder Diagnostic', checked: false }
        ]
    },
    {
        name: 3,
        name1: 'Funder Diagnostic',
        option: [
            { name: 31, name1: 'Funder Diagnostic', checked: false },
            { name: 32, name1: 'Funder Diagnostic', checked: false },
            { name: 33, name1: 'Funder Diagnostic', checked: false },
            { name: 34, name1: 'Funder Diagnostic', checked: false }
        ]
    },
    {
        name: 4,
        name1: 'Funder Diagnostic',
        option: [
            { name: 41, name1: 'Funder Diagnostic', checked: false },
            { name: 42, name1: 'Funder Diagnostic', checked: false },
            { name: 43, name1: 'Funder Diagnostic', checked: false },
            { name: 44, name1: 'Funder Diagnostic', checked: false }
        ]
    },
    {
        name: 5,
        name1: 'Funder Diagnostic',
        option: [
            { name: 51, name1: 'Funder Diagnostic', checked: false },
            { name: 52, name1: 'Funder Diagnostic', checked: false },
            { name: 53, name1: 'Funder Diagnostic', checked: false },
            { name: 54, name1: 'Funder Diagnostic', checked: false }
        ]
    },
])
const submit = () => {
    // console.log(data.value)
    router.push('/recommended')
}
</script>
