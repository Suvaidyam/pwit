<template>
    <div :class="store.sidebar ? 'block' : 'hidden md:block'" class="w-16 md:w-60 h-screen fixed top-0 left-0 z-20">
        <div class="flex justify-end  bg-white fixed px-4 md:px-10 lg:px-20 h-20 items-center">
            <router-link to="/" class="text-2xl font-bold text-primary">
                <img :src="`/files/logo.png`" class="w-40 h-14" alt="">
            </router-link>
        </div>
        <div  class="w-full h-full bg-primary p-2 pt-24 ">
            <LeftMenuLoader v-if="loading" />
            <div v-if="!loading" class="w-full h-full">
                <div class="w-full text-white opacity-40 block md:hidden text-center py-2 hover:bg-white hover:text-black rounded-md mb-1 cursor-pointer"
                    @click="store.sidebar = false">X</div>
                <p class="pl-2 hidden md:block py-2 font-bold text-[11px] text-white">
                    RECOMMENDED PRINCIPLES
                </p>
                <div class="" v-for="items in recommended" :key="items.name">
                    <router-link :to="`/funder/${items.ref_doctype?.toLowerCase()?.split(' ').join('-')}`"
                        :class="['/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-'), '/funder/' + items.ref_doctype?.toLowerCase()?.split(' ').join('-') + '/results'].includes(route.fullPath) ? 'bg-white' : 'text-white'"
                        class="text-sm px-2 h-10 flex gap-2 items-center justify-center md:justify-normal rounded-md mb-2 hover:bg-white hover:text-black">
                        <img :src="items.icon" alt="" class="w-5 h-5">
                        <p class="hidden md:block">{{ items.label }}</p>
                    </router-link>
                </div>
                <p v-if="additional.length > 0"
                    class="pl-2 hidden md:block py-2 font-bold text-[11px] text-white border-t">
                    ADDITIONAL PWIT PRINCIPLES
                </p>
                <div class="" v-for="items in additional" :key="items.name">
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
import { ref, computed, inject, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import LeftMenuLoader from './LeftMenuLoader.vue';

const route = useRoute();
const store = inject('store');
const call = inject('$call');
const session = JSON.parse(localStorage.getItem('session'));
const menu_list = ref([]);
const logic = ref([]);
const results = ref({});
const loading = ref(true);

const leftMenu = async () => {
    const res = await call('pwit.controllers.api.left_menu_list', {});
    if (res.code === 200) {
        menu_list.value = res.data;
    }
};

const get_result = async () => {
    loading.value = true;
    try {
        const response = await call('pwit.controllers.api.get_results', {
            doctype: 'Funder Diagnostic',
            session: session.data.name
        });

        const groupedSums = Object.entries(response.data).reduce((acc, [key, value]) => {
            const prefix = key.split('_').slice(0, -1).join('_');
            acc[prefix] = (acc[prefix] || 0) + value;
            return acc;
        }, {});
        results.value = groupedSums;
    } catch (error) {
        console.error('Error fetching results:', error);
    } finally {
        loading.value = false;
    }
};

const get_recomm = async () => {
    loading.value = true;
    try {
        const res = await call('pwit.controllers.api.get_recommended_principles', {});
        if (res.code === 200) {
            logic.value = res.data;
        }
    } catch (error) {
        console.error('Error fetching recommendations:', error);
    } finally {
        loading.value = false;
    }
};

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

const computedMatchingLogic = computed(() => evaluateLogic(logic.value, results.value));

const recommended = computed(() => {
    const matchingLogic = computedMatchingLogic.value[0] || {};
    const recommendationKeys = [
        matchingLogic.recommendation_1,
        matchingLogic.recommendation_2,
        matchingLogic.recommendation_3
    ].filter(Boolean);

    return results.length
        ? menu_list.value?.filter(item => recommendationKeys.includes(item.code))
        : menu_list.value
});

const additional = computed(() => {
    const matchingLogic = computedMatchingLogic.value[0] || {};
    const additionalKeys = [
        matchingLogic.additional_1,
        matchingLogic.additional_2
    ].filter(Boolean);

    return results.length ? menu_list.value?.filter(item => additionalKeys.includes(item.code))
        : [];
});

onMounted(() => {
    get_result();
    get_recomm();
    leftMenu();
});
</script>
