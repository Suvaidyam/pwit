<template>
    <Menu as="div" class="relative inline-block text-left">
        <div>
            <MenuButton
                class="inline-flex w-full justify-center gap-x-1.5 rounded-full bg-white p-1 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
                <img v-if="auth?.cookie?.user_image" class="w-10 h-10 object-cover rounded-full" :src="auth?.cookie?.user_image"
                    alt="">
                <p class="w-10 h-10 flex items-center justify-center text-xl font-normal text-gray-600" v-else>{{
                    auth?.cookie?.full_name?.split('')[0] }}</p>
            </MenuButton>
        </div>

        <transition enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95">
            <MenuItems
                class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <div class="py-1">
                    <MenuItem v-slot="{ active }" @click="openDialog('profile')">
                    <a href="#"
                        :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'flex items-center gap-2 px-4 py-2 text-sm']">
                        <UserRound class="w-4 h-4 text-gray-400" /> Profile
                    </a>
                    </MenuItem>
                    <MenuItem v-slot="{ active }" @click="openDialog('change_pass')">
                    <a href="#"
                        :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'flex items-center gap-2 px-4 py-2 text-sm']">
                        <LockKeyhole class="w-4 h-4 text-gray-400" />Change Password
                    </a>
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                    <router-link to="/recommended"
                        :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'flex items-center gap-2 px-4 py-2 text-sm']">
                        <FileSearch2 class="w-4 h-4 text-gray-400" />View Previous Results
                    </router-link>
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                    <button type="button" @click="auth.logout()"
                        :class="[active ? 'bg-gray-100 text-gray-900 outline-none' : 'text-gray-700', 'flex items-center gap-2 w-full px-4 py-2 text-left text-sm']">
                        <LogOut class="w-4 h-4 text-gray-400" />Logout
                    </button>
                    </MenuItem>
                </div>
            </MenuItems>
        </transition>
    </Menu>
    <Profile />
    <ChangePassword/>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { ref, inject, watch } from 'vue'
import { UserRound, LockKeyhole, LogOut ,FileSearch2} from 'lucide-vue-next'
import Profile from './Profile.vue';
import ChangePassword from './ChangePassword.vue'
import { useRouter } from 'vue-router';

const auth = inject('$auth');
const store = inject('store');
const router = useRouter();
const openDialog = (el) => {
    if(el=='profile'){
        store.isOpen = true;
    }else{
        store.isOpenPas=true
    }
} 
watch(() => auth.cookie, (value) => {
    auth.cookie = value
});
</script>