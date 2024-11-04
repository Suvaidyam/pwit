<template>
    <Menu as="div" class="relative inline-block text-left">
        <div>
            <MenuButton
                class="inline-flex w-full justify-center gap-x-1.5 rounded-full bg-white p-1 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                <img v-if="auth?.cookie?.user_image" class="w-10 h-10 rounded-full" :src="auth?.cookie?.user_image" alt="">
                <p class="w-10 h-10 flex items-center justify-center text-xl text-gray-600" v-else>{{ auth?.cookie?.full_name?.split('')[0] }}</p>
            </MenuButton>
        </div>

        <transition enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95">
            <MenuItems
                class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div class="py-1">
                    <MenuItem v-slot="{ active }">
                    <a href="#"
                        :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'block px-4 py-2 text-sm']">Account
                        settings</a>
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                    <button type="button" @click="auth.logout()"
                        :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'block w-full px-4 py-2 text-left text-sm']">Sign
                        out</button>
                    </MenuItem>
                </div>
            </MenuItems>
        </transition>
    </Menu>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { ref, inject, watch } from 'vue'

const auth = inject('$auth');

watch(() => auth.cookie, (value) => {
    auth.cookie = value
});
</script>