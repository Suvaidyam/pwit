<template>
    <Popover v-slot="{ open }" class="relative z-20">
        <PopoverButton @mouseenter="open = true" @mouseleave="open = false" class="focus:outline-none">
            <InfoIcon class="w-4 h-4 text-gray-400 hover:text-gray-600 dark:text-gray-500 dark:hover:text-gray-300" />
        </PopoverButton>
        <transition enter-active-class="transition duration-200 ease-out" enter-from-class="opacity-0 translate-y-1"
            enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
            <PopoverPanel class="absolute z-10 w-[500px] min-w-[500px] px-4 mt-3 transform -translate-x-1/2 left-1/2 sm:px-0 lg:max-w-3xl"
                @mouseenter="open = true" @mouseleave="open = false">
                <div class="overflow-hidden border shadow-blue-300 border-blue-600 rounded-lg shadow-md ring-1 ring-black ring-opacity-5">
                    <div class="p-4 bg-white dark:bg-gray-800">
                        <p class="text-sm text-gray-700 dark:text-gray-300">
                            {{ props.content }}
                        </p>
                    </div>
                </div>
            </PopoverPanel>
        </transition>
    </Popover>
</template>

<script setup>
import {InfoIcon} from 'lucide-vue-next'
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'

const props = defineProps({
    title: {
        type: String,
        required: false
    },
    content: {
        type: String,
        required: true
    }
})
</script>