<template>
    <div class="p-4 w-full">
        <div class="flex justify-between gap-3 pb-2">
            <Breadcrumb />
            <div class="flex justify-between gap-3">
                <p class=" w-16 py-1 text-center rounded-2xl text-red-700 bg-red-100 font-bold"
                    v-if="Object.keys(initialData).length">Draft</p>
                <button v-if="Object.keys(results).length" @click="() => router.push(`${current_path}/results`)"
                    class="border flex items-center gap-2 text-secondary border-[#255B97] rounded-md h-9 px-4 text-sm truncate">
                    View Results
                    <FileSearch2 class="w-4" />
                </button>
            </div>
        </div>
        <div class="flex items-center gap-3">
                <h1 v-for="item in heading.filter((e)=>e.name==title)" class="text-h4 md:text-h2 font-primary font-semibold text-primary leading-8">{{ item.label }}</h1>
               
            </div>
        <p v-if="title !== 'Diversity Equity Inclusion'" class="pt-3 text-h5 text-sebase">For each question, we ask you to select the level that largely corresponds to your organisation’s current practices, if any.</p>
        <transition name="fade" mode="out-in">
            <div class="w-full pt-4">
                <FormView v-if="title !== 'Diversity Equity Inclusion'" :width="true" :initialData="initialData" :doctype="title"
                    :onSubmit="handleSubmit" :isTable="true" :isDraft="true" :section="true"
                    :save_as_draft="save_as_draft" :key="title" />
                <DiversityEquity  v-if="title == 'Diversity Equity Inclusion' && !store.is_dei_ass"/>
                <FormView v-if="title == 'Diversity Equity Inclusion' && store.is_dei_ass" :width="true" :initialData="initialData" :doctype="title"
                    :onSubmit="handleSubmit" :isDraft="true" :isCard="true" :section="true"
                    :save_as_draft="save_as_draft" :isColumn="true" :key="title" />
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, watch, inject, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import Breadcrumb from './Breadcrumb.vue'
import { FormView } from '../../../../../sva_form_vuejs/form_view';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { FileSearch2 } from 'lucide-vue-next'
import DiversityEquity from './DiversityEquity.vue'

const route = useRoute()
const router = useRouter()
const current_path = ref(route.fullPath)
const title = ref(splitAtSecondCapital(route.name));
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const initialData = ref({});
const results = ref({});

const heading = ref([{
                'label':'Develop multiyear funder-nonprofit partnerships',
                'name':'Multi-year Partnerships'
            },
            {
                'label':'Embed diversity, equity, and inclusion in grantmaking',
                'name':'Diversity Equity Inclusion'
            },
            {
                'label':'Invest in organisational development',
                'name':'Organisational Development'
            },
            {
                'label':'Build financial resilience',
                'name':'Financial Resilience'
            },
            {
                'label':'Pay a fair share of core costs',
                'name':'Core Costs'
            }
]);

watch(route, (oldVal, newVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    current_path.value = newVal.path
    if (auth.isLoggedIn) {
        get_save_as_draft();
    }
})
watch(() => title.value, async (newVal) => {
    await get_results();
    title.value = newVal
})
watch(()=>initialData.value, (newVal) => {
    initialData.value = newVal
}, {deep: true, immediate: true})

const handleSubmit = async (formData) => {
    try {
        const res = await call('pwit.controllers.api.save_doc', { doctype: title.value, doc: { ...formData, 'session': store.session }, name: initialData?.value?.name });
        if (res.code === 200) {
            sessionStorage.removeItem('re_attempt');
            router.push(`${current_path.value}/results`);
        }
    } catch (err) {
        console.error('Error saving form:', err);
    }
};
const save_as_draft = async (formData) => {
    let changes
    if (Object.keys(initialData.value).length) {
        changes = await compareObjects(initialData.value, formData)
    } else {
        changes = true
    }
    if (auth.isLoggedIn && changes) {
        const res = await call('pwit.controllers.api.save_as_draft', { doctype: title.value, doc: { ...formData, 'session': store.session }, name: initialData?.value?.name });
        if (res.code === 200) {
            sessionStorage.removeItem('draft');
            toast.info('Draft saved successfully');
            get_save_as_draft()
            return res;
        }
    } else if (!auth.isLoggedIn) {
        sessionStorage.setItem('draft', JSON.stringify(formData));
        store.save_as_login = true;
    }
}
function compareObjects(initialData, formData) {
    let changes = [];
    Object.entries(formData).filter(([key]) => key.startsWith('myp') || key.startsWith('cc') || key.startsWith('dei') || key.startsWith('od') || key.startsWith('fr')).forEach(([key, value]) => {
        if (value && initialData[key] != value) {
            changes.push({ key, value: initialData[key] })
        }
    })
    if (changes.length) {
        return true;
    } else {
        return false;
    }
}
const get_save_as_draft = async () => {
    try {
        let res = await call('pwit.controllers.api.get_save_as_draft', { doctype: title.value, user: auth.cookie.user_id });
        if (res.code === 200) {
            initialData.value = res?.data ?? {};
        }
    } catch (error) {

    }
}

const get_results = async () => {
    try {
        let res = await call('pwit.controllers.api.get_assistive_result', {
            doctype: title.value,
            session: store.session,
            user: auth.cookie.user_id !== 'Guest' ? auth.cookie.user_id : ''
        })
        if (res.code === 200) {
            let re_attempt = sessionStorage.getItem('re_attempt');
            results.value = res.data.result;
            if (Object.keys(res.data.result).length && !re_attempt && Object.keys(initialData.value).length === 0) {
                router.push(`${current_path.value}/results`);
            }
        }
    } catch (error) {

    }
}
function splitAtSecondCapital(input) {
    return input
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .trim();
}
onMounted(async () => {
    get_results();
    let draft = JSON.parse(sessionStorage.getItem('draft') ?? '{}');
    if (Object.keys(draft).length) {
        if (auth.isLoggedIn) {
            await save_as_draft(draft);
        }
    }
    if (auth.isLoggedIn) {
        get_save_as_draft();
    }
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
