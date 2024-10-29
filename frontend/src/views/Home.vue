<template>
	<div class="w-full h-screen">
		<div class="w-full flex flex-col gap-5 justify-center h-40 items-center">
			<h1 class="text-6xl text-primary">Assistive Funder Toolkit</h1>
			<p>Developed under the Pay-What-It-Takes India Initiative</p>
		</div>
		<div class="w-full bg-tatary px-20 py-6">
			<h4 class="text-center text-2xl">About the tool</h4>
			<p class="text-center">Philanthropy has a significant opportunity to amplify the impact of their grantmaking
				by enabling a
				stronger and more resilient nonprofit sector. Bridgespan’s Pay-What-ItTakes India Initiative has
				identified five principles of effective grantmaking, rooted in trust, that funders can adopt to support
				strong, resilient nonprofit partners. As funders recognize the importance of making grantmaking</p>
			<div class="flex gap-5 pt-14">
				<div class="w-56 h-32 rounded-md bg-white relative" v-for="item in data" :key="item.name">
					<div
						class="w-[70px] h-[70px] rounded-full border-8 border-blue-600 absolute left-1/3 -top-10 bg-white">
					</div>
				</div>
			</div>
			<p class="text-center pt-5">
				As funders recognize the importance of making grantmaking more supportive and inclusive, there is a need
				to pursue actionable strategies to advance on this journey. The Funder Practices Assistive Tool is an
				open-source and freely available tool to help assess how aligned your current funding practices are with
				the five PWIT principles and identify areas for further enhancement. Wherever you may be on your
				journey, the tool provides next steps and recommendations for how you can make your grantmaking
				practices more supportive and chart a path forward for more expansive forms of true cost investment.
			</p>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
const data = ref([{ name: 1 }, { name: 2 }, { name: 3 }, { name: 4 }, { name: 5 }])
</script>
