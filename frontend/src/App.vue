<template>
	<div>
		<Navbar />
		<div class="pt-16">
			<router-view />
		</div>
	</div>
</template>


<script setup>
import Navbar from './components/Navbar.vue';
</script>
