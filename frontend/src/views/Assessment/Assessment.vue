<template>
    <div class="p-4 w-full">
        <Breadcrumb />
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <h1 class="text-h2 font-primary font-semibold text-primary truncate">{{ title }}</h1>
                <p class=" w-16 py-1 text-center hidden md:block rounded-2xl text-red-700 bg-red-100 font-bold"
                    v-if="Object.keys(initialData).length">Draft</p>
            </div>
            <div class="flex justify-between w-full md:w-auto">
                <p class=" w-16 py-1 text-center block md:hidden rounded-2xl text-red-700 bg-red-100 font-bold"
                    v-if="Object.keys(initialData).length">Draft</p>
                <button v-if="Object.keys(results).length" @click="() => router.push(`${current_path}/results`)"
                    class="border flex items-center gap-2 text-secondary border-[#255B97] rounded-md h-9 px-4 text-sm truncate">
                    View Results
                    <FileSearch2 class="w-4" />
                </button>
            </div>
        </div>
        <transition name="fade" mode="out-in">
            <div class="w-full">
                <FormView v-if="title !== 'Diversity Equity Inclusion'" :initialData="initialData" :doctype="title"
                    :onSubmit="handleSubmit" :isTable="true" :isDraft="true" :section="true"
                    :save_as_draft="save_as_draft" :key="title" />
                    <div v-if="title == 'Diversity Equity Inclusion'" class="w-full h-96 flex justify-center items-center text-h2">Coming Soon..</div>
                <!-- <FormView v-if="title == 'Diversity Equity Inclusion'" :initialData="initialData" :doctype="title"
                    :onSubmit="handleSubmit" :isDraft="true" :isCard="true" :section="true"
                    :save_as_draft="save_as_draft" :key="title" /> -->
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

const route = useRoute()
const router = useRouter()
const current_path = ref(route.fullPath)
const title = ref(splitAtSecondCapital(route.name));
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const initialData = ref({});
const results = ref({});
import { FileSearch2 } from 'lucide-vue-next'
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
            localStorage.removeItem('re_attempt');
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
            localStorage.removeItem('draft');
            toast.info('Draft saved successfully');
            get_save_as_draft()
            return res;
        }
    } else if (!auth.isLoggedIn) {
        localStorage.setItem('draft', JSON.stringify(formData));
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
            let re_attempt = localStorage.getItem('re_attempt');
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
    let draft = JSON.parse(localStorage.getItem('draft') ?? '{}');
    if (Object.keys(draft).length) {
        if (auth.isLoggedIn) {
            await save_as_draft(draft);
        } else {
            initialData.value = draft;
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
