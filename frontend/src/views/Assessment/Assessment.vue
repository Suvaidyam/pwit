<template>
    <div class="p-4 w-full h-screen">
        <Breadcrumb />
        <h1 class="text-h2 font-serif font-semibold text-primary">{{ title }}</h1>
        <transition name="fade" mode="out-in">
            <div  class="w-full h-full">
               <FormView v-if="title!=='Diversity Equity Inclusion'"
                    :doctype="title"
                    :onSubmit="handleSubmit" 
                    :isTable="true" 
                    :isDraft="true" 
                    :section="true"
                    :save_as_draft="save_as_draft"
                    :key="title" 
                />
               <FormView v-if="title=='Diversity Equity Inclusion'"
                    :doctype="title"
                    :onSubmit="handleSubmit" 
                    :isDraft="true" 
                    :isCard="true" 
                    :section="true"
                    :save_as_draft="save_as_draft"
                    :key="title" 
                />
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, watch,inject } from 'vue'
import { useRoute ,useRouter} from 'vue-router';
import Breadcrumb from './Breadcrumb.vue'
import {FormView} from '../../../../../sva_form_vuejs/form_view';

const route = useRoute()
const router = useRouter()
const current_path = ref(route.fullPath)
const title = ref(splitAtSecondCapital(route.name));
const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const cur_session = JSON.parse(localStorage.getItem('session'));

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    current_path.value = oldVal.path
})
const handleSubmit = async (formData) => {
  try {
    const res = await call('pwit.controllers.api.save_doc', { doctype: title.value, doc: {...formData,'session':cur_session.data.name} });
    if (res.code === 200) {
      router.push(`${current_path}/results`);
    }
  } catch (err) {
    console.error('Error saving form:', err);
  } 
};
const save_as_draft = () => {
    if(auth.isLoggedIn){
        console.log('save as draft');
    }else{
        store.auth = 'Log In';
    } 
}

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
