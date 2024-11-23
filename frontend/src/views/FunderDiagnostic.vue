<template>
    <div class="w-full pt-6 h-screen">
        <div class="flex gap-2 px-4 md:px-8 lg:px-20">
            <p class="text-gray-800 text-sm">
                <router-link to="/">Home </router-link>
                <span class="text-gray-400">/ Funder Diagnostic</span>
            </p>
        </div>
        <h1 class="text-h2 px-4 md:px-8 lg:px-20 tracking-wide font-serif text-primary font-bold">
            Funder Diagnostic
        </h1>
        <p class="text-sm px-4 md:px-8 lg:px-20   font-serif text-sebase font-normal">
            Please select the degree to which your organization’s mindset and practices agree or disagree with the
            following statements:
        </p>
        <div class="w-full flex flex-col gap-4 px-4 md:px-8 lg:px-20 py-5 mt-4 bg-gray-50">
            <FormView  
                :doctype="'Funder Diagnostic'" 
                :onSubmit="handleSubmit"
                :isCard="true" 
                :isDraft="true" 
                :section="true"
                :save_as_draft="save_as_draft" 
            />
        </div>
        <FooterNav />
    </div>
</template>

<script setup>
import { ref ,inject} from 'vue';
import FooterNav from '../components/FooterNav.vue';
import { FormView } from '../../../../sva_form_vuejs/form_view.js';
import {useRouter} from 'vue-router';

const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const router = useRouter();

const handleSubmit = async (formData) => {
  try {
    const res = await call('frappe.desk.form.save.savedocs', {
      doc: JSON.stringify({
        doctype: 'Funder Diagnostic',
        ...formData
      }),
      action: 'Save'
    });
    if (res) {
      router.push('/recommended');
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

</script>
