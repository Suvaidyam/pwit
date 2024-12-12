<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'" class="w-16 md:w-60 h-screen fixed top-0 left-0 z-20">
        <div class="flex justify-end  bg-white fixed px-4 md:px-10 lg:px-20 h-20 items-center">
            <router-link to="/" class="text-2xl font-bold text-primary">
                <!-- <img src="../../assets/navbar.png" class="w-40 h-14" alt=""> -->
                <svg width="159" height="52" viewBox="0 0 159 52" fill="none" xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink">
                    <rect width="159" height="52" fill="url(#pattern0_2084_87)" />
                    <defs>
                        <pattern id="pattern0_2084_87" patternContentUnits="objectBoundingBox" width="1" height="1">
                            <use xlink:href="#image0_2084_87"
                                transform="matrix(0.00403758 0 0 0.0123457 -0.00469757 0)" />
                        </pattern>
                        <image id="image0_2084_87" width="250" height="81"
                            xlink:href="data:image/png;base64,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" />
                    </defs>
                </svg>
            </router-link>
        </div>
        <div class="w-full h-full bg-primary p-2 pt-24 ">
            <LeftMenuLoader v-if="loading" />
            <div v-if="!loading" class="w-full h-full">
                <div class="w-full text-white opacity-40 block md:hidden text-center py-2 hover:bg-white hover:text-black rounded-md mb-1 cursor-pointer"
                    @click="store.sidebar = false">X</div>
                <p class="pl-2 hidden md:block py-2 font-bold text-[11px] text-white">
                    RECOMMENDED PRINCIPLES
                </p>
                <div class="" v-for="items in recommendedList" :key="items.name">
                    <router-link :to="`/funder/${items.ref_doctype?.toLowerCase()?.split(' ').join('-')}`"
                        :class="['/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-'), '/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-') + '/results'].includes(route.fullPath) ? 'bg-white' : 'text-white'"
                        class="text-sm px-2 h-10 flex gap-2 items-center justify-center md:justify-normal rounded-md mb-2 hover:bg-white hover:text-black">
                        <img v-if="items.icon" :src="items.icon" alt="" class="w-5 h-5">
                        <div v-else>
                            <IndianRupee v-if="items.ref_doctype == 'Core Costs'" class="w-5 h-5" />
                            <Handshake v-if="items.ref_doctype == 'Multi-year Partnerships'" class="w-5 h-5" />
                            <PiggyBank v-if="items.ref_doctype == 'Financial Resilience'" class="w-5 h-5" />
                            <ChartNoAxesCombined v-if="items.ref_doctype == 'Organization Development'" class="w-5 h-5" />
                            <Scale v-if="items.ref_doctype == 'Diversity Equity Inclusion'" class="w-5 h-5" />
                        </div>
                        <p class="hidden md:block">{{ items.label }}</p>
                    </router-link>
                </div>
                <p v-if="recommendedList.length > 0"
                    class="pl-2 hidden md:block py-2 font-bold text-[11px] text-white border-t">
                    ADDITIONAL PWIT PRINCIPLES
                </p>
                <div class="" v-for="items in additionalList" :key="items.name">
                    <router-link :to="`/funder/${items.ref_doctype?.toLowerCase()?.split(' ').join('-')}`"
                        :class="['/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-'), '/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-') + '/results'].includes(route.fullPath) ? 'bg-white' : 'text-white'"
                        class="text-sm px-2 h-10 flex gap-2 items-center justify-center md:justify-normal rounded-md mb-2 hover:bg-white hover:text-black">
                        <img v-if="items.icon" :src="items.icon" alt="" class="w-5 h-5">
                        <div v-else>
                            <IndianRupee v-if="items.ref_doctype == 'Core Costs'" class="w-5 h-5" />
                            <Handshake v-if="items.ref_doctype == 'Multi-year Partnerships'" class="w-5 h-5" />
                            <PiggyBank v-if="items.ref_doctype == 'Financial Resilience'" class="w-5 h-5" />
                            <ChartNoAxesCombined v-if="items.ref_doctype == 'Organization Development'" class="w-5 h-5" />
                            <Scale v-if="items.ref_doctype == 'Diversity Equity Inclusion'" class="w-5 h-5" />
                        </div>
                        <p class="hidden md:block">{{ items.label }}</p>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import LeftMenuLoader from './LeftMenuLoader.vue';
import { IndianRupee, Handshake, PiggyBank, ChartNoAxesCombined, Scale } from 'lucide-vue-next'

const route = useRoute();
const store = inject('store');
const call = inject('$call');
const auth = inject('$auth');
const menu_list = ref([]);
const loading = ref(false);
const recommendedList = ref([])
const additionalList = ref([])

const leftMenu = async () => {
    loading.value = true;
    const res = await call('pwit.controllers.api.left_menu_list', {});
    if (res.code === 200) {
        loading.value = false;
        menu_list.value = res.data;
    }
};


const get_result = async () => {
    return new Promise((resolve, reject) => {
        loading.value = true;
        call('pwit.controllers.api.get_results', {
            doctype: 'Funder Diagnostic',
            session: store.session,
            user: auth.cookie.user_id !== 'Guest' ? auth.cookie.user_id : ''
        })
            .then(res => {
                const groupedSums = Object.entries(res.data).reduce((acc, [key, value]) => {
                    const keyParts = key.split('_');
                    keyParts.pop();
                    const prefix = keyParts.join('_');
                    acc[prefix] = (acc[prefix] || 0) + value;
                    return acc;
                }, {});
                resolve(groupedSums);
            })
            .catch(error => {
                reject(error);
            })
            .finally(() => {
                loading.value = false;
            });
    });
};

// Fetch recommended principles
const get_recomm = async () => {
    return new Promise((resolve, reject) => {
        loading.value = true;
        call('pwit.controllers.api.get_recommended_principles', {})
            .then(res => {
                if (res.code === 200) {
                    resolve(res.data);
                }
            })
            .catch(error => {
                reject(error);
            })
            .finally(() => {
                loading.value = false;
            });
    });
};

function sortAndAssign(d) {
    d.sort((a, b) => {
        if (a.score === b.score) {
            return a.priority - b.priority;
        }
        return a.score - b.score;
    });
    d.forEach((item, index) => {
        item.group = index < 3 ? 'Recommended' : 'Additional';
    });
    return d;
}
// Evaluate logic dynamically based on results
const evaluateLogic = (logicArray, results) => {
    return logicArray.filter(entry => {
        try {
            if (entry?.logic?.trim()) {
                const substitutedLogic = entry.logic.replace(
                    /\b(core_cost|od|myp|fr|dei)\b/g,
                    match => `(${results[match] || 0})`
                );
                return eval(substitutedLogic);
            }
            return false;
        } catch (e) {
            console.error(`Error evaluating logic for entry ${entry.name}:`, e);
            return false;
        }
    });
};

watch(() => menu_list.value, async (value) => {
    menu_list.value = value
    recommendedList.value = await value?.filter(e => e.group === 'Recommended')
    additionalList.value = await value?.filter(e => e.group === 'Additional')
    let doc = await splitAndCapitalize(route.fullPath)
    let index = (recommendedList.value.concat(additionalList.value)).findIndex(e => e.ref_doctype == (doc == 'Multi Year Partnerships' ? 'Multi-year Partnerships' : doc))
    store.nextPrinciple = index !== -1 && index < (recommendedList.value.concat(additionalList.value)).length - 1 ? (recommendedList.value.concat(additionalList.value))[index + 1] : null;
}, { deep: true, immediate: true });
watch(() => route.fullPath, async (value) => {
    let doc = await splitAndCapitalize(value)
    let index = (recommendedList.value.concat(additionalList.value)).findIndex(e => e.ref_doctype == (doc == 'Multi Year Partnerships' ? 'Multi-year Partnerships' : doc))
    store.nextPrinciple = index !== -1 && index < (recommendedList.value.concat(additionalList.value)).length - 1 ? (recommendedList.value.concat(additionalList.value))[index + 1] : null;
}, { deep: true, immediate: true });
// Fetch menu_list on mount
onMounted(async () => {

    await leftMenu();
    let assessmentResult = await get_result()
    let logics = await get_recomm();
    let topMatching = await evaluateLogic(logics, assessmentResult)?.[0];
    if (!topMatching) {
        let updatedData = menu_list?.value?.map(e => {
            e.score = assessmentResult[e.code] || 0;
            return e;
        });
        menu_list.value = sortAndAssign(updatedData);

    } else {
        menu_list.value = [
            { ...menu_list.value.find(e => e.code === topMatching.recommendation_1), group: 'Recommended' },
            { ...menu_list.value.find(e => e.code === topMatching.recommendation_2), group: 'Recommended' },
            { ...menu_list.value.find(e => e.code === topMatching.recommendation_3), group: 'Recommended' },
            { ...menu_list.value.find(e => e.code === topMatching.additional_1), group: 'Additional' },
            { ...menu_list.value.find(e => e.code === topMatching.additional_2), group: 'Additional' }
        ]
    }

});
function splitAndCapitalize(str) {
    return str
        .split('/')[2]
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}
</script>
