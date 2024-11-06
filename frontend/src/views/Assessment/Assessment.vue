<template>
    <div class="p-4 h-full w-full">
        <Breadcrumb />
        <h1 class="text-h2 font-serif font-semibold text-primary">{{ title }}</h1>
        <Loader v-if="loading" />
        <transition name="fade" mode="out-in">
            <div v-if="!loading" class="w-full h-full">
                <div class="flex flex-col pt-4">
                    <div class="" v-for="(item, index) in question" :key="item.name">
                        <div class="flex gap-2">
                            <div class="w-5 h-5 rounded-full flex items-center justify-center text-xs text-white bg-slate-700">
                                {{ index + 1 }}
                            </div>
                            <h2 class="text-sebase text-h5">{{ item.label }}</h2>
                        </div>
                        <div class="flex h-56 flex-col border mt-3 w-full text-sm">
                            <div class="w-full h-8 bg-tatary min-h-8 border-b flex">
                                <div class="w-10 h-full border-r"></div>
                                <div class="w-28 border-r flex items-center justify-center">Level</div>
                                <div class="w-full border-r flex items-center justify-center">Options</div>
                            </div>
                            <div class="flex w-full h-full border-b" v-for="option in item.options" :key="option.name">
                                <div class="w-10 border-r flex items-center justify-center">
                                    <input type="radio" :name="item.name" :id="item.name">
                                </div>
                                <div class="w-28 border-r flex items-center justify-center bg-primary text-white"
                                    :style="{ opacity: (10 - option.level) / 10 }">
                                    Level {{ option.level }}
                                </div>
                                <div class="w-full flex items-center px-4">{{ option.label }}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex mt-4 gap-3">
                    <button class="bg-primary w-28 text-h5 h-12 rounded-md text-white">Submit</button>
                    <button class="border w-40 text-h5 h-12 rounded-md">Save as Draft</button>
                </div>
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue'
import { useRoute } from 'vue-router';
import Breadcrumb from './Breadcrumb.vue'
import Loader from './Loader.vue'

const call = inject('$call')
const route = useRoute()
const title = ref(splitAtSecondCapital(route.name));
const loading = ref(false)

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    question_list()
})
onMounted(() => {
    question_list()
})
const question_list = async () => {
    loading.value = true
    let res = await call('pwit.controllers.api.question_list', { doctype: title.value })
    if (res.code == 200) {
       setTimeout(() => {
            loading.value = false
        }, 500)
        console.log(res)
    }
}
const question = [
    {
        name: 1,
        label: "What is the total cost of the core activities of the organization?",
        options: [
            {
                name: "a",
                label: "Salaries and benefits of core staff",
                level: 1
            },
            {
                name: "b",
                label: "Rent and utilities",
                level: 2
            },
            {
                name: "c",
                label: "Office supplies",
                level: 3
            },
            {
                name: "d",
                label: "Other",
                level: 4
            },
        ]
    },
]
function splitAtSecondCapital(input) {
    return input
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .trim();
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
</style>
