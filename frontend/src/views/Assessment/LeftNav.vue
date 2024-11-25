<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'" class="w-16 md:w-60 h-screen fixed top-0 left-0 z-20">
        <div class="flex justify-end  bg-white fixed px-4 md:px-10 lg:px-20 h-20 items-center">
            <router-link to="/" class="text-2xl font-bold text-primary">
                <img :src="`/files/logo.png`" class="w-40 h-14" alt="">
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
                        <img :src="items.icon" alt="" class="w-5 h-5">
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
                        <img :src="items.icon" alt="" class="w-5 h-5">
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

</script>
