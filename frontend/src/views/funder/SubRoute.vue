<template>
    <div class="flex">
        <LeftNav />
        <div class="pl-52">
            <router-view />
        </div>
    </div>
</template>

<script setup>
import LeftNav from '../../components/LeftNav.vue';
</script>