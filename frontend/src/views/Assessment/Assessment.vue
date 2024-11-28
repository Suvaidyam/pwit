<template>
    <div class="p-4 w-full h-screen">
        <Breadcrumb />
        <div class="flex items-center gap-3">
            <h1 class="text-h2 font-serif font-semibold text-primary">{{ title }}</h1>
            <p class="w-16 py-1 flex items-center justify-center rounded-2xl text-red-700 bg-red-100 font-bold"
                v-if="Object.keys(initialData).length">Draft</p>
        </div>
        <transition name="fade" mode="out-in">
            <div class="w-full h-full">
                <FormView v-if="title !== 'Diversity Equity Inclusion'" :initialData="initialData" :doctype="title"
                    :onSubmit="handleSubmit" :isTable="true" :isDraft="true" :section="true"
                    :save_as_draft="save_as_draft" :key="title" />
                <FormView v-if="title == 'Diversity Equity Inclusion'" :initialData="initialData" :doctype="title"
                    :onSubmit="handleSubmit" :isDraft="true" :isCard="true" :section="true"
                    :save_as_draft="save_as_draft" :key="title" />
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

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    current_path.value = oldVal.path
    if (auth.isLoggedIn) {
        get_save_as_draft();
    }
})
console.log(router,'router')
const handleSubmit = async (formData) => {
    try {
        const res = await call('pwit.controllers.api.save_doc', { doctype: title.value, doc: { ...formData, 'session': store.session }, name: initialData?.value?.name });
        if (res.code === 200) {
            router.push(`${current_path.value}/results`);
        }
    } catch (err) {
        console.error('Error saving form:', err);
    }
};
const save_as_draft = async (formData) => {
    if (auth.isLoggedIn) {
        const res = await call('pwit.controllers.api.save_as_draft', { doctype: title.value, doc: { ...formData, 'session': store.session }, name: initialData?.value?.name });
        if (res.code === 200) {
            localStorage.removeItem('draft');
            toast.info('Draft saved successfully');
            return res;
        }
    } else {
        localStorage.setItem('draft', JSON.stringify(formData));
        store.save_as_login = true;
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

const get_results=async()=>{
    try {
        let res = await call('pwit.controllers.api.get_assistive_result', {
            doctype: title.value,
            session: store.session,
            user:auth.cookie.user_id!=='Guest'?auth.cookie.user_id:''
        })
        if(res.code===200){
            if(res.data){
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
    // get_results();
    let draft = JSON.parse(localStorage.getItem('draft') ?? '{}');
    if (Object.keys(draft).length) {
        if (auth.isLoggedIn) {
            await save_as_draft(draft);
        } else {
            initialData.value = draft;
        }
    }
    if (auth.isLoggedIn) {
        console.log('first')
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
