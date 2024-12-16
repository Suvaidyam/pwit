<template>
    <Popper>
      <button class="text-trbase"><InfoIcon class="w-4"/></button>
      <template #content>
        <div>This is the Popper content</div>
      </template>
    </Popper>
  </template>

<script setup>
import {InfoIcon} from 'lucide-vue-next'
import Popper from "vue3-popper";

const props = defineProps({
    title: {
        type: String,
        required: false
    },
    content: {
        type: String,
        required: true
    },
    link: {
        type: String,
        required: false
    }
})
</script>