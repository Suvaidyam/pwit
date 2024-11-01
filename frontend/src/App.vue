<template>
	<div>
		<Navbar />
		<div class="pt-16 mx-auto max-w-[1700px]">
			<router-view />
		</div>
	</div>
</template>


<script setup>
import Navbar from './components/Navbar.vue';
</script>
