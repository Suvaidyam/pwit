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
import { ref, watch,inject, onMounted } from 'vue'
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

watch(route, (newVal, oldVal) => {
    title.value = splitAtSecondCapital(newVal.name)
    current_path.value = oldVal.path
})
const handleSubmit = async (formData) => {
  try {
    const res = await call('pwit.controllers.api.save_doc', { doctype: title.value, doc: {...formData,'session':store.session} });
    if (res.code === 200) {
      router.push(`${current_path.value}/results`);
    }
  } catch (err) {
    console.error('Error saving form:', err);
  } 
};
const save_as_draft = () => {
    if(auth.isLoggedIn){
        console.log('save as draft');
    }else{
        store.save_as_login = true;
    } 
}
const get_save_as_draft = async() => {
    try {
        let res = await call('pwit.controllers.api.get_save_as_draft', { doctype: title.value, user:auth.cookie.user_id });
        console.log(res)
    } catch (error) {
        
    }
}
onMounted(() => {
    if(auth.isLoggedIn){
        get_save_as_draft();
    }
})
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
