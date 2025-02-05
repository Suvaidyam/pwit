<template>
	<div class="h-screen">
		<Navbar v-if="!['ChangePass','ComingSoon'].includes(route.name)"/>
		<div class="pt-20 mx-auto max-w-[1700px] h-full">
			<router-view />
		</div>
	</div>
</template>


<script setup>
import Navbar from './components/Navbar.vue';
import {useRoute} from 'vue-router';

const route = useRoute();
</script>
