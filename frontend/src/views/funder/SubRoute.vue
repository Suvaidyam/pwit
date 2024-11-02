<template>
    <div class="flex w-full">
        <LeftNav />
        <div class="md:pl-60 w-full">
            <router-view />
        </div>
    </div>
</template>

<script setup>
import LeftNav from '../../components/LeftNav.vue';
</script>