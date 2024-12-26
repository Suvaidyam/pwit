<template>
    <div class="w-full h-screen p-4">
        <div class="flex gap-2">
            <Text @click="store.sidebar = true" class="w-6 min-w-6 cursor-pointer block md:hidden" />
            <!-- <p class="text-gray-800 text-sm">
                <router-link to="/">Home</router-link>
                / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> / <router-link
                    to="/recommended">Recommended Principles</router-link> /
                <router-link :to="`/funder/${route.params.category}`">{{ title=='Organisational Development'?' Organisation Development':title }}</router-link>
                <span class="text-gray-400 truncate"> / Results and Recommendations</span>
            </p> -->
            <router-link to="/" class="flex text-trbase items-center gap-1"><House class="w-4 h-4"/> Home</router-link>|
            <div class="flex items-center text-trbase cursor-pointer" @click="router.back(-1)"><ArrowBigLeft  class="w-5"/> Back</div>
        </div>
        <div class="flex justify-between items-center">
            <h1 class="text-h3 md:text-h2 text-primary truncate">{{ recommendations?.details?.title }}</h1>
            <div class="flex items-center gap-3">
                <button v-if="recommendations.result && Object.keys(recommendations.result).length"
                    class="border border-[#255B97] flex items-center gap-2 truncate rounded-md h-7 md:h-9 text-secondary text-sm px-2 md:px-4"
                    @click="re_attempt">
                    <span class="hidden md:block"
                        v-if="recommendations?.draft?.data && Object.keys(recommendations?.draft?.data).length">Continue
                        Assessment</span>
                    <span class="hidden md:block" v-else>Retake</span>
                    <ChevronRight class="w-4"
                        v-if="recommendations?.draft?.data && Object.keys(recommendations?.draft?.data).length" />
                    <RefreshCcw class="w-4" v-else />
                </button>
                <DownloadResults :ref_doctype="title == 'Multi Year Partnerships' ? 'Multi-year Partnerships' : title"
                    :disabled="recommendations.result && Object.keys(recommendations.result).length > 0 ? false : true" />
            </div>
        </div>
        <div class="w-full results-section"
            :class="recommendations.result && Object.keys(recommendations.result).length ? '' : 'h-full'"
            v-if="!loading">
            <div class="w-full" v-if="recommendations.result && Object.keys(recommendations.result).length">
                <div class="w-full grid grid-cols-1 xl:grid-cols-2 gap-5 pt-4">
                    <div class="w-full  mx-auto">
                        <div class="bg-white border p-4">
                            <div class="flex justify-between items-center">
                                <h2 class="text-primary font-bold font-primary text-h5">
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
                                                class="w-1/2 px-4 py-2 text-left font-primary text-h6 text-trbase font-bold border">
                                                Parameters
                                            </th>
                                            <th
                                                class="w-1/2 px-4 py-2 text-left font-primary text-h6 text-trbase font-bold border">
                                                Performance at that stage
                                            </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-if="recommendations.result" v-for="item in recommendations.result"
                                            :key="item.key" class="border-b">
                                            <td
                                                class="w-1/2 px-4 py-2 font-normal text-h6 text-pbase border border-gray-200">
                                                {{ item.key }}
                                            </td>
                                            <td class="py-2 px-4">
                                                <div class="h-4 bg-gray-200">
                                                    <div class="h-4 text-xs flex justify-center"
                                                        :class="[item.priority == 'High' ? 'bg-[#337357] w-full text-green-200' : item.priority == 'Medium' ? 'w-2/3 bg-[#FFD23F] text-yellow-100' : 'bg-[#FF6464] w-1/3 text-red-100']">
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
                            <p class="text-sm text-trbase text-justify">
                                {{ recommendations?.details?.description }}
                            </p>
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-1 xl:grid-cols-[70%_30%] md:grid-cols-1  lg:grid-cols-1 gap-4 pt-4 w-full">
                    <!-- Recommended Actions Section -->
                    <div v-if="recommend_action.length"
                        class="w-full mx-auto h-96 relative overflow-y-auto">
                        <p class="text-primary font-bold sticky top-0 bg-white font-primary text-xl sm:text-2xl pb-4">
                            Recommended actions
                        </p>
                        <div v-if="recommend_action.length"
                            v-for="items in recommend_action" :key="items.name" class="pb-5">
                            <div
                                class="flex justify-between items-center px-4 py-2 bg-[#e9eaec] text-h5 font-bold font-primary text-pbase">
                                {{ items.title }}
                            </div>
                            <div class="pt-2" v-html="items.actions"></div>
                        </div>
                    </div>
                    <!-- Useful Resources Section -->
                    <div v-if="recommendations?.details?.useful_resources"
                        class="w-full mx-auto rounded-sm shadow-md px-4 pb-2 h-96 overflow-y-auto">
                        <p class="text-primary sticky top-0 bg-white font-bold font-primary text-xl sm:text-2xl pb-4">
                            Useful resources
                        </p>
                        <div v-for="resource in recommendations?.details?.useful_resources" :key="resource.title"
                            class="flex flex-col gap-1 py-3 border-b ">
                            <p v-if="resource.section" class="text-h6 font-bold bg-gray-100 px-2 py-1">{{ resource.section }}</p>
                            <div class="flex items-center gap-2">
                                <span class="flex justify-center pt-1">
                                    <svg class="w-4 h-4" fill="none" xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 13 13">
                                        <path
                                            d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z"
                                            fill="#27853F" />
                                    </svg>
                                </span>
                                <a :href="resource.to" target="_blank"
                                    class="text-pbase hover:text-blue-500 text-h6 font-normal text-justify">
                                    {{ resource.resources }}
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-full h-full flex flex-col items-center justify-center " v-else>
                <img src="../../assets/no-results.png" class="w-40" alt="">
            </div>
        </div>
        <div class="w-full h-full flex justify-center items-center" v-if="loading">
            <div class="w-10 h-10 border-2 border-t-[4px] border-[#255B97] rounded-full animate-spin"></div>
        </div>
        <div class="py-5 flex justify-end">
            <router-link v-if="store?.nextPrinciple?.ref_doctype"
                :to="`/funder/${store?.nextPrinciple?.ref_doctype?.toLowerCase()?.split(' ').join('-')}`"
                class="w-full flex justify-center md:w-fit gap- py-3 px-6 bg-[#255B97] text-white rounded">
                Next Principle
                <ChevronRight class="w-[18px]" />
            </router-link>
        </div>
    </div>

</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import DownloadResults from './DownloadResults.vue';
import { Text, RefreshCcw, ChevronRight,House,ArrowBigLeft } from 'lucide-vue-next';

const route = useRoute()
const router = useRouter()
const store = inject('store');
const call = inject('$call');
const auth = inject('$auth');
const recommendations = ref({});
const recommend_action = ref([]);
const loading = ref(false);
const title = ref(splitAtSecondCapital(route.path));

const get_results = async () => {
    loading.value = true
    let url
    if (title.value == 'Diversity Equity Inclusion') {
        url = 'get_dei_result'
    } else {
        url = 'get_assistive_result'
    }
    try {
        let res = await call(`pwit.controllers.api.${url}`, {
            doctype: title?.value == "Multi Year Partnerships" ? 'Multi-year Partnerships' : title.value,
            session: store.session,
            user: auth.cookie.user_id !== 'Guest' ? auth.cookie.user_id : ''
        })
        if (res.code === 200) {
            recommendations.value = res.data
            loading.value = false
            let actions = res?.data?.details?.recommended_actions
            let groups = res?.data?.group
            if (actions.length) {
                recommend_action.value = actions.sort((a, b) => groups[a.title] - groups[b.title]);
            }
            setTimeout(() => {
                const targetLi = document.querySelectorAll('ol');
                const targetOl = document.querySelectorAll('li[data-list="unchecked"]');
                const targetInLI = document.querySelectorAll('li[data-list="bullet"]');
                if (targetLi) {
                    targetLi.forEach((li) => {
                        li.style.paddingLeft = '20px';
                    });
                    targetOl.forEach((ol) => {
                        ol.style.listStyleType = 'disc';
                    });
                    targetInLI.forEach((li) => {
                        li.style.marginLeft = '40px';
                        li.style.listStyleType = 'circle';
                    });
                    document.querySelectorAll('a').forEach(anchor => {
                        if (anchor.href && !anchor.href.startsWith(location.origin)) {
                            anchor.setAttribute('target', '_blank');
                            anchor.style.color = '#255B97';
                        }
                    });

                }
            }, 1000)
        }
    } catch (error) {
        loading.value = false
    }
}
const re_attempt = () => {
    router.push(`/funder/${route.params.category}`)
    sessionStorage.setItem('re_attempt', true)
    if(recommendations?.draft?.data && Object.keys(recommendations?.draft?.data).length){
        store.is_dei_ass=true
    }else{
        store.is_dei_ass=false
    }
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

<style scoped>
/* Styling for modern browsers */
::-webkit-scrollbar {
    width: 10px;
    /* Width of the scrollbar */
}

::-webkit-scrollbar-track {
    background: #f4f4f4;
    /* Background of the scrollbar track */
}

* {
    scrollbar-width: thin;
    scrollbar-color: #255B97 #f4f4f4;
}
</style>