<template>
	<div class="w-full h-screen">
		<div class="w-full flex flex-col gap-5 justify-center h-40 items-center">
			<h1 class="text-xl font-bold md:text-4xl lg:text-6xl text-primary">Assistive Funder Toolkit</h1>
			<p class="px-4 text-center font-extrabold text-[#4f4f4f] text-xl">Developed under the Pay-What-It-Takes India Initiative</p>
		</div>
		<!--  -->
		<div class="w-full bg-tatary px-4 md:px-8 lg:px-20 py-6">
			<h4 class="text-center text-3xl font-medium">About the tool</h4>
			<p class="text-center text-sm font-medium text-tatary">Philanthropy has a significant opportunity to amplify
				the impact of their grantmaking
				by enabling a
				stronger and more resilient nonprofit sector. Bridgespan’s Pay-What-ItTakes India Initiative has
				identified five principles of effective grantmaking, rooted in trust, that funders can adopt to support
				strong, resilient nonprofit partners. As funders recognize the importance of making grantmaking</p>
			<div
				class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-y-12 gap-x-5 pt-14">
				<div class="h-36 rounded-md bg-white relative" v-for="item in data" :key="item.name">
					<div
						class="w-[70px] h-[70px] rounded-full border-8 border-blue-600 absolute left-[40%] sm:left-[38%] md:left-[36%] lg:left-[36%] -top-10 bg-white">
					</div>
				</div>
			</div>
			<p class="text-center pt-5 text-sm font-medium text-tatary">
				As funders recognize the importance of making grantmaking more supportive and inclusive, there is a need
				to pursue actionable strategies to advance on this journey. The Funder Practices Assistive Tool is an
				open-source and freely available tool to help assess how aligned your current funding practices are with
				the five PWIT principles and identify areas for further enhancement. Wherever you may be on your
				journey, the tool provides next steps and recommendations for how you can make your grantmaking
				practices more supportive and chart a path forward for more expansive forms of true cost investment.
			</p>
		</div>
		<!--  -->
		<div class=" w-full px-4 md:px-8 lg:px-20 py-10 ">
			<h1 class="text-primary text-3xl font-semibold">What does the toolkit include?</h1>
			<div class="flex flex-col md:flex-row">
				<div class="w-full flex flex-col gap-3">
					<p class="pt-2 text-sm font-medium text-tatary">The tool is designed for institutional funders
						(global, domestic, CSR) who are seeking a deeper understanding of how they can strengthen their
						own
						grantmaking practices to effectively and meaningfully support their nonprofit partners. It may
						also
						be used by advisors/ intermediaries who work closely with institutional donors, and leverage
						this
						tool to provide more targeted support to strengthen the impact of their grantmaking. The tool
						helps
						do this through a two-step approach:</p>
					<div class="flex flex-col gap-5">
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 2 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Use these guides to map your current practices on the five PWIT principles, across
									various elements spanning policy, approaches, communication, etc., to understand the
									strengths and gaps in your funding practices. The guides for most principles are
									rubric-based to accurately identify incremental shifts towards improving your
									practices. Given the nascent stage of DEI practices in India, the DEI guide takes a
									different form to allow you to reflect on how inclusive your grantmaking practices
									are. At the end, you will receive a summary report with recommendations and relevant
									resources that may be useful to move forward on your journey.
								</p>
							</div>
						</div>
					</div>
				</div>
				<div class="w-full h-96 flex md:justify-end">
					<img class="w-[90%]" src="https://s3-alpha-sig.figma.com/img/fd5f/3676/ae1cb6c025ff0ce6cf4fa11682c74551?Expires=1731283200&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=ZW6YxqY7dSwIZ8GcQEHIRcC5A6T~oxGg3xLqCHv~A4GnVxUXMPH0~zqEVie0xR8XE6v~xkAcnOQwPjYWQtnZZdzCAi95WlikIUs7Mi9egCHfQoR3jwa39DROeFzacjayYTjm52~~lVyrHU7MwUbQNl08iJffpYI-kSC6vvgZG9yrBsrxdGBq48R0pr0aOyh5vuosUR2m9ppiCGU1xp9xTQkd44WKCd3GbP1gobxI5KDEzuf2Q6meVTpJi9BAu-MCFgWzQg40PovT6vcjaAQlcoWWmnOEV2HJHtP3WriZJE94CFcMVOQULVSKxDIE3NfLFGGCBc87Lh9zSwc5Ul-FIw__" alt="">
				</div>
			</div>
		</div>
		<!--  -->
		<div class=" w-full px-4 md:px-8 lg:px-20  md:py-10 ">
			<div class="flex flex-col md:flex-row">
				<div class="w-full pt-8   md:order-1">
					<img class="w-[90%] " src="https://s3-alpha-sig.figma.com/img/834b/f517/79c7b44475375a1dc3f5a0e6e046517c?Expires=1731283200&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=IpJtiWqr53iUZULdXroP4U58t4RSnDxGIAnfkiPwd5TLR-J0C9AMkmY58yjqWYVCFrvx3GwVxHz33GGNxHbpf5clOSXcICECCmmejjuDN~x9zU3kJKWM9W7-mfmZowuA9vqTTihh6zeV7~vWfQjVk4NitQ86fLOD-IxCArckkPDM37ReIGHHKAXAoaKFJgW8G7wGuJmg4Yb3zSoXonUAUra56ivgkkhwHNpb9qH9ryJTK12LtVK6TYpU10ogRG8yE6NK9xbZczT~oBt4UhV4gz-6cFxwEwFbNsekpm22BuXC5NscJXODhG4audPfPO3jVJeJZAsDm8Yfa--QB4Oc-Q__" alt="">
				</div>
				<div class="w-full flex flex-col gap-3 order-1 md:order-2">
					<h1 class="text-primary  text-3xl font-semibold">What does the toolkit include?</h1>
					<div class="flex flex-col gap-5">
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
						<div class="flex gap-4">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
							</div>
							<div class="">
								<h4 class="font-semibold text-sm">Part 1 - Funding practices diagnostic</h4>
								<p class="text-tatary text-xs">
									Take a quick diagnostic of your organization’s funding beliefs and practices to
									identify specific principles that would be most relevant for you to enhance your
									grantmaking.
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!--  -->
		<div class="w-full flex justify-center py-6 px-4">
			<button class="bg-secondary text-white w-96 py-3 text-sm font-semibold rounded-md">Start the Assessment
			</button>
		</div>
		<FooterNav/>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import FooterNav from '../components/FooterNav.vue';
const data = ref([{ name: 1 }, { name: 2 }, { name: 3 }, { name: 4 }, { name: 5 }])
</script>
