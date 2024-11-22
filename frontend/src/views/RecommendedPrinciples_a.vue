    <template>
        <div class="w-100">
            <div class="px-4 md:px-8 lg:px-20 mx-auto">
                <div class="mt-6">
                    <div class="flex gap-2">
                        <p class="text-gray-800 text-sm">
                            <router-link to="/">Home</router-link>
                            / <router-link to="/funder-diagnostic">Funder Diagnostic</router-link> <span
                                class="text-gray-400">/ Recommended Principles</span>
                        </p>
                    </div>
                    <h1 class="text-h3 md:text-h2 font-bold  text-[#002C77] font-serif">Pathway for funders to
                        strengthen their
                        grant
                        making practices</h1>
                    <p class="text-sebase pt-3  font-normal text-sm text-justify">
                        Funders can pursue or advance their journey on one or more principles; however, we recognize
                        that a step-by-step approach
                        would allow this exercise to become more meaningful and effective. This section presents three
                        entry points for you to initiate
                        your journey; however, you may select whichever principles you would like to explore given your
                        focus.
                    </p>
                </div>
                <div class="flex items-center justify-center my-14">
                    <div class="border-t border-[#D0D1D3] flex-grow"></div>
                    <p class="px-4  text-sebase font-bold text-h4 font-serif ">Recommended principles</p>
                    <div class="border-t border-[#D0D1D3] flex-grow"></div>
                </div>
                <Loader v-if="loading"/>
                <div v-if="!loading" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-x-4 gap-y-12 pt-4">
                    <!-- Card 1 -->
                    <router-link v-for="el in recommended" :key="el.name" :to="el.route"
                        class="bg-white shadow-sm hover:shadow-xl rounded-lg p-4 min-h-56  border-t-4 " :class="`border-[${el.color}]`">
                        <div class="rounded-md bg-white relative shadow-lg">
                            <div class="w-[70px] h-[70px] rounded-full border-8 absolute -top-14 bg-white justify-center items-center flex"
                                :class="`border-[${el.color}]`">
                                <IndianRupee v-if="el.icon=='IndianRupee'"/>
                                <Handshake v-if="el.icon=='Handshake'"/>
                                <PiggyBank v-if="el.icon=='PiggyBank'"/>
                               <ChartNoAxesCombined v-if="el.icon=='ChartNoAxesCombined'"/>
                               <Scale v-if="el.icon=='Scale'"/>
                            </div>
                        </div>

                        <div class="flex items-center pt-8">
                            <div>
                                <h3 class="text-h5 font-bold" :class="`text-[${el.color}]`">{{ el.name1 }}</h3>
                                <p class="text-[trbase] text-h6 font-normal pt-1 text-justify">{{ el.description }}</p>
                            </div>
                        </div>
                    </router-link>
                </div>

                <div class="flex items-center justify-center my-14">
                    <div class="border-t border-[#D0D1D3] flex-grow"></div>
                    <p class="px-4  text-sebase font-bold text-h4 font-serif ">Additional PWIT principles to explore
                        principles</p>
                    <div class="border-t border-[#D0D1D3] flex-grow"></div>
                </div>
                <Loader v-if="loading"/>
                <div v-if="!loading" class="grid grid-cols-1 lg:grid-cols-2 gap-x-4 gap-y-12 py-6">
                    <router-link v-for="el in additional" :key="el.name" :to="el.route"
                        class="bg-white shadow-lg rounded-lg p-4 h-56  border-t-4 " :class="`border-[${el.color}]`">
                        <div class="rounded-md bg-white relative shadow-lg">
                            <div class="w-[70px] h-[70px] rounded-full border-8 absolute -top-14 bg-white justify-center items-center flex"
                                :class="`border-[${el.color}]`">
                               <IndianRupee v-if="el.icon=='IndianRupee'"/>
                               <Handshake v-if="el.icon=='Handshake'"/>
                               <PiggyBank v-if="el.icon=='PiggyBank'"/>
                               <ChartNoAxesCombined v-if="el.icon=='ChartNoAxesCombined'"/>
                               <Scale v-if="el.icon=='Scale'"/>
                            </div>
                        </div>
                        <div class="flex items-center pt-8">
                            <div>
                                <h3 class="text-h5 font-bold" :class="`text-[${el.color}]`">{{ el.name1 }}</h3>
                                <p class="text-[trbase] text-h6 font-normal pt-1 text-justify">{{ el.description }}</p>
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>
            <FooterNav />
        </div>
    </template>
<script setup>
import { computed, inject, onMounted, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import FooterNav from '../components/FooterNav.vue';
import  Loader  from './Assessment/Loader.vue';
import {IndianRupee,Handshake,PiggyBank,ChartNoAxesCombined,Scale} from 'lucide-vue-next'

const router = useRouter()
const call = inject('$call')
const session = JSON.parse(localStorage.getItem('session'))
const results = ref({})
const loading = ref(false)

const data = [
    {
        name: 1,
        name1: 'DEVELOP MULTIYEAR FUNDER-NONPROFIT PARTNERSHIPS',
        description: 'Multiyear partnerships nurture trust between funders and nonprofits while simplifying the grantmaking process. Adopting a longer-term partnership approach can help funders increasingly focus on creating lasting change, over immediate and short-term outputs.',
        icon: 'Handshake',
        route: '/funder/multi-year-partnerships',
        color: '#59467b',
        code: 'myp'
    },
    {
        name: 2,
        name1: 'PAY A FAIR SHARE OF CORE COSTS',
        description: 'Core costs — often referred to as indirect costs — are functions are essential for nonprofits to conduct day-to-day operations and deliver on their impact mandates. Supporting nonprofits in this regard aligns with funders goals of ensuring that nonprofits have the critical investments required to enable operational effectives, have sound...',
        icon: 'IndianRupee',
        route: '/funder/core-costs',
        color: '#136096',
        code: 'core_cost'
    },
    {
        name: 3,
        name1: 'INVEST IN ORGANIZATIONAL DEVELOPMENT',
        description: 'Organizational development (OD) investments build and strengthen a range of critical efficiency and growth-oriented capabilities that enable nonprofits to deliver greater impact.',
        icon: 'ChartNoAxesCombined',
        route: '/funder/organization-development',
        color: '#029fd9',
        code: 'od'
    },
    {
        name: 4,
        name1: 'BUILD FINANCIAL RESILIENCE',
        description: 'Financial resilience refers to a nonprofit’s ability to sustain its operations over the long term and withstand external stresses and shocks. By supporting nonprofits build their financial resilience, funders can ensure the sustainability of the organization and its ability to continue creating impact in the communities in which they work.',
        icon: 'PiggyBank',
        route: '/funder/build-financial-resilience',
        color: '#058248',
        code: 'fr'
    },
    {
        name: 5,
        name1: 'EMBED DIVERSITY EQUITY, AND INCLUSION IN GRANTMAKING',
        description: 'An intentional focus on DEI can help funders address the disproportional funding gap that persists by organizations not located in major cities and headed by members of historically marginalized populations such as Dalit, Bahujan and Adivasi (DBA) communities. An intentional focus on DEI can help funders address the disproportionate financial gap these critical agents of social change face and thus accelerate progress on India’s steepest challenges.',
        icon: 'Scale',
        route: '/funder/diversity-equity-inclusion',
        color: '#f38714',
        code: 'dei'
    }
] 
console.log(results)
const recommended = computed(() => {
    return data;
});

// Additional logic
const additional = computed(() => { 
    return data;
});

const get_result = async () => {
    loading.value = true
    try {
        const response = await call('pwit.controllers.api.get_results', {
            doctype: 'Funder Diagnostic',
            session: session.data.name
        });

        const groupedSums = Object.entries(response.data).reduce((acc, [key, value]) => {
            const keyParts = key.split('_');
            keyParts.pop();
            const prefix = keyParts.join('_');
            acc[prefix] = (acc[prefix] || 0) + value;
            return acc;
        }, {});
        results.value = groupedSums;
        loading.value = false
    } catch (error) {
        console.error('Error fetching results:', error);
    }
};

watch(results.value, (newVal) => {
    results.value = newVal;
});
// Fetch data on mount
onMounted(() => {
    get_result();
});
</script>