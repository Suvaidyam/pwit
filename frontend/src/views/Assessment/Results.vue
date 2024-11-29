<template>
    <div class="w-full h-screen p-4">
        <div class="flex gap-2">
            <Text @click="store.sidebar = true" class="w-6 min-w-6 cursor-pointer block md:hidden" />
            <p class="text-gray-800 text-sm">
                <router-link to="/">Home</router-link>
                / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> / <router-link
                    to="/recommended">Recommended Principles</router-link> /
                <router-link :to="`/funder/${route.params.category}`">{{ title }}</router-link>
                <span class="text-gray-400 truncate"> / Results and Recommendtions</span>
            </p>
        </div>
        <div class="flex justify-between items-center">
            <h1 class="text-h3 md:text-h2 text-primary">Results and Recommendtions</h1>
            <div class="flex items-center gap-3">
                <button v-if="recommendations.result && Object.keys(recommendations.result).length" class="border border-[#255B97] flex items-center gap-2 rounded-md h-7 md:h-9 text-secondary text-sm px-2 md:px-4"
                    @click="re_attempt"><span class="hidden md:block">Retake</span> <RefreshCcw class="w-4"/> </button>
                <DownloadResults :disabled="recommendations.result && Object.keys(recommendations.result).length > 0 ? false : true" />
            </div>
        </div>
        <div class="w-full results-section" :class="recommendations.result && Object.keys(recommendations.result).length ? '' : 'h-full'" v-if="!loading">
            <div class="w-full" v-if="recommendations.result && Object.keys(recommendations.result).length">
                <div class="w-full grid grid-cols-1 xl:grid-cols-2 gap-5 pt-4">
                    <div class="w-full  mx-auto">
                        <div class="bg-white border p-4">
                            <div class="flex justify-between items-center">
                                <h2 class="text-primary font-bold font-serif text-2xl">
                                    Results and Recommendations
                                </h2>
                            </div>
                            <p class="text-h6 pt-1 pb-4">
                                <span class="font-medium">Average: </span>
                                <span class="text-green-600 font-semibold">{{ recommendations?.average ?? 0 }}</span>
                            </p>
                            <!-- Table -->
                            <div class="overflow-x-auto">
                                <table class="w-full border">
                                    <thead class="bg-[#E0F4FB]">
                                        <tr>
                                            <th
                                                class="w-1/2 px-4 py-2 text-left font-serif text-h6 text-trbase font-bold border">
                                                Parameters
                                            </th>
                                            <th
                                                class="w-1/2 px-4 py-2 text-left font-serif text-h6 text-trbase font-bold border">
                                                Performance at that stage
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-if="recommendations.result"
                                            v-for="[key, value] in Object.entries(recommendations.result)" :key="key"
                                            class="border-b">
                                            <td
                                                class="w-1/2 px-4 py-2 font-normal text-h6 text-pbase border border-gray-200">
                                                {{ key }}
                                            </td>
                                            <td class="py-2 px-4">
                                                <div class="h-4 bg-gray-200">
                                                    <div class="h-4 text-xs flex justify-center"
                                                        :class="[value == 4 ? 'bg-[#337357] w-full' : value == 3 ? 'w-2/3 bg-[#FFD23F]' : value == 2 ? 'bg-[#FF6464] w-1/3' : 'bg-[#FF6464] w-1/5']">
                                                        {{ recommendations.result ? '' : 'Not Found' }}
                                                    </div>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <!-- Right Section -->
                    <div class="w-full mx-auto flex justify-center items-center p-4">
                        <div class="text-start">
                            <p class="text-primary font-bold font-serif text-2xl pb-4">
                                {{ recommendations?.details?.title }}
                            </p>
                            <p class="text-h6 text-trbase text-justify">
                                {{ recommendations?.details?.description }}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-1 xl:grid-cols-[70%_30%] md:grid-cols-1  lg:grid-cols-1 gap-4 pt-4 w-full">
                    <!-- Recommended Actions Section -->
                    <div class="w-full mx-auto">
                        <p class="text-primary font-bold font-serif text-xl sm:text-2xl pb-4">
                            Recommended Actions
                        </p>
                        <div v-if="recommendations.details.recommended_actions" v-for="items in recommendations.details.recommended_actions" :key="items.name" class="pb-5">
                            <div
                                class="flex justify-between items-center px-4 py-2 bg-[#e9eaec] text-h5 font-bold font-serif text-pbase">
                                {{ items.title }}
                            </div>
                            <div class="pt-2" v-html="items.actions"></div>
                            <!-- <div class="pt-2">
                                <div v-for="item in action.items" :key="item.description" class="flex gap-4 pt-4">
                                    <div class="w-7 h-7 flex justify-center items-center">
                                        <svg class="w-5 h-5" fill="none" xmlns="http://www.w3.org/2000/svg"
                                            viewBox="0 0 16 16">
                                            <path
                                                d="M8 0L9.16938 5.17688L13.6569 2.34315L10.8231 6.83062L16 8L10.8231 9.16938L13.6569 13.6569L9.16938 10.8231L8 16L6.83062 10.8231L2.34315 13.6569L5.17688 9.16938L0 8L5.17688 6.83062L2.34315 2.34315L6.83062 5.17688L8 0Z"
                                                fill="#255B97" />
                                        </svg>
                                    </div>
                                    <p class="text-justify text-sm text-trbase font-normal">
                                        <strong class="text-pbase">{{ item.title }}</strong>
                                        {{ item.description }}
                                    </p>
                                </div>
                            </div> -->
                        </div>
                    </div>
                    <!-- Useful Resources Section -->
                    <div class="w-full mx-auto rounded-sm shadow-md px-4 py-2">
                        <p class="text-primary font-bold font-serif text-xl sm:text-2xl pb-4">
                            Useful Resources
                        </p>
                        <div v-for="resource in recommendations?.details?.useful_resources" :key="resource.title"
                            class="flex gap-4 py-3 border-b ">
                            <span class="flex justify-center pt-1">
                                <svg class="w-4 h-4" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13 13">
                                    <path
                                        d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z"
                                        fill="#27853F" />
                                </svg>
                            </span>
                            <a :href="resource.to" target="_blank" class="text-pbase text-h6 font-normal text-justify">
                                {{ resource.resources }}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-full h-full flex items-center justify-center text-h2 text-gray-700" v-else>Results Not Found
            </div>
        </div>
        <div class="w-full h-full flex justify-center items-center" v-if="loading">
            <div class="w-10 h-10 border-2 border-t-[4px] border-[#255B97] rounded-full animate-spin"></div>
        </div>
        <div class="py-5 w-full">
            <router-link :to="`/funder/${store?.nextPrinciple?.ref_doctype?.toLowerCase()?.split(' ').join('-')}`"
                class="w-full md:w-auto py-3 px-6 bg-[#255B97] text-white rounded">
                Next Principle
            </router-link>
        </div>
    </div>

</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import DownloadResults from './DownloadResults.vue';
import { Text,RefreshCcw } from 'lucide-vue-next';
import html2pdf from 'html2pdf.js';

const route = useRoute()
const router = useRouter()
const store = inject('store');
const call = inject('$call');
const auth = inject('$auth');
const recommendations = ref({});
const loading = ref(false);
const title = ref(splitAtSecondCapital(route.path));

const downloadPDF = () => {
    const element = document.querySelector(".results-section");
    const options = {
        margin: 0.5,
        filename: 'Results_and_Recommendations.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' },
    };

    html2pdf().set(options).from(element).save();
};

const get_results = async () => {
    loading.value = true
    try {
        let res = await call('pwit.controllers.api.get_assistive_result', {
            doctype: title?.value == "Multi Year Partnerships" ? 'Multi-year Partnerships' : title.value,
            session: store.session,
            user: auth.cookie.user_id !== 'Guest' ? auth.cookie.user_id : ''
        })
        if (res.code === 200) {
            recommendations.value = res.data
            loading.value = false
        }
    } catch (error) {
        loading.value = false
    }
}
const re_attempt = () => {
    router.push(`/funder/${route.params.category}`)
    localStorage.setItem('re_attempt', true)
}
watch(route, (newVal) => {
    title.value = splitAtSecondCapital(newVal.path)
})
onMounted(() => {
    get_results()
})
function splitAtSecondCapital(input) {
    input = input.split('/')[2]
    return input
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ')
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .trim();
}

</script>