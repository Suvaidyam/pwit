<template>
    <div class="flex flex-col md:flex-row justify-around md:justify-between items-center w-full px-4 md:px-8 lg:px-20 h-16 bg-blue-500">
        <p class="text-white text-sm">
            © 2023 The Bridgespan Group. All rights reserved.
        </p>
        <div class="flex gap-4">
            <a href="#" class="text-white text-sm">
                <Youtube class="w-5 h-5" />
            </a>
            <a href="#" class="text-white text-sm">
                <Facebook class="w-5 h-5" />
            </a>
            <a href="#" class="text-white text-sm">
                <Twitter class="w-5 h-5" />
            </a>
            <a href="#" class="text-white text-sm">
                <Instagram class="w-5 h-5" />
            </a>
            <a href="#" class="text-white text-sm">
                <Linkedin class="w-5 h-5" />
            </a>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import {Instagram ,Youtube,Facebook,Twitter,Linkedin} from 'lucide-vue-next'
</script>