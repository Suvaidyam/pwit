<template>
    <div class="w-full px-4 md:px-8 lg:px-20 h-16 flex justify-between items-center shadow-md">
        <router-link to="/" class="text-2xl font-bold text-primary">LOGO</router-link>
        <div class="flex gap-3 text-sm">
           <Register/>
           <Login/>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import Login from './Login.vue'
import Register from './Register.vue'
</script>