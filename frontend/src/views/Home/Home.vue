<template>
	<div class="w-full h-screen">
		<div
			class="w-full px-4 md:px-8 lg:px-20 flex flex-col gap-2 md:gap-3 justify-center h-24 md:h-40 items-center ">
			<h1 class="text-h2 font-bold lg:text-[64px] text-primary font-primary leading-[70.4px]">Assistive Funder
				Toolkit
			</h1>
			<p class="px-4 text-center font-bold text-[#464547] leading-4 tracking-wide text-h5 font-primary">
				Developed by
				the
				Pay-What-It-Takes India Initiative</p>
		</div>
		<!--  -->
		<div class="w-full bg-tatary px-4 md:px-8 lg:px-20 py-6 mt-7">
			<h4 class="text-center text-h2 font-bold text-[#21272A] my-6 font-primary tracking-wide leading-9">About the
				tool</h4>
			<div class="flex justify-center font-normal text-sebase text-h5 text-center tracking-wider leading-5">
				<p>Philanthropy has a significant opportunity to amplify the impact of their grantmaking by enabling a
					stronger and more resilient nonprofit sector. <a
						href="https://www.bridgespan.org/our-global-reach/pay-what-it-takes-india-initiative"
						class="text-secondary hover:underline"> Bridgespan’s Pay-What-ItTakes India Initiative</a> has
					identified five principles of effective grantmaking, rooted in trust, that funders can adopt to
					support
					strong, resilient nonprofit partners.</p>
			</div>

			<div
				class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-y-12 gap-x-3 pt-14">
				<div class="h-[160px] flex rounded-md bg-white relative px-4 ">
					<div
						class="w-[70px] h-[70px] rounded-full border-8  tracking-wider border-[#59467b] absolute left-[40%] sm:left-[38%] md:left-[36%] lg:left-[36%] -top-10 bg-white flex justify-center items-center">
						<Handshake class="w-7 h-7" />
					</div>
					<div class="flex flex-col justify-around gap-2 pt-10 pb-4">
						<p class="text-[#42217c] text-center font-bold text-h5 uppercase tracking-wider leading-4">
							Develop Multiyear Funder-Nonprofit Partnerships
						</p>
						<p class="text-h6 text-center leading-3 font-bold ">Partner for the long term and build mutual
							trust with NGOs</p>
					</div>

				</div>
				<div class="h-[160px] flex justify-center rounded-md bg-white relative px-4 ">
					<div
						class="w-[70px] h-[70px] rounded-full border-8 border-[#136096] absolute left-[40%] sm:left-[38%] md:left-[36%] lg:left-[36%] -top-10 bg-white flex justify-center items-center">
						<IndianRupee class="w-7 h-7" />
					</div>
					<div class="flex flex-col justify-around gap-2 pt-10 pb-4">
						<p class="text-[#136096] text-center font-bold text-h5 uppercase  tracking-wider leading-4">
							Pay a fair share of core costs
						</p>
						<p class="text-h6 font-bold text-center leading-3">Cover NGOs' expenses for day-to-day
							operations</p>
					</div>

				</div>
				<div class="h-[160px] flex justify-center rounded-md bg-white relative px-4">
					<div
						class="w-[70px] h-[70px] rounded-full border-8 border-[#029fd9] absolute left-[40%] sm:left-[38%] md:left-[36%] lg:left-[36%] -top-10 bg-white flex justify-center items-center">
						<ChartNoAxesCombined class="w-7 h-7" />
					</div>
					<div class="flex flex-col gap-2 justify-around pt-10 pb-4">
						<p class="text-[#029fd9] text-center font-bold text-h5 uppercase  tracking-wider leading-4">
							Invest in organisational development
						</p>
						<p class="text-h6 font-bold text-center leading-3">Support NGOs' growth in key areas</p>
					</div>
				</div>
				<div class="h-[160px] flex rounded-md bg-white relative px-4">
					<div
						class="w-[70px] h-[70px] rounded-full border-8 border-[#058248] absolute left-[40%] sm:left-[38%] md:left-[36%] lg:left-[36%] -top-10 bg-white flex justify-center items-center">
						<PiggyBank class="w-7 h-7" />
					</div>
					<div class="flex flex-col gap-2 justify-around pt-10 pb-4">
						<p class="text-[#058248] text-center font-bold text-h5 uppercase  tracking-wider leading-4">
							Build Financial Resilience
						</p>
						<p class="text-h6 font-bold text-center leading-3">Contribute to reserves, or corpus, that
							provide a safety net for NGOs</p>
					</div>
				</div>
				<div class="h-[160px] flex rounded-md bg-white relative px-4 ">
					<div
						class="w-[70px] h-[70px] rounded-full border-8 border-[#f38714] absolute left-[40%] sm:left-[38%] md:left-[36%] lg:left-[36%] -top-10 bg-white flex justify-center items-center">
						<Scale class="w-7 h-7" />
					</div>
					<div class="flex flex-col gap-2 justify-around pt-10 pb-4">
						<p class="text-[#f38714] text-center font-bold text-h5 uppercase  tracking-wider leading-4 ">
							Embed Diversity Equity, and inclusion in grantmaking
						</p>
						<p class="text-h6 leading-3 font-bold text-center">Recognize and address the needs of
							underserved individuals and communities</p>
					</div>
				</div>

			</div>

			<div class="flex justify-center md:px-8 text-h5 py-8 font-normal tracking-wider ">
				As funders recognize the importance of making grantmaking more supportive and inclusive, there is a need
				to pursue actionable strategies to advance on this journey. The Funder Practices Assistive Tool is an
				open-source and freely available tool to help assess how aligned your current funding practices are with
				the five PWIT principles and identify areas for further enhancement. Wherever you may be on your
				journey, the tool provides next steps and recommendations for how you can make your grantmaking
				practices more supportive and chart a path forward for more expansive forms of true cost investment.
			</div>
		</div>
		<!--  -->
		<div class=" w-full px-4 md:px-8 lg:px-20 py-10 ">
			<h1 class="text-primary text-h2 font-bold leading-9 tracking-wide font-primary">What does the toolkit
				include?
			</h1>
			<div class="flex flex-col md:flex-row mt-5">
				<div class="w-full flex flex-col gap-3">
					<p class="pt-2 text-h5 font-normal text-trbase text-justify leading-5 tracking-wider">The tool is
						designed for institutional
						funders
						(global, domestic, CSR) who are seeking a deeper understanding of how they can strengthen their
						own
						grantmaking practices to effectively and meaningfully support their nonprofit partners. It may
						alsofont-sans
						be used by advisors/ intermediaries who work closely with institutional donors, and leverage
						this
						tool to provide more targeted support to strengthen the impact of their grantmaking. The tool
						helps
						do this through a two-step approach:</p>
					<div class="flex flex-col gap-5 mt-3">
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="18" height="20" viewBox="0 0 18 20" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path fill-rule="evenodd" clip-rule="evenodd"
										d="M1.172 1.172C-1.19209e-07 2.343 0 4.229 0 8V12C0 15.771 -1.19209e-07 17.657 1.172 18.828C2.344 19.999 4.229 20 8 20H10C13.771 20 15.657 20 16.828 18.828C17.981 17.676 18 15.832 18 12.18L15.182 14.998C14.912 15.268 14.691 15.489 14.442 15.684C14.1499 15.9128 13.8333 16.1083 13.498 16.267C13.1911 16.4051 12.8758 16.5236 12.554 16.622L10.242 17.393C9.87498 17.5154 9.48113 17.5332 9.10458 17.4443C8.72804 17.3554 8.38368 17.1635 8.11011 16.8899C7.83654 16.6163 7.64456 16.272 7.5557 15.8954C7.46684 15.5189 7.4846 15.125 7.607 14.758L7.881 13.938L8.356 12.512L8.377 12.446C8.498 12.084 8.597 11.788 8.733 11.502C8.893 11.166 9.08733 10.8517 9.316 10.559C9.511 10.309 9.732 10.089 10.002 9.819L14.008 5.812L15.12 4.7L15.247 4.573C15.5868 4.23215 15.9907 3.96188 16.4353 3.77773C16.88 3.59358 17.3567 3.49919 17.838 3.5C17.687 2.47 17.394 1.737 16.828 1.172C15.657 -1.19209e-07 13.771 0 10 0H8C4.229 0 2.343 -1.19209e-07 1.172 1.172ZM4.25 7C4.25 6.80109 4.32902 6.61032 4.46967 6.46967C4.61032 6.32902 4.80109 6.25 5 6.25H11.5C11.6989 6.25 11.8897 6.32902 12.0303 6.46967C12.171 6.61032 12.25 6.80109 12.25 7C12.25 7.19891 12.171 7.38968 12.0303 7.53033C11.8897 7.67098 11.6989 7.75 11.5 7.75H5C4.80109 7.75 4.61032 7.67098 4.46967 7.53033C4.32902 7.38968 4.25 7.19891 4.25 7ZM4.25 11C4.25 10.8011 4.32902 10.6103 4.46967 10.4697C4.61032 10.329 4.80109 10.25 5 10.25H7.5C7.69891 10.25 7.88968 10.329 8.03033 10.4697C8.17098 10.6103 8.25 10.8011 8.25 11C8.25 11.1989 8.17098 11.3897 8.03033 11.5303C7.88968 11.671 7.69891 11.75 7.5 11.75H5C4.80109 11.75 4.61032 11.671 4.46967 11.5303C4.32902 11.3897 4.25 11.1989 4.25 11ZM4.25 15C4.25 14.8011 4.32902 14.6103 4.46967 14.4697C4.61032 14.329 4.80109 14.25 5 14.25H6.5C6.69891 14.25 6.88968 14.329 7.03033 14.4697C7.17098 14.6103 7.25 14.8011 7.25 15C7.25 15.1989 7.17098 15.3897 7.03033 15.5303C6.88968 15.671 6.69891 15.75 6.5 15.75H5C4.80109 15.75 4.61032 15.671 4.46967 15.5303C4.32902 15.3897 4.25 15.1989 4.25 15Z"
										fill="#27853F" />
								</svg>
							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide">Part 1 -
									Funding practices
									diagnostic</h4>
								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.one" key="text" class="inline">
												Take a quick diagnostic of your organization’s funding beliefs and
												practices to identify specific principles
												that would be most relevant for you to enhance your grantmaking.
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold transition-all duration-300 ease-in-out"
											@click="readmore.one = !readmore.one">
											{{ readmore.one ? 'Read Less' : 'Read More' }}
										</span>
									</transition>
								</div>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<g clip-path="url(#clip0_248_5487)">
										<path fill-rule="evenodd" clip-rule="evenodd"
											d="M14.25 2.5C14.25 2.4337 14.2237 2.37011 14.1768 2.32322C14.1299 2.27634 14.0663 2.25 14 2.25H7C6.27065 2.25 5.57118 2.53973 5.05546 3.05546C4.53973 3.57118 4.25 4.27065 4.25 5V19C4.25 19.7293 4.53973 20.4288 5.05546 20.9445C5.57118 21.4603 6.27065 21.75 7 21.75H17C17.7293 21.75 18.4288 21.4603 18.9445 20.9445C19.4603 20.4288 19.75 19.7293 19.75 19V9.147C19.75 9.0807 19.7237 9.01711 19.6768 8.97022C19.6299 8.92334 19.5663 8.897 19.5 8.897H15C14.8011 8.897 14.6103 8.81798 14.4697 8.67733C14.329 8.53668 14.25 8.34591 14.25 8.147V2.5ZM15 12.25C15.1989 12.25 15.3897 12.329 15.5303 12.4697C15.671 12.6103 15.75 12.8011 15.75 13C15.75 13.1989 15.671 13.3897 15.5303 13.5303C15.3897 13.671 15.1989 13.75 15 13.75H9C8.80109 13.75 8.61032 13.671 8.46967 13.5303C8.32902 13.3897 8.25 13.1989 8.25 13C8.25 12.8011 8.32902 12.6103 8.46967 12.4697C8.61032 12.329 8.80109 12.25 9 12.25H15ZM15 16.25C15.1989 16.25 15.3897 16.329 15.5303 16.4697C15.671 16.6103 15.75 16.8011 15.75 17C15.75 17.1989 15.671 17.3897 15.5303 17.5303C15.3897 17.671 15.1989 17.75 15 17.75H9C8.80109 17.75 8.61032 17.671 8.46967 17.5303C8.32902 17.3897 8.25 17.1989 8.25 17C8.25 16.8011 8.32902 16.6103 8.46967 16.4697C8.61032 16.329 8.80109 16.25 9 16.25H15Z"
											fill="#27853F" />
										<path
											d="M15.75 2.82396C15.75 2.63996 15.943 2.52296 16.086 2.63796C16.2073 2.73596 16.315 2.84996 16.409 2.97996L19.422 7.17696C19.49 7.27296 19.416 7.39696 19.298 7.39696H16C15.9337 7.39696 15.8701 7.37062 15.8232 7.32373C15.7763 7.27685 15.75 7.21326 15.75 7.14696V2.82396Z"
											fill="#27853F" />
									</g>
									<defs>
										<clipPath id="clip0_248_5487">
											<rect width="24" height="24" fill="white" />
										</clipPath>
									</defs>
								</svg>
							</div>
							<div class="">
								<h4 class="font-bold text-sebase text-h5 font-primary leading-4 tracking-wide">Part 2 –
									Assistive guides for each
									principle</h4>
								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.two" key="text" class="inline">
												Use these guides to map your current practices on the five
												PWIT principles, across
												various elements spanning policy, approaches, communication, etc., to
												understand
												the
												strengths and gaps in your funding practices. The guides for most
												principles are
												rubric-based to accurately identify incremental shifts towards improving
												your
												practices. Given the nascent stage of DEI practices in India, the DEI
												guide
												takes a
												different form to allow you to reflect on how inclusive your grantmaking
												practices
												are. At the end, you will receive a summary report with recommendations
												and
												relevant
												resources that may be useful to move forward on your journey.
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold transition-all duration-300 ease-in-out"
											@click="readmore.two = !readmore.two">
											{{ readmore.two ? 'Read Less' : 'Read More' }}
										</span>
									</transition>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="w-full md:h-96 flex md:justify-end">
					<img class="w-[520px] h-[338px]" src="../../assets/right.png" alt="">
				</div>
			</div>
		</div>
		<!--  -->
		<div class=" w-full px-4 md:px-8 lg:px-20  md:pt-8 ">
			<div class="flex flex-col md:flex-row">
				<div class="w-full pt-8 flex justify-center items-center order-2 md:order-1">
					<img class="w-[434px] h-[436px]" src="../../assets/left.png" alt="">
				</div>
				<div class="w-full flex flex-col gap-3 order-1 md:order-2">
					<h1 class="text-primary text-h2 font-bold font-primary leading-9 tracking-wide">What will the output
						include?</h1>
					<div class="flex flex-col gap-5">
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<g clip-path="url(#clip0_248_5499)">
										<path
											d="M6 4V8H18V4H20.007C20.555 4 21 4.445 21 4.993V21.007C20.9997 21.2703 20.895 21.5227 20.7089 21.7089C20.5227 21.895 20.2703 21.9997 20.007 22H3.993C3.72964 22 3.47707 21.8954 3.29084 21.7092C3.10462 21.5229 3 21.2704 3 21.007V4.993C3 4.445 3.445 4 3.993 4H6ZM9 17H7V19H9V17ZM9 14H7V16H9V14ZM9 11H7V13H9V11ZM16 2V6H8V2H16Z"
											fill="#27853F" />
									</g>
									<defs>
										<clipPath id="clip0_248_5499">
											<rect width="24" height="24" fill="white" />
										</clipPath>
									</defs>
								</svg>

							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide">Optional
									Survey Before Accessing
									Guides
								</h4>
								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2  leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.three" key="text" class="inline">
												Visit <a href="http://pwit.localhost:8080/pwit/funder"
													class="text-secondary hover:underline">Funder Diagnostic Link </a>
												and fill
												out
												the short survey before proceeding to the principle-specific
												assistive guides,
												to understand which principles might be most relevant for you. You may
												feel free
												to
												skip this part and proceed directly to the guides.
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold transition-all duration-300 ease-in-out"
											@click="readmore.three = !readmore.three">
											{{ readmore.three ? 'Read Less' : 'Read More' }}
										</span>
									</transition>
								</div>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="20" height="22" viewBox="0 0 20 22" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path
										d="M12.5 0.5V5.75C12.5 6.34674 12.7371 6.91903 13.159 7.34099C13.581 7.76295 14.1533 8 14.75 8H20V19.25C20 19.8467 19.7629 20.419 19.341 20.841C18.919 21.2629 18.3467 21.5 17.75 21.5H11.9945C13.5909 20.3803 14.7391 18.7314 15.2354 16.8457C15.7318 14.96 15.5442 12.9595 14.7059 11.199C13.8676 9.43845 12.4328 8.03175 10.6561 7.2284C8.87936 6.42506 6.87551 6.27701 5 6.8105V2.75C5 2.15326 5.23705 1.58097 5.65901 1.15901C6.08097 0.737053 6.65326 0.5 7.25 0.5H12.5ZM14 0.875V5.75C14 5.94891 14.079 6.13968 14.2197 6.28033C14.3603 6.42098 14.5511 6.5 14.75 6.5H19.625L14 0.875ZM14 14.75C14 16.5402 13.2888 18.2571 12.023 19.523C10.7571 20.7888 9.04021 21.5 7.25 21.5C5.45979 21.5 3.7429 20.7888 2.47703 19.523C1.21116 18.2571 0.5 16.5402 0.5 14.75C0.5 12.9598 1.21116 11.2429 2.47703 9.97703C3.7429 8.71116 5.45979 8 7.25 8C9.04021 8 10.7571 8.71116 12.023 9.97703C13.2888 11.2429 14 12.9598 14 14.75ZM10.781 11.969C10.7113 11.8992 10.6286 11.8437 10.5375 11.8059C10.4463 11.7681 10.3487 11.7487 10.25 11.7487C10.1513 11.7487 10.0537 11.7681 9.96255 11.8059C9.87143 11.8437 9.78867 11.8992 9.719 11.969L5.75 15.9395L4.781 14.969C4.71127 14.8993 4.62848 14.844 4.53737 14.8062C4.44627 14.7685 4.34862 14.7491 4.25 14.7491C4.15138 14.7491 4.05373 14.7685 3.96263 14.8062C3.87152 14.844 3.78873 14.8993 3.719 14.969C3.64927 15.0387 3.59395 15.1215 3.55622 15.2126C3.51848 15.3037 3.49905 15.4014 3.49905 15.5C3.49905 15.5986 3.51848 15.6963 3.55622 15.7874C3.59395 15.8785 3.64927 15.9613 3.719 16.031L5.219 17.531C5.28867 17.6008 5.37143 17.6563 5.46255 17.6941C5.55367 17.7319 5.65135 17.7513 5.75 17.7513C5.84865 17.7513 5.94633 17.7319 6.03745 17.6941C6.12857 17.6563 6.21133 17.6008 6.281 17.531L10.781 13.031C10.8508 12.9613 10.9063 12.8786 10.9441 12.7874C10.9819 12.6963 11.0013 12.5987 11.0013 12.5C11.0013 12.4013 10.9819 12.3037 10.9441 12.2126C10.9063 12.1214 10.8508 12.0387 10.781 11.969Z"
										fill="#27853F" />
								</svg>

							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide">Complete
									the Tool in One Session
								</h4>

								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.four" key="text" class="inline">
												The tool is designed to be completed in one session; however, you can
												pause and
												return to this later. Please do not close the browser window as results
												for
												completed sessions will not be saved. You will be provided the
												opportunity to email
												the results to yourself at the end of Part 1 and after completing each
												principle-level section in Part 2.
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold transition-all duration-300 ease-in-out"
											@click="readmore.four = !readmore.four">
											{{ readmore.four ? 'Read Less' : 'Read More' }}
										</span>
									</transition>
								</div>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="22" height="20" viewBox="0 0 22 20" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path
										d="M16.657 10.007C16.4235 10.031 16.1999 10.1138 16.0071 10.2475C15.8142 10.3813 15.6583 10.5617 15.554 10.772L14.699 12.495L12.792 12.772C12.272 12.844 11.832 13.212 11.668 13.716L11.63 13.856C11.53 14.321 11.676 14.81 12.023 15.146L13.4 16.483L13.074 18.375C13.0313 18.6305 13.0606 18.8928 13.1588 19.1326C13.2569 19.3723 13.4199 19.5799 13.6296 19.7321C13.8392 19.8843 14.0871 19.975 14.3455 19.9941C14.6038 20.0131 14.8623 19.9598 15.092 19.84L16.8 18.945L18.508 19.841C18.7373 19.9614 18.9957 20.0154 19.254 19.9969C19.5123 19.9783 19.7603 19.888 19.97 19.736L20.082 19.646C20.2574 19.4888 20.39 19.2896 20.4673 19.0671C20.5447 18.8446 20.5642 18.6061 20.524 18.374L20.199 16.483L21.579 15.144C21.959 14.773 22.095 14.22 21.931 13.717L21.88 13.583C21.7843 13.3683 21.6356 13.1813 21.448 13.0396C21.2603 12.898 21.0398 12.8062 20.807 12.773L18.9 12.495L18.047 10.773C17.9319 10.5407 17.7542 10.3452 17.5338 10.2086C17.3135 10.072 17.0593 9.99973 16.8 10L16.657 10.007ZM5.05702 10.007C4.82353 10.031 4.59993 10.1138 4.40706 10.2475C4.21419 10.3813 4.05833 10.5617 3.95402 10.772L3.09902 12.495L1.19202 12.772C0.672022 12.844 0.232022 13.212 0.0680221 13.716L0.0300221 13.856C-0.0699779 14.321 0.0760221 14.81 0.423022 15.146L1.80002 16.483L1.47402 18.375C1.43128 18.6305 1.46062 18.8928 1.55876 19.1326C1.6569 19.3723 1.81994 19.5799 2.02957 19.7321C2.2392 19.8843 2.48711 19.975 2.74545 19.9941C3.00379 20.0131 3.26233 19.9598 3.49202 19.84L5.20002 18.945L6.90802 19.841C7.1373 19.9614 7.39567 20.0154 7.65399 19.9969C7.91231 19.9783 8.16031 19.888 8.37002 19.736L8.48202 19.646C8.65744 19.4888 8.79003 19.2896 8.86734 19.0671C8.94465 18.8446 8.96416 18.6061 8.92402 18.374L8.60002 16.483L9.98002 15.144C10.36 14.773 10.496 14.22 10.332 13.717L10.281 13.583C10.1853 13.3683 10.0366 13.1813 9.84896 13.0396C9.66131 12.898 9.44078 12.8062 9.20802 12.773L7.30002 12.494L6.44702 10.772C6.3318 10.5399 6.15398 10.3446 5.93363 10.2082C5.71328 10.0717 5.45918 9.99964 5.20002 10L5.05702 10.007ZM10.857 0.00700132C10.6235 0.0310147 10.3999 0.113764 10.2071 0.247532C10.0142 0.381301 9.85833 0.561732 9.75402 0.772001L8.89902 2.495L6.99202 2.772C6.47202 2.844 6.03202 3.212 5.86802 3.716L5.83002 3.856C5.73002 4.321 5.87602 4.81 6.22302 5.146L7.60002 6.483L7.27402 8.375C7.23128 8.6305 7.26062 8.89285 7.35876 9.13258C7.4569 9.37232 7.61994 9.57994 7.82957 9.73212C8.0392 9.88431 8.28711 9.97502 8.54545 9.99408C8.80379 10.0131 9.06233 9.95978 9.29202 9.84L11 8.946L12.709 9.842C12.9383 9.96244 13.1967 10.0164 13.455 9.99787C13.7133 9.97932 13.9613 9.88897 14.171 9.737L14.283 9.647C14.4584 9.4898 14.591 9.2906 14.6683 9.0681C14.7457 8.8456 14.7652 8.6071 14.725 8.375L14.4 6.483L15.78 5.144C16.16 4.773 16.296 4.22 16.132 3.717L16.081 3.583C15.9853 3.36826 15.8366 3.18131 15.649 3.03965C15.4613 2.89799 15.2408 2.80624 15.008 2.773L13.1 2.494L12.247 0.772001C12.1318 0.539867 11.954 0.344567 11.7336 0.208152C11.5133 0.0717368 11.2592 -0.000360105 11 1.35247e-06L10.857 0.00700132Z"
										fill="#27853F" />
								</svg>

							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide">Expect
									Level 1 and 2 Ratings in
									Part 2</h4>
								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.five" key="text" class="inline">
												As you go through Part 2 of the tool, it is possible that you will have
												certain
												Level 1 and 2 ratings. Few will achieve Level 4, and in some cases,
												Level 4 is not the desired end state.
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold transition-all duration-300 ease-in-out"
											@click="readmore.five = !readmore.five">
											{{ readmore.five ? 'Read Less' : 'Read More' }}
										</span>
									</transition>
								</div>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="14" height="14" viewBox="0 0 14 14" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path fill-rule="evenodd" clip-rule="evenodd"
										d="M1.5 0C1.10218 0 0.720644 0.158036 0.43934 0.43934C0.158035 0.720645 0 1.10218 0 1.5V12C0 12.3978 0.158035 12.7794 0.43934 13.0607C0.720644 13.342 1.10218 13.5 1.5 13.5H12C12.3978 13.5 12.7794 13.342 13.0607 13.0607C13.342 12.7794 13.5 12.3978 13.5 12V1.5C13.5 1.10218 13.342 0.720645 13.0607 0.43934C12.7794 0.158036 12.3978 0 12 0H1.5ZM4.125 3.75C3.82663 3.75 3.54048 3.86853 3.3295 4.07951C3.11853 4.29048 3 4.57663 3 4.875C3 5.17337 3.11853 5.45952 3.3295 5.67049C3.54048 5.88147 3.82663 6 4.125 6H9.375C9.67337 6 9.95952 5.88147 10.1705 5.67049C10.3815 5.45952 10.5 5.17337 10.5 4.875C10.5 4.57663 10.3815 4.29048 10.1705 4.07951C9.95952 3.86853 9.67337 3.75 9.375 3.75H4.125ZM3 8.625C3 8.32663 3.11853 8.04048 3.3295 7.82951C3.54048 7.61853 3.82663 7.5 4.125 7.5H9.375C9.67337 7.5 9.95952 7.61853 10.1705 7.82951C10.3815 8.04048 10.5 8.32663 10.5 8.625C10.5 8.92337 10.3815 9.20952 10.1705 9.42049C9.95952 9.63147 9.67337 9.75 9.375 9.75H4.125C3.82663 9.75 3.54048 9.63147 3.3295 9.42049C3.11853 9.20952 3 8.92337 3 8.625Z"
										fill="#27853F" />
								</svg>
							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide">Generate
									a
									Summary Report Upon
									Completion
								</h4>
								<div class=" text-justify pt-2">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.six" key="text" class="inline">
												Upon completion, you will have the option of generating a summary report
												which
												provides an overview of your assessment and
												recommendations to strengthen your practices. Please save a copy of the
												report to
												preserve it.
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold  transition-all duration-300 ease-in-out"
											@click="readmore.six = !readmore.six">
											{{ readmore.six ? 'Read Less' : 'Read More' }}
										</span>
									</transition>
								</div>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path fill-rule="evenodd" clip-rule="evenodd"
										d="M23.0794 16.6148C23.0794 21.7097 18.4628 24 12 24C5.5371 24 0.920532 21.7097 0.920532 16.6508C0.920532 11.112 3.69082 8.30569 9.22968 5.4994L7.26853 1.84626C7.15152 1.66328 7.08636 1.45198 7.08 1.23488C7.07365 1.01778 7.12633 0.80303 7.23243 0.613521C7.33854 0.424011 7.49409 0.266851 7.68249 0.158799C7.8709 0.0507465 8.08509 -0.00414703 8.30225 -2.82914e-05H16.1314C16.3349 0.00517969 16.5338 0.0620919 16.7093 0.165352C16.8848 0.268612 17.0311 0.414824 17.1345 0.590228C17.2379 0.765631 17.2949 0.964458 17.3003 1.16799C17.3056 1.37153 17.2591 1.57308 17.1651 1.75369L14.7702 5.4994C20.3074 8.26797 23.0794 11.0743 23.0794 16.6148ZM8.49767 11.1428H11.3828C11.6228 11.2148 11.9245 11.3485 12.1662 11.5714C12.3471 11.7356 12.4809 11.9451 12.5537 12.1783H8.49939C8.38683 12.1783 8.27537 12.2004 8.17138 12.2435C8.06738 12.2866 7.97289 12.3497 7.8933 12.4293C7.8137 12.5089 7.75057 12.6034 7.70749 12.7074C7.66442 12.8114 7.64225 12.9228 7.64225 13.0354C7.64225 13.148 7.66442 13.2594 7.70749 13.3634C7.75057 13.4674 7.8137 13.5619 7.8933 13.6415C7.97289 13.7211 8.06738 13.7842 8.17138 13.8273C8.27537 13.8704 8.38683 13.8925 8.49939 13.8925H12.2828C11.9883 14.2198 11.6146 14.4659 11.1977 14.6074C10.6603 14.8037 10.0947 14.912 9.52282 14.928H9.4971C9.32262 14.9281 9.15234 14.9815 9.00901 15.081C8.86569 15.1805 8.75614 15.3214 8.69502 15.4849C8.6339 15.6483 8.62411 15.8265 8.66696 15.9956C8.70981 16.1648 8.80326 16.3168 8.93482 16.4314L8.93825 16.4348L8.94682 16.44L8.9691 16.4605C9.09076 16.5637 9.21598 16.6627 9.34453 16.7571C10.8228 17.861 12.5039 18.6631 14.292 19.1177C14.4021 19.1479 14.5172 19.1558 14.6305 19.1409C14.7437 19.126 14.8529 19.0886 14.9515 19.0309C15.0501 18.9732 15.1361 18.8964 15.2046 18.805C15.2731 18.7136 15.3226 18.6094 15.3503 18.4985C15.3779 18.3877 15.3832 18.2725 15.3656 18.1596C15.3481 18.0467 15.3082 17.9385 15.2483 17.8412C15.1883 17.744 15.1095 17.6597 15.0166 17.5934C14.9236 17.527 14.8183 17.4799 14.7068 17.4548C13.6582 17.1858 12.6496 16.7801 11.7068 16.248L11.7994 16.2137C12.3788 15.996 13.0165 15.6497 13.5137 15.0891C13.8137 14.7548 14.0485 14.3554 14.1942 13.8925H15.5005C15.7279 13.8925 15.9459 13.8022 16.1066 13.6415C16.2674 13.4807 16.3577 13.2627 16.3577 13.0354C16.3577 12.8081 16.2674 12.5901 16.1066 12.4293C15.9459 12.2686 15.7279 12.1783 15.5005 12.1783H14.3108C14.2566 11.8165 14.1419 11.4665 13.9714 11.1428H15.5005C15.7279 11.1428 15.9459 11.0525 16.1066 10.8918C16.2674 10.731 16.3577 10.513 16.3577 10.2857C16.3577 10.0584 16.2674 9.84034 16.1066 9.67959C15.9459 9.51885 15.7279 9.42854 15.5005 9.42854H8.49939C8.27206 9.42854 8.05404 9.51885 7.8933 9.67959C7.73255 9.84034 7.64225 10.0584 7.64225 10.2857C7.64225 10.513 7.73255 10.731 7.8933 10.8918C8.05404 11.0525 8.27206 11.1428 8.49939 11.1428H8.49767Z"
										fill="#27853F" />
								</svg>
							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide"> Use
									Insights for Strategic
									Discussions and
									Team Conversations on Improving Grantmaking</h4>
								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.seven">
												We encourage you to use the insights for strategic discussions on
												enhancing your grantmaking as well as in conversations with your teams.
											</span>
										</transition>

										<transition name="fade-slide-x">
											<span key="button" class="text-secondary text-h6 cursor-pointer font-bold"
												@click="readmore.seven = !readmore.seven">
												{{ readmore.seven ? 'Read Less' : 'Read More' }}
											</span>
										</transition>

									</p>
								</div>
							</div>
						</div>
						<div class="flex gap-2">
							<div class="w-10 min-w-10 h-10 flex items-center justify-center rounded-full bg-gray-100">
								<svg width="21" height="18" viewBox="0 0 21 18" fill="none"
									xmlns="http://www.w3.org/2000/svg">
									<path
										d="M11 16H2C1.46957 16 0.960859 15.7893 0.585786 15.4142C0.210714 15.0391 0 14.5304 0 14V2C0 0.89 0.89 0 2 0H8L10 2H18C18.5304 2 19.0391 2.21071 19.4142 2.58579C19.7893 2.96086 20 3.46957 20 4V7.04C19.1432 6.36997 18.0877 6.00408 17 6C14.4 6 12.2 8.06 12.2 10.5V10.74C11.5 11.34 11 12.24 11 13.2V16ZM21 13.3V16.8C21 17.4 20.4 18 19.7 18H14.2C13.6 18 13 17.4 13 16.7V13.2C13 12.6 13.6 12 14.2 12V10.5C14.2 9.1 15.6 8 17 8C18.4 8 19.8 9.1 19.8 10.5V12C20.4 12 21 12.6 21 13.3ZM18.5 10.5C18.5 9.7 17.8 9.2 17 9.2C16.2 9.2 15.5 9.7 15.5 10.5V12H18.5V10.5Z"
										fill="#27853F" />
								</svg>

							</div>
							<div class="">
								<h4 class="font-bold text-h5 text-sebase font-primary leading-4 tracking-wide"> Your
									Responses Are Confidential
								</h4>
								<div class="pt-2 text-justify">
									<p class="text-trbase text-sm py-2 text-justify leading-5 tracking-wider inline">
										<transition name="fade-slide-x">
											<span v-if="readmore.eight" key="text" class="inline">
												development team.
												Any trends interfered from this data will only be made at an aggregate
												level, based
												on type of funder (i.e., CSR, Global Foundation,
												Domestic Foundation).
											</span>
										</transition>
									</p>
									<transition name="fade-slide-x">
										<span key="button"
											class="text-secondary text-h6 cursor-pointer font-bold transition-opacity duration-700"
											:class="{ 'opacity-50': readmore.eight }"
											@click="readmore.eight = !readmore.eight">
											{{ readmore.eight ? 'Read Less' : 'Read More' }}
										</span>

									</transition>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>


		<div class="flex flex-col gap-3 px-4 md:px-8 lg:px-16 pt-8">
			<h1 class="text-h2 text-primary font-bold font-primary tracking-wide leading-9">How to get started</h1>
			<p class="text-h5 text-trbase font-normal tracking-wide leading-5">You may pick which section of the tool
				you would like to start with.</p>
			<p class="text-h5 text-trbase font-normal tracking-wide leading-5">You may begin with the <span class="font-bold text-[15px]">Funder Diagnostic</span>
				to get customised recommendations for specific principles you need to improve or
				proceed directly to the <span class="font-bold text-[15px]">Assistive Guides</span> to explore specific principles of interest to your
				organisation.</p>

			<p class="text-h5 text-trbase font-normal tracking-wide leading-5">Alternatively, you can select any of the
				five principle-level <span class="font-bold text-[15px]">Assistive Guides</span> to explore. The Assistive Guides help map your current
				practices along the five PWIT principles, across various elements spanning organisational guidelines,
				approaches, communication,
				etc., to understand the strengths and gaps in your funding practices.</p>
				<ul class="px-2 md:px-10">
					<li class="text-h5 text-trbase">For the first four principles, the guide helps to categorise your practices on a progressive scale. </li>
					<li class="text-h5 text-trbase">For the first four principles, the guide helps to categorise your practices on a progressive scale. </li>
				</ul>

		</div>
		<!-- <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 justify-between gap-4 px-4 md:px-8 lg:px-16 py-7">
			<div class="flex flex-col gap-2">
				<div class="w-16 min-w-16 h-16 rounded-full bg-gray-200 flex items-center justify-center">
					<img class="w-8  h-8" src="../../assets/file.png" alt="Description of image">

				</div>
				<h1 class="font-bold text-h5 text-sebase tracking-wide leading-5 font-primary">Lorem ipsum dolor sit
					amet
				</h1>
				<p class="text-h6 text-trbase font-normal leading-4 tracking-wider"> Duis aute irure dolor in
					reprehenderit in voluptate velit esse cillum
					dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
					officia deserunt mollit anim id est laborum.</p>
			</div>
			<div class="flex flex-col gap-2">
				<div class="w-16 min-w-16 h-16  rounded-full bg-gray-200 flex items-center justify-center">
					<img class="w-8  h-8" src="../../assets/file.png" alt="Description of image">
				</div>
				<h1 class="font-bold text-h5 text-sebase tracking-wide leading-5 font-primary">Lorem ipsum dolor sit
					amet
				</h1>
				<p class="text-h6 text-trbase font-normal leading-4 tracking-wider"> Duis aute irure dolor in
					reprehenderit in voluptate velit esse cillum
					dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
					officia deserunt mollit anim id est laborum.</p>

			</div>
			<div class="flex flex-col gap-2">
				<div class="w-16 min-w-16 h-16 rounded-full bg-gray-200 flex items-center justify-center">
					<img class="w-8  h-8" src="../../assets/file.png" alt="Description of image">
				</div>
				<h1 class="font-bold text-h5 text-sebase tracking-wide leading-5 font-primary">Lorem ipsum dolor sit
					amet
				</h1>
				<p class="text-h6 text-trbase font-normal leading-4 tracking-wider"> Duis aute irure dolor in
					reprehenderit in voluptate velit esse cillum
					dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
					officia deserunt mollit anim id est laborum.</p>

			</div>
		</div> -->
		<div class="w-full flex justify-center py-6 px-4">
			<PickAssessment />
		</div>
		<div class="bg-secondary h-auto pb-52  relative px-4 md:px-8 lg:px-16">
			<!-- SVG Background -->
			<div class="absolute inset-0 flex justify-center gap-12 py-10">
				<div class="relative">
					<svg width="240" height="200" viewBox="0 0 24100" fill="none" xmlns="http://www.w3.org/2000/svg"
						class="absolute h-52">
						<path
							d="M191.131 195.802C183.475 202.784 163.131 208.639 148.045 205.712C172.664 205.185 200.515 190.397 208.097 182.666C215.001 175.534 215.301 170.956 214.4 166.527C202.69 176.661 176.194 185.519 149.696 182.066C183.85 183.642 218.755 161.647 226.187 155.342C234.819 147.911 235.045 138.679 233.918 136.651C213.576 151.513 188.279 159.472 166.06 160.147C186.102 156.243 220.107 147.986 237.296 122.84C239.248 120.211 241.425 116.234 240.899 114.432C236.621 100.996 219.956 120.062 218.68 120.812C216.654 122.014 214.626 123.215 212.526 124.265C195.034 133.724 175.894 140.33 156.076 142.581C137.31 144.684 118.019 143.182 106.157 126.368C98.7251 115.783 101.279 104.298 111.413 96.5675C116.741 92.5137 123.046 89.6612 129.203 86.8834C133.631 84.9321 138.736 83.656 140.387 78.7011C142.038 73.8227 144.366 67.9667 134.907 67.5918C107.808 66.4649 87.9161 79.9025 69.6767 98.2931C65.1713 102.871 61.194 107.826 57.89 113.305C56.5394 111.354 55.338 109.253 54.3623 107.151C51.9594 102.121 50.5342 96.6421 50.1593 91.0119C48.2079 62.788 73.279 41.2427 95.4231 27.9562C124.699 10.4667 159.003 2.88513 192.633 0.482264C157.201 -1.54368 123.798 2.88513 95.0481 12.4181C83.713 16.1716 73.1278 20.675 63.4457 25.9303C54.5135 30.7341 46.3312 36.1385 39.0499 42.0692C34.2442 45.9718 29.8154 50.1769 25.8381 54.5311C6.99598 74.498 -1.03518 96.2672 0.916173 116.909C2.71832 136.35 10.1488 153.015 21.1835 167.503C21.2581 167.578 21.2581 167.652 21.3347 167.729C32.444 182.215 47.1557 194.451 63.3711 204.885C63.9718 205.411 64.496 205.937 65.0967 206.461C72.6783 212.918 81.7617 217.797 91.5204 221.1C93.9978 221.925 96.6991 222.751 99.5515 223.427C130.779 231.309 178.071 229.658 190.005 200.908C190.531 199.406 190.906 197.229 191.131 195.802Z"
							fill="white" fill-opacity="0.08" />
					</svg>
				</div>
				<div class="relative pl-20 pt-5">
					<svg width="240" height="227" viewBox="0 0 241 228" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path
							d="M240.642 111.166C238.84 91.7235 231.407 75.0605 220.374 60.5726C220.298 60.498 220.298 60.4214 220.223 60.3468C209.114 45.859 194.4 33.6247 178.187 23.1907C177.586 22.6646 177.06 22.1385 176.461 21.6143C168.88 15.1576 159.796 10.2792 150.038 6.9753C147.56 6.15079 144.859 5.32431 142.006 4.64899C110.779 -3.23296 63.4872 -1.58197 51.5514 27.168C51.0272 28.5952 50.5757 30.7723 50.3519 32.1976C58.0081 25.2167 78.35 19.3626 93.4386 22.2897C68.8171 22.8138 40.9681 37.602 33.3866 45.3348C26.4803 52.4649 26.1799 57.0449 27.081 61.4737C38.791 51.34 65.2893 42.4824 91.7876 45.9355C57.6331 44.3591 22.7268 66.352 15.2963 72.6576C6.6625 80.09 6.4387 89.3226 7.56358 91.3485C27.9075 76.4857 53.2043 68.5292 75.423 67.8538C55.3795 71.7565 21.3761 80.0135 4.18503 105.161C2.23369 107.788 0.0565777 111.767 0.582696 113.569C4.86231 127.005 21.5253 107.939 22.8014 107.187C24.8293 105.988 26.8552 104.786 28.9577 103.734C46.4472 94.2775 65.5897 87.6716 85.4055 85.4199C104.173 83.3174 123.465 84.8192 135.324 101.633C142.756 112.217 140.204 123.703 130.071 131.434C124.741 135.487 118.435 138.34 112.279 141.118C107.85 143.069 102.746 144.345 101.095 149.3C99.4438 154.178 97.1175 160.034 106.574 160.409C133.673 161.534 153.565 148.099 171.807 129.708C176.31 125.128 180.289 120.173 183.591 114.694C184.942 116.645 186.143 118.748 187.119 120.85C189.522 125.88 190.947 131.359 191.324 136.989C193.275 165.213 168.202 186.757 146.058 200.043C116.784 217.534 82.4785 225.116 48.8501 227.517C84.2806 229.545 117.685 225.116 146.435 215.581C157.768 211.83 168.354 207.324 178.038 202.071C186.97 197.265 195.152 191.861 202.433 185.932C207.237 182.027 211.666 177.824 215.645 173.47C234.56 153.578 242.593 131.809 240.642 111.166Z"
							fill="white" fill-opacity="0.08" />
					</svg>
				</div>
			</div>


			<!-- Content -->
			<h1 class="text-center font-primary text-h2 font-bold tracking-wide leading-9 text-white pt-8 pb-5">
				About the Partnership
			</h1>
			<div class="flex flex-col sm:flex-row items-center justify-center gap-4">
				<div class="flex flex-col gap-4 w-full text-center text-white font-primary text-sm">
					<p class="text-h5 text-[#E9EAEB] font-normal text-center leading-5 tracking-wider"> Lorem
						ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
						dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
						aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
						cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
						culpa qui officia deserunt mollit anim id est laborum.
					</p>
				</div>
			</div>
		</div>

		<div
			class="flex flex-col sm:flex-row h-[500px]  items-center justify-center gap-4 px-4 pb-8 relative bg-gray-100 ">
			<ContactUs />
		</div>
		<FooterNav />
	</div>
</template>
<script setup>
import { inject, ref, onMounted } from 'vue';
import FooterNav from '../../components/FooterNav.vue';
import PickAssessment from './PickAssessment.vue';
import ContactUs from './ContactUs.vue';
import { IndianRupee, Handshake, PiggyBank, ChartNoAxesCombined, Scale } from 'lucide-vue-next'

// const call = inject('$call');
let readmore = ref({
	one: false,
	two: false,
	three: false,
	four: false,
	five: false,
	six: false,
	seven: false,
	eight: false,
});

// const get_faqs = async () => {
// 	const res = await call('pwit.controllers.api.get_faq', {});
// 	if (res.code === 200) {
// 		faqs_list.value = res.data;
// 	}
// };
// onMounted(() => {
// 	get_faqs();
// });

</script>
<style scoped>
.fade-slide-x-enter-from {
	opacity: 0;
	transform: translateX(-20px);
}

.fade-slide-x-enter-to {
	opacity: 1;
	transform: translateX(0);
}

.fade-slide-x-leave-from {
	opacity: 1;
	transform: translateX(-10);
}

.fade-slide-x-leave-to {
	opacity: 0;
	transform: translateX(-20px);
}

.fade-slide-x-enter-active,
.fade-slide-x-leave-active {
	transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out 0.1s;
}
ul li {
	list-style-type: disc;
}
</style>
