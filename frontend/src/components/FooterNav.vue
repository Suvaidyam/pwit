<template>
    <div class="flex flex-col md:flex-row justify-around md:justify-between items-center w-full px-4 md:px-8 lg:px-20 h-[72px] bg-[#578CC6]">
        <p class="text-white text-sm">
            © 2023 The Bridgespan Group. All rights reserved.
        </p>
        <div class="flex gap-6 items-center">
            <a href="#" class="text-white text-sm">
                <img class="w-6" src="../assets/Vector.png" alt="" srcset="">

            </a>
            <a href="#" class="text-white text-sm">
                <img class=" h-5" src="../assets/fb.png" alt="" srcset="">
            </a>
            <a href="#" class="text-white text-sm">
                <img class=" h-5" src="../assets/twiter.png" alt="" srcset="">
            </a>
            <a href="#" class="text-white text-sm">
                 <Instagram class="w-6"/>
            </a>
            <a href="#" class="text-white text-sm">
                 <img class=" h-5" src="../assets/linked.png" alt="" srcset="">
            </a>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import {Instagram} from 'lucide-vue-next'
</script>