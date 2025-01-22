<template>
  <div class="w-full pt-6">
    <div class="flex justify-between px-4 md:px-8 lg:px-20">
      <div class="flex gap-2 items-center">
        <router-link to="/" class="flex items-center text-trbase gap-1">
          <House class="w-4 h-4" /> Home
        </router-link>|
        <div class="flex items-center cursor-pointer text-trbase" @click="router.back(-1)">
          <ArrowBigLeft class="w-5 " /> Back
        </div>
      </div>
      <div class="flex gap-3 justify-between ">
        <p class="w-16 py-1 flex items-center justify-center rounded-2xl text-red-700 bg-red-100 font-bold"
          v-if="Object.keys(initialData).length">Draft</p>
        <router-link v-if="viewResult" to="/recommended"
          class="border flex items-center gap-2 text-secondary border-[#255B97] rounded-md h-9 px-4 text-sm truncate">
          View Results
          <FileSearch2 class="w-4" />
        </router-link>
      </div>
    </div>
    <div class="flex flex-col md:flex-row md:items-center px-4 md:px-8 lg:px-20 justify-between">
      <div class="flex items-center gap-3">
        <h1 class="text-h2  tracking-wide font-primary text-primary font-bold">
          Funder Diagnostic
        </h1>
      </div>

    </div>
    <p class="text-h5 px-4 md:px-8 lg:px-20 font-primary text-sebase font-semibold">
      Please select the degree to which <span class="underline font-primary">your organisation’s</span> mindset and
      practices agree or disagree with the
      following statements:
    </p>
    <div class="w-full flex flex-col gap-4 px-4 md:px-8 lg:px-20">
      <!-- <div class=" w-full relative">
        <p class="absolute  w-full top-5 left-0 border-b-4 rounded-md border-[]"></p>
      </div> -->
      <FormView :section_hidden="true" :width="true" :isRow="true" :initialData="initialData"
        :doctype="'Funder Diagnostic'" :onSubmit="handleSubmit" :isCard="true" :isDraft="true" :isColumn="true"
        :section="true" :save_as_draft="save_as_draft" />
    </div>
    <!-- <FooterNav /> -->
  </div>
</template>

<script setup>
import { ref, inject, onMounted } from 'vue';
import FooterNav from '../components/FooterNav.vue';
import { FormView } from '@@/form_view.js';
import { useRouter } from 'vue-router';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
import { FileSearch2, ArrowBigLeft, House } from 'lucide-vue-next';

const store = inject('store');
const auth = inject('$auth');
const call = inject('$call');
const router = useRouter();
const initialData = ref({});
const viewResult = ref(false);
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
      sessionStorage.removeItem('draft');
      toast.info('Draft saved successfully');
      get_save_as_draft()
      return res;
    }
  } else {
    sessionStorage.setItem('draft', JSON.stringify(formData));
    store.save_as_login = true;
  }
}
onMounted(async () => {
  let draft = JSON.parse(sessionStorage.getItem('draft') ?? '{}');
  if (Object.keys(draft).length) {
    if (auth.isLoggedIn) {
      await save_as_draft(draft);
    }
  }
  if (auth.isLoggedIn) {
    get_save_as_draft();
  }
  let res = await call('pwit.controllers.api.get_results', {
    doctype: 'Funder Diagnostic',
    session: store.session,
    user: auth.cookie.user_id !== 'Guest' ? auth.cookie.user_id : ''
  })
  if (res.code === 200 && Object.keys(res.data).length) {
    viewResult.value = true;
  }
})

</script>
