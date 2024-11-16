<template>
    <div class="w-full h-screen p-4">
        <div class="flex gap-2">
            <Text @click="store.sidebar = true" class="w-6 min-w-6 cursor-pointer block md:hidden" />
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
        <div class="w-full grid grid-cols-1 xl:grid-cols-2 gap-5 pt-4">
            <div class="w-full  mx-auto">
                <div class="bg-white border p-4">
                    <h2 class="text-primary font-bold font-serif text-2xl">
                        Results and Recommendations
                    </h2>
                    <p class="text-h6 pt-1 pb-4">
                        <span class="font-medium">Average:</span>
                        <span class="text-green-600 font-semibold">2.5</span>
                    </p>
                    <!-- Table -->
                    <div class="overflow-x-auto">
                        <table class="w-full border">
                            <thead class="bg-[#E0F4FB]">
                                <tr>
                                    <th
                                        class="w-1/2 px-4 py-2 text-left font-serif text-h6 text-trbase font-bold border">
                                        Parameters
                                    </th>
                                    <th
                                        class="w-1/2 px-4 py-2 text-left font-serif text-h6 text-trbase font-bold border">
                                        Performance at that stage
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="recommendation in recommendations" :key="recommendation.title"
                                    class="border-b">
                                    <td class="w-1/2 px-4 py-2 font-normal text-h6 text-pbase border border-gray-200">
                                        {{ recommendation.title }}
                                    </td>
                                    <td class="py-2 px-4">
                                        <div v-for="(item, idx) in recommendation.items" :key="idx"
                                            class="h-4 bg-gray-200">
                                            <div class="h-4 " :style="{ width: item.chart + '%', backgroundColor: item.color  }">
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <!-- Right Section -->
            <div class="w-full mx-auto flex justify-center items-center p-4">
                <div class="text-start">
                    <p class="text-primary font-bold font-serif text-2xl pb-4">
                        The Power of Multiyear Partnerships in Grantmaking
                    </p>
                    <p class="text-h6 text-trbase text-justify">
                        Multiyear partnerships simplify grantmaking, reduce the time spent on scouting new grantees and
                        projects,
                        and help funders gain a deeper understanding of social issues. Engaging in these longer-term
                        partnerships allows funders to move from being
                        only grant makers to playing the role of advisors to nonprofit partners and can facilitate
                        greater job enrichment for program teams as they are able
                        to invest more time and effort in understanding nonprofit needs and support them in delivering
                        on their intended impact. Multiyear partnerships nurture
                        trust as relationships between funders and nonprofits deepen over time and a mutual
                        understanding of a nonprofit’s needs and goals grows. For funders,
                        adopting a multiyear approach can help increasingly focus on creating lasting change, over
                        immediate and short-term outputs. Additionally,
                        it enables stability and visibility for nonprofits to plan and direct efforts on their core
                        focus.
                    </p>
                </div>
            </div>
        </div>
        <div class="grid grid-cols-1 xl:grid-cols-[70%_30%] md:grid-cols-1  lg:grid-cols-1 gap-4 pt-10 w-full">
            <!-- Recommended Actions Section -->
            <div class="w-full mx-auto">
                <p class="text-primary font-bold font-serif text-xl sm:text-2xl pb-4">
                    Recommended Actions
                </p>
                <div v-for="action in recommendedActions" :key="action.title" class="pb-5">
                    <div
                        class="flex justify-between items-center px-4 py-2 bg-[#e9eaec] text-h5 font-bold font-serif text-pbase">
                        {{ action.title }}
                    </div>
                    <div class="pt-2">
                        <div v-for="item in action.items" :key="item.description" class="flex gap-4 pt-4">
                            <div class="w-7 h-7 flex justify-center items-center">
                                <svg class="w-5 h-5" fill="none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
                                    <path
                                        d="M8 0L9.16938 5.17688L13.6569 2.34315L10.8231 6.83062L16 8L10.8231 9.16938L13.6569 13.6569L9.16938 10.8231L8 16L6.83062 10.8231L2.34315 13.6569L5.17688 9.16938L0 8L5.17688 6.83062L2.34315 2.34315L6.83062 5.17688L8 0Z"
                                        fill="#255B97" />
                                </svg>
                            </div>
                            <p class="text-justify text-sm md:text-base text-trbase font-normal">
                                <strong class="text-pbase">{{ item.title }}</strong>
                                {{ item.description }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Useful Resources Section -->
            <div class="w-full mx-auto rounded-sm shadow-md px-4 py-2">
                <p class="text-primary font-bold font-serif text-xl sm:text-2xl pb-4">
                    Useful Resources
                </p>
                <div v-for="resource in resources" :key="resource.title" class="flex gap-4 py-3 border-b ">
                    <span class="flex justify-center items-center">
                        <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 13 13">
                            <path
                                d="M9.92589 1.94306L3.05734 1.94306L3.05734 0.343298H12.657L12.657 1.14318L12.657 9.94298L11.0573 9.94298L11.0573 3.07443L1.909 12.2227L0.777625 11.0913L9.92589 1.94306Z"
                                fill="#27853F" />
                        </svg>
                    </span>
                    <p class="text-pbase text-h6  md:text-base font-normal text-justify">
                        {{ resource.title }}
                    </p>
                </div>
            </div>
        </div>
        <div class="pb-6 sm:pt-5">
            <button class=" py-3 px-6 bg-[#255B97] text-white rounded">
                Next Principle
            </button>
        </div>
    </div>

</template>

<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router';
import DownloadResults from './DownloadResults.vue';
import { Text } from 'lucide-vue-next';
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

const recommendedActions = ref([
    {
        title: 'Policy guidelines',
        items: [
            { title: 'Revisiting your policy in context of your impact goals ', description: 'and ascertain any biases or blind spots that might be limiting multiyear partnerships (such as extending multiyear funding only to large nonprofits with a credible funder baser rather than small, community-based nonprofits).' },
            { title: 'If alignment on policy is a barrier, engage with senior leadership and board / committee ', description: ' on the need, benefits and alignment with the Foundation/ CSRs vision and goals, to increase the number of multiyear partnerships. Lay out the opportunity cost (e.g., costs associated with sourcing and diligence). Leverage research and evidence, and showcase examples from funders/ NGOs who have fostered multiyear partnerships.' }
        ]
    },
    {
        title: 'Annual budget allocation',
        items: [
            { title: 'Engage with existing and potential nonprofits on their 3–5-year strategy and', description: ' to understand the percentage of funding allocated to multiyear partnerships and the number of nonprofits being supported in this regard. If the percentage is low, reflect on internal awareness and mindsets that may be influencing current practices.' },
            { title: 'Evaluating your current funding portfolio', description: ' and impact goals, and how your funding can enable your collective mission. Customize grants to best suit their needs (both current and future) and objectives.' }
        ]
    }
]);

const resources = ref([
    { title: 'Funder Practices that Strengthen Nonprofit Resilience: Lessons from India' },
    { title: 'New Attitudes, Old Practices: The Provision of Multiyear General Operating Support' },
    { title: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' },
    { title: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' }
]);


const recommendations = ref([
    {
        title: 'Policy guidelines',
        items: [
            { chart: 50, color:'#FFD23F' }
        ]
    },
    {
        title: 'Annual budget allocation',
        items: [
            { chart: 75, color:'#FF6464' }
        ]
    },
    {
        title: 'Approach: Structuring of multiyear partnerships',
        items:[
            {chart:40, color:'#337357'}
        ]
    }
]);

</script>