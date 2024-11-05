<template>
    <div class="flex w-full">
        <LeftNav />
        <div class="md:pl-60 md:pr-8 lg:pr-20 w-full">
            <router-view />
        </div>
    </div>
</template>

<script setup>
import LeftNav from './LeftNav.vue';
</script>