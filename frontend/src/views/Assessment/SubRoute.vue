<template>
    <div class="flex w-full h-full">
        <LeftNav />
        <div class="md:pl-60 md:pr-8 lg:pr-20 w-full h-full">
            <router-view />
        </div>
    </div>
</template>

<script setup>
import LeftNav from './LeftNav.vue';
</script>