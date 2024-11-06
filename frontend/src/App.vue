<template>
	<div class="h-screen">
		<Navbar />
		<div class="pt-20 mx-auto max-w-[1700px] h-full">
			<router-view />
		</div>
	</div>
</template>


<script setup>
import Navbar from './components/Navbar.vue';
</script>
