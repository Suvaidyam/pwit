<template>
  <div class="w-full pt-6">
    <div class="flex gap-2 px-4 md:px-8 lg:px-20">
      <p class="text-gray-800 text-sm">
        <router-link to="/">Home </router-link>
        <span class="text-gray-400">/ Funder Diagnostic</span>
      </p>
    </div>
    <div class="flex items-center px-4 md:px-8 lg:px-20 gap-3">
      <h1 class="text-h2  tracking-wide font-primary text-primary font-bold">
        Funder Diagnostic
      </h1>
      <p class="w-16 py-1 flex items-center justify-center rounded-2xl text-red-700 bg-red-100 font-bold"
        v-if="Object.keys(initialData).length">Draft</p>
    </div>
    <p class="text-h5 px-4 md:px-8 lg:px-20 font-primary text-sebase font-bold">
      Please select the degree to which your organization’s mindset and practices agree or disagree with the
      following statements:
    </p>
    <div class="w-full flex flex-col gap-4 px-4 md:px-8 lg:px-20 mt-4 ">
      <FormView :isRow="true" :initialData="initialData" :doctype="'Funder Diagnostic'" :onSubmit="handleSubmit" :isCard="true"
        :isDraft="true" :section="true" :save_as_draft="save_as_draft" />
    </div>
    <!-- <FooterNav /> -->
  </div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue';
import FooterNav from '../components/FooterNav.vue';
import { FormView } from '../../../../sva_form_vuejs/form_view.js';
import { useRouter } from 'vue-router';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const router = useRouter();
const initialData = ref({});
const handleSubmit = async (formData) => {
  try {
    const res = await call('pwit.controllers.api.save_doc', { doctype: 'Funder Diagnostic', doc: { ...formData, 'session': store.session }, name: initialData.value.name });
    if (res.code === 200) {
      router.push('/recommended');
    }
  } catch (err) {
    console.error('Error saving form:', err);
  }
};

const get_save_as_draft = async () => {
  try {
    let res = await call('pwit.controllers.api.get_save_as_draft', { doctype: 'Funder Diagnostic', user: auth.cookie.user_id });
    if (res.code === 200) {
      initialData.value = res.data;
    }
  } catch (error) {

  }
}

const save_as_draft = async (formData) => {
  if (auth.isLoggedIn) {
    const res = await call('pwit.controllers.api.save_as_draft', { doctype: 'Funder Diagnostic', doc: { ...formData, 'session': store.session }, name: initialData?.value?.name });
    if (res.code === 200) {
      localStorage.removeItem('draft');
      toast.success('Draft saved successfully');
      get_save_as_draft()
      return res;
    }
  } else {
    localStorage.setItem('draft', JSON.stringify(formData));
    store.save_as_login = true;
  }
}
onMounted(async () => {
  let draft = JSON.parse(localStorage.getItem('draft') ?? '{}');
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
