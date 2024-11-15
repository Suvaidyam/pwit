<template>
    <div class="w-full h-screen p-4">
        <div class="flex gap-2">
            <Text  @click="store.sidebar=true" class="w-6 min-w-6 cursor-pointer block md:hidden"/>
            <p class="text-gray-800 text-sm">
                <router-link to="/">Home</router-link>
                / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> / <router-link
                    to="/recommended">Recommended Principles</router-link> /
                <router-link :to="`/funder/${route.params.category}`">{{ title }}</router-link>
                <span class="text-gray-400 truncate"> / Results and Recommendtions</span>
            </p>
        </div>
        <div class="flex justify-between items-center">
            <h1 class="text-h3 md:text-h2 text-primary">Results and Recommendtions</h1>
            <DownloadResults />
        </div>
        <div class="w-full flex gap-5 justify-center pt-4">
            <div class="w-1/2">
                <div class="bg-white border p-4">
                    <h2 class="text-xl font-semibold text-blue-800">Developing multiyear funder-nonprofit partnerships</h2>
                    <p class="text-sm mt-1 mb-4">
                        <span class="font-medium">Average:</span> <span class="text-green-600 font-semibold">2.5</span>
                    </p>

                    <div class="overflow-x-auto">
                        <table class="min-w-full border border-gray-300 rounded-lg">
                        <thead class="bg-blue-50">
                            <tr>
                                <th class="py-2 px-4 text-left text-gray-700 font-medium">Parameters</th>
                                <th class="py-2 px-4 text-left text-gray-700 font-medium">Performance at that stage</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white">
                            <tr class="border-t border-gray-200">
                                <td class="py-2 px-4 text-gray-700">Policy guidelines</td>
                                <td class="py-2 px-4">
                                    <div class="h-4 bg-gray-200 rounded-full">
                                        <div class="h-4 bg-yellow-400 rounded-full w-3/4"></div>
                                    </div>
                                </td>
                            </tr>
                            <tr class="border-t border-gray-200">
                                <td class="py-2 px-4 text-gray-700">Annual budget allocation</td>
                                <td class="py-2 px-4">
                                    <div class="h-4 bg-gray-200 rounded-full">
                                        <div class="h-4 bg-red-400 rounded-full w-1/3"></div>
                                    </div>
                                </td>
                            </tr>
                            <tr class="border-t border-gray-200">
                                <td class="py-2 px-4 text-gray-700">Approach: Structuring of multiyear partnerships</td>
                                <td class="py-2 px-4">
                                    <div class="h-4 bg-gray-200 rounded-full">
                                        <div class="h-4 bg-red-400 rounded-full w-1/2"></div>
                                    </div>
                                </td>
                            </tr>
                            <tr class="border-t border-gray-200">
                                <td class="py-2 px-4 text-gray-700">Approach: Eligibility for multiyear partnerships</td>
                                <td class="py-2 px-4">
                                    <div class="h-4 bg-gray-200 rounded-full">
                                        <div class="h-4 bg-red-400 rounded-full w-1/2"></div>
                                    </div>
                                </td>
                            </tr>
                            <tr class="border-t border-gray-200">
                                <td class="py-2 px-4 text-gray-700">Channels of communication: Nonprofits and the ecosystem</td>
                                <td class="py-2 px-4">
                                    <div class="h-4 bg-gray-200 rounded-full">
                                        <div class="h-4 bg-red-400 rounded-full w-1/2"></div>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            </div>
                <div class="w-1/2 flex justify-center items-center p-4 ">
                    <div class="text-justify ">
                        <p class="text-primary font-bold font-serif text-2xl pb-4">The Power of Multiyear Partnerships in Grantmaking</p>
                    <p class="text-sm text-trbase">
                        Multiyear partnerships simplifies grantmaking, reduces the time spent on scouting new grantees and projects, and help funders gain a deeper understanding of social issues. Engaging in these longer-term partnerships allows for funders to move from being only grant makers to playing the role of advisors to nonprofit partners and can facilitate greater job enrichment for program teams as they are able to invest more time and effort in understanding nonprofit needs and support them in delivering on their intended impact. Multiyear partnerships nurture trust as relationships between funders and nonprofits deepen over time and a mutual understanding of a nonprofit’s needs and goals grows. For funder, adopting a multiyear approach can help increasingly focus on creating lasting change, over immediate and short-term outputs. Additionally, it enables stability and visibility for nonprofits to plan and direct efforts on their core focus.
                    </p>
                    </div>
                </div>
            </div>   
            <div class="w-full pt-10 flex justify-center gap-4 ">
                <div class="w-[70%]">
                    <p class="text-primary font-bold font-serif text-2xl pb-4">Recommended actions</p>
                        <div class="relative  w-full">
                            <div class="w-full">
                                <div class="flex w-full justify-between items-center px-4 py-3 bg-[#e9eaec] text-h5  font-bold font-serif text-pbase ">
                                    Policy guidelines
                                </div>
                                    <div class="absolute mt-2 w-full bg- h-auto pb-3 ">
                                        <div class="py-1" role="menu" aria-orientation="vertical">
                                         <div class="w-full pt-4 flex gap-4">
                                            <div
                                            class="w-7 h-7 min-w-7 flex justify-center items-center">
                                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M8 0L9.16938 5.17688L13.6569 2.34315L10.8231 6.83062L16 8L10.8231 9.16938L13.6569 13.6569L9.16938 10.8231L8 16L6.83062 10.8231L2.34315 13.6569L5.17688 9.16938L0 8L5.17688 6.83062L2.34315 2.34315L6.83062 5.17688L8 0Z" fill="#255B97"/>
                                                </svg>

                                            </div>
                                            <div class=" ">
                                                <p class="text-justify text-sm text-trbase font-normal">
                                                    <strong class="text-pbase">Revisiting your policy in context of your impact goals </strong>
                                                    and ascertain any biases or blind spots that might be limiting multiyear partnerships (such as extending multiyear funding only to large nonprofits with a credible funder baser rather than small, community-based nonprofits).
                                                </p>
                                            </div>
                                        </div>
                                    <div class="w-full pt-4 flex gap-4">
                                            <div
                                            class="w-7 h-7 min-w-7 flex justify-center items-center">
                                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M8 0L9.16938 5.17688L13.6569 2.34315L10.8231 6.83062L16 8L10.8231 9.16938L13.6569 13.6569L9.16938 10.8231L8 16L6.83062 10.8231L2.34315 13.6569L5.17688 9.16938L0 8L5.17688 6.83062L2.34315 2.34315L6.83062 5.17688L8 0Z" fill="#255B97"/>
                                                </svg>

                                            </div>
                                            <div class=" ">
                                                <p class="text-justify text-sm text-trbase font-normal">
                                                    <strong class="text-pbase">If alignment on policy is a barrier, engage with senior leadership and board / committee</strong>
                                                    on the need, benefits and alignment with the Foundation/ CSRs vision and goals, to increase the number of multiyear partnerships. Lay out the opportunity cost (e.g., costs associated with sourcing and diligence). Leverage research and evidence, and showcase examples from funders/ NGOs who have fostered multiyear partnerships.
                                                </p>
                                            </div>
                                    </div>
                              </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-[30%]  rounded-md shadow-lg px-4 py-2">
                <p class="text-primary font-bold font-serif text-2xl pb-4">Useful resources</p>
                <div class="flex gap-4 py-3">
                    <span class="flex justify-center items-center">
                        <svg width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z" fill="#27853F"/>
                        </svg>
                    </span>
                    <p class="text-pbase text-sm font-normal text-justify">
                        Funder Practices that Strengthen Nonprofit Resilience: Lessons from India
                    </p> 
                </div>
                <div class="flex gap-4 border-t-2 py-3">
                    <span class="flex justify-center items-center">
                        <svg width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z" fill="#27853F"/>
                        </svg>
                    </span>
                    <p class="text-pbase text-sm font-normal text-justify">
                        New Attitudes, Old Practices: The Provision of Multiyear General Operating Support
                    </p> 
                </div>
                <div class="flex gap-4 border-t-2 py-3">
                    <span class="flex justify-center items-center">
                        <svg width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z" fill="#27853F"/>
                        </svg>
                    </span>
                    <p class="text-pbase text-sm font-normal text-justify">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    </p> 
                </div>
                <div class="flex gap-4 border-t-2 py-3">
                    <span class="flex justify-center items-center">
                        <svg width="13" height="13" viewBox="0 0 13 13" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z" fill="#27853F"/>
                        </svg>
                    </span>
                    <p class="text-pbase text-sm font-normal text-justify">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    </p> 
                </div>
               
            </div>
        </div>              
        </div>
       
</template>

<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router';
import DownloadResults from './DownloadResults.vue';
import { Text } from 'lucide-vue-next'

const route = useRoute()
const title = ref(splitAtSecondCapital(route.path));

watch(route, (newVal) => {
    title.value = splitAtSecondCapital(newVal.path)
})
function splitAtSecondCapital(input) {
    input = input.split('/')[2]
    return input
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ')
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .trim();
}
</script>