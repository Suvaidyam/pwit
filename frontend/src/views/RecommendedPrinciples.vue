    <template>
        <div class="w-100">
            <div class="px-4 md:px-8 lg:px-20 mx-auto">
                <div class="mt-6">
                    <p @click="router.back(-1)" class="cursor-pointer text-sm">
                        <ArrowLeftIcon class="h-4 w-4 inline-block " />
                        Back
                    </p>
                    <h1 class="text-h2 font-bold  text-[#002C77] font-serif">Pathway for funders to strengthen their
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

                <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-x-4 gap-y-12 pt-4">
                    <!-- Card 1 -->
                    <router-link v-for="el in recommended" :key="el.name" :to="el.route"
                        class="bg-white shadow-lg rounded-lg p-4 h-56  border-t-4 " :class="`border-[${el.color}]`">
                        <div class="rounded-md bg-white relative shadow-lg">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 absolute -top-14 bg-white justify-center items-center flex" :class="`border-[${el.color}]`">
                                 <svg width="34" height="22" viewBox="0 0 34 22" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M17.0808 1.92616L12.0261 6.09156C11.1854 6.78226 11.0235 8.0255 11.6606 8.91277C12.3342 9.85849 13.6448 10.0444 14.5482 9.32719L19.7334 5.22554C20.0989 4.93864 20.6211 5.0024 20.9083 5.37431C21.1955 5.74622 21.1276 6.27752 20.7621 6.56974L19.6708 7.43044L26.929 14.2311V4.20013H26.8925L26.6888 4.06731L22.8978 1.59676C22.0989 1.07608 21.1642 0.799805 20.2138 0.799805C19.0755 0.799805 17.9685 1.19828 17.0808 1.92616ZM18.2713 8.53555L15.5717 10.6714C13.9268 11.9784 11.5405 11.6383 10.3081 9.91693C9.14888 8.29646 9.4413 6.03312 10.9713 4.77394L15.3158 1.19828C14.7101 0.937943 14.0574 0.805118 13.3942 0.805118C12.4125 0.799805 11.4569 1.09733 10.6371 1.64989L6.87741 4.20013V16.1013H8.34995L13.1227 20.5323C14.1461 21.4834 15.7283 21.409 16.663 20.3676C16.9502 20.0435 17.1434 19.6663 17.2426 19.2731L18.1303 20.102C19.1486 21.053 20.736 20.9839 21.6707 19.9479C21.9057 19.6876 22.078 19.3847 22.1877 19.0712C23.2007 19.7619 24.5792 19.6185 25.4304 18.6728C26.3651 17.6367 26.2972 16.0216 25.2789 15.0706L18.2713 8.53555ZM1.02903 4.20013C0.56951 4.20013 0.193542 4.58267 0.193542 5.05021V16.1013C0.193542 17.0417 0.940256 17.8014 1.86451 17.8014H3.53548C4.45973 17.8014 5.20645 17.0417 5.20645 16.1013V4.20013H1.02903ZM2.69999 14.4011C2.92158 14.4011 3.13409 14.4907 3.29077 14.6501C3.44745 14.8095 3.53548 15.0257 3.53548 15.2512C3.53548 15.4767 3.44745 15.6929 3.29077 15.8523C3.13409 16.0117 2.92158 16.1013 2.69999 16.1013C2.47841 16.1013 2.2659 16.0117 2.10922 15.8523C1.95253 15.6929 1.86451 15.4767 1.86451 15.2512C1.86451 15.0257 1.95253 14.8095 2.10922 14.6501C2.2659 14.4907 2.47841 14.4011 2.69999 14.4011ZM28.6 4.20013V16.1013C28.6 17.0417 29.3467 17.8014 30.271 17.8014H31.9419C32.8662 17.8014 33.6129 17.0417 33.6129 16.1013V5.05021C33.6129 4.58267 33.2369 4.20013 32.7774 4.20013H28.6ZM30.271 15.2512C30.271 15.0257 30.359 14.8095 30.5157 14.6501C30.6724 14.4907 30.8849 14.4011 31.1064 14.4011C31.328 14.4011 31.5405 14.4907 31.6972 14.6501C31.8539 14.8095 31.9419 15.0257 31.9419 15.2512C31.9419 15.4767 31.8539 15.6929 31.6972 15.8523C31.5405 16.0117 31.328 16.1013 31.1064 16.1013C30.8849 16.1013 30.6724 16.0117 30.5157 15.8523C30.359 15.6929 30.271 15.4767 30.271 15.2512Z"
                                        fill="#464547" />
                                </svg>
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
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-x-4 gap-y-12 py-6">
                    <router-link v-for="el in additional" :key="el.name" :to="el.route"
                        class="bg-white shadow-lg rounded-lg p-4 h-56  border-t-4 " :class="`border-[${el.color}]`">
                        <div class="rounded-md bg-white relative shadow-lg">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 absolute -top-14 bg-white justify-center items-center flex" :class="`border-[${el.color}]`">
                                 <svg width="34" height="22" viewBox="0 0 34 22" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M17.0808 1.92616L12.0261 6.09156C11.1854 6.78226 11.0235 8.0255 11.6606 8.91277C12.3342 9.85849 13.6448 10.0444 14.5482 9.32719L19.7334 5.22554C20.0989 4.93864 20.6211 5.0024 20.9083 5.37431C21.1955 5.74622 21.1276 6.27752 20.7621 6.56974L19.6708 7.43044L26.929 14.2311V4.20013H26.8925L26.6888 4.06731L22.8978 1.59676C22.0989 1.07608 21.1642 0.799805 20.2138 0.799805C19.0755 0.799805 17.9685 1.19828 17.0808 1.92616ZM18.2713 8.53555L15.5717 10.6714C13.9268 11.9784 11.5405 11.6383 10.3081 9.91693C9.14888 8.29646 9.4413 6.03312 10.9713 4.77394L15.3158 1.19828C14.7101 0.937943 14.0574 0.805118 13.3942 0.805118C12.4125 0.799805 11.4569 1.09733 10.6371 1.64989L6.87741 4.20013V16.1013H8.34995L13.1227 20.5323C14.1461 21.4834 15.7283 21.409 16.663 20.3676C16.9502 20.0435 17.1434 19.6663 17.2426 19.2731L18.1303 20.102C19.1486 21.053 20.736 20.9839 21.6707 19.9479C21.9057 19.6876 22.078 19.3847 22.1877 19.0712C23.2007 19.7619 24.5792 19.6185 25.4304 18.6728C26.3651 17.6367 26.2972 16.0216 25.2789 15.0706L18.2713 8.53555ZM1.02903 4.20013C0.56951 4.20013 0.193542 4.58267 0.193542 5.05021V16.1013C0.193542 17.0417 0.940256 17.8014 1.86451 17.8014H3.53548C4.45973 17.8014 5.20645 17.0417 5.20645 16.1013V4.20013H1.02903ZM2.69999 14.4011C2.92158 14.4011 3.13409 14.4907 3.29077 14.6501C3.44745 14.8095 3.53548 15.0257 3.53548 15.2512C3.53548 15.4767 3.44745 15.6929 3.29077 15.8523C3.13409 16.0117 2.92158 16.1013 2.69999 16.1013C2.47841 16.1013 2.2659 16.0117 2.10922 15.8523C1.95253 15.6929 1.86451 15.4767 1.86451 15.2512C1.86451 15.0257 1.95253 14.8095 2.10922 14.6501C2.2659 14.4907 2.47841 14.4011 2.69999 14.4011ZM28.6 4.20013V16.1013C28.6 17.0417 29.3467 17.8014 30.271 17.8014H31.9419C32.8662 17.8014 33.6129 17.0417 33.6129 16.1013V5.05021C33.6129 4.58267 33.2369 4.20013 32.7774 4.20013H28.6ZM30.271 15.2512C30.271 15.0257 30.359 14.8095 30.5157 14.6501C30.6724 14.4907 30.8849 14.4011 31.1064 14.4011C31.328 14.4011 31.5405 14.4907 31.6972 14.6501C31.8539 14.8095 31.9419 15.0257 31.9419 15.2512C31.9419 15.4767 31.8539 15.6929 31.6972 15.8523C31.5405 16.0117 31.328 16.1013 31.1064 16.1013C30.8849 16.1013 30.6724 16.0117 30.5157 15.8523C30.359 15.6929 30.271 15.4767 30.271 15.2512Z"
                                        fill="#464547" />
                                </svg>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import FooterNav from '../components/FooterNav.vue';
import { ArrowLeftIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const data = [
    {
        name: 1,
        name1: 'DEVELOP MULTIYEAR FUNDER-NONPROFIT PARTNERSHIPS',
        description: 'Multiyear partnerships nurture trust between funders and nonprofits while simplifying the grantmaking process. Adopting a longer-term partnership approach can help funders increasingly focus on creating lasting change, over immediate and short-term outputs.',
        icon:'',
        route: '/funder/multi-year-partnerships',
        color: '#5d497d',
        group: 'recommended'
    },
    {
        name: 2,
        name1: 'PAY A FAIR SHARE OF CORE COSTS',
        description: 'Core costs — often referred to as indirect costs — are functions are essential for nonprofits to conduct day-to-day operations and deliver on their impact mandates. Supporting nonprofits in this regard aligns with funders goals of ensuring that nonprofits have the critical investments required to enable operational effectives, have sound...',
        icon:'',
        route: '/funder/core-costs',
        color: '#136096',
        group: 'recommended'
    },
    {
        name: 3,
        name1: 'INVEST IN ORGANIZATIONAL DEVELOPMENT',
        description: 'Organizational development (OD) investments build and strengthen a range of critical efficiency and growth-oriented capabilities that enable nonprofits to deliver greater impact.',
        icon:'',
        route: '/funder/organization-development',
        color: '#00A9E0',
        group: 'recommended'
    },
    {
        name: 4,
        name1: 'BUILD FINANCIAL RESILIENCE',
        description: 'Financial resilience refers to a nonprofit’s ability to sustain its operations over the long term and withstand external stresses and shocks. By supporting nonprofits build their financial resilience, funders can ensure the sustainability of the organization and its ability to continue creating impact in the communities in which they work.',
        icon:'',
        route: '/funder/build-financial-resilience',
        color: '#058248',
        group: 'additional'
    },
    {
        name: 5,
        name1: 'EMBED DIVERSITY EQUITY, AND INCLUSION IN GRANTMAKING',
        description: 'An intentional focus on DEI can help funders address the disproportional funding gap that persists by organizations not located in major cities and headed by members of historically marginalized populations such as Dalit, Bahujan and Adivasi (DBA) communities. An intentional focus on DEI can help funders address the disproportionate financial gap these critical agents of social change face and thus accelerate progress on India’s steepest challenges.',
        icon:'',
        route: '/funder/diversity-equity-inclusion',
        color: '#EF8613',
        group: 'additional'
    }
]
const recommended = ref(data.filter(item => item.group === 'recommended'))
const additional = ref(data.filter(item => item.group === 'additional'))
</script>