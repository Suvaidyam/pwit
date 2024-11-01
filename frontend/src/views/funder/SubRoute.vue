<template>
    <div class="flex">
        <LeftNav />
        <div class="md:pl-56">
            <router-view />
        </div>
    </div>
</template>

<script setup>
import LeftNav from '../../components/LeftNav.vue';
</script>