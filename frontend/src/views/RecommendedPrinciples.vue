    <template>
        <div class="w-100">
            <div class="px-4 md:px-8 lg:px-20 mx-auto">
                <div class="mt-6">
                    <p @click="router.back(-1)" class="cursor-pointer text-sm">
                        <ArrowLeftIcon class="h-4 w-4 inline-block " />
                        Back
                    </p>
                    <h1 class="text-h2 font-bold  text-[#002C77] font-serif">Pathway for funders to strengthen their grant
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
                    <router-link to="/funder/multi-year-partnerships"
                        class="bg-white shadow-lg rounded-lg p-4 h-56  border-t-4 border-[#5d497d]">
                        <div class="rounded-md bg-white relative shadow-lg">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 border-[#5d497d] absolute -top-14 bg-white justify-center items-center flex">
                                {{ }} <svg width="34" height="22" viewBox="0 0 34 22" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M17.0808 1.92616L12.0261 6.09156C11.1854 6.78226 11.0235 8.0255 11.6606 8.91277C12.3342 9.85849 13.6448 10.0444 14.5482 9.32719L19.7334 5.22554C20.0989 4.93864 20.6211 5.0024 20.9083 5.37431C21.1955 5.74622 21.1276 6.27752 20.7621 6.56974L19.6708 7.43044L26.929 14.2311V4.20013H26.8925L26.6888 4.06731L22.8978 1.59676C22.0989 1.07608 21.1642 0.799805 20.2138 0.799805C19.0755 0.799805 17.9685 1.19828 17.0808 1.92616ZM18.2713 8.53555L15.5717 10.6714C13.9268 11.9784 11.5405 11.6383 10.3081 9.91693C9.14888 8.29646 9.4413 6.03312 10.9713 4.77394L15.3158 1.19828C14.7101 0.937943 14.0574 0.805118 13.3942 0.805118C12.4125 0.799805 11.4569 1.09733 10.6371 1.64989L6.87741 4.20013V16.1013H8.34995L13.1227 20.5323C14.1461 21.4834 15.7283 21.409 16.663 20.3676C16.9502 20.0435 17.1434 19.6663 17.2426 19.2731L18.1303 20.102C19.1486 21.053 20.736 20.9839 21.6707 19.9479C21.9057 19.6876 22.078 19.3847 22.1877 19.0712C23.2007 19.7619 24.5792 19.6185 25.4304 18.6728C26.3651 17.6367 26.2972 16.0216 25.2789 15.0706L18.2713 8.53555ZM1.02903 4.20013C0.56951 4.20013 0.193542 4.58267 0.193542 5.05021V16.1013C0.193542 17.0417 0.940256 17.8014 1.86451 17.8014H3.53548C4.45973 17.8014 5.20645 17.0417 5.20645 16.1013V4.20013H1.02903ZM2.69999 14.4011C2.92158 14.4011 3.13409 14.4907 3.29077 14.6501C3.44745 14.8095 3.53548 15.0257 3.53548 15.2512C3.53548 15.4767 3.44745 15.6929 3.29077 15.8523C3.13409 16.0117 2.92158 16.1013 2.69999 16.1013C2.47841 16.1013 2.2659 16.0117 2.10922 15.8523C1.95253 15.6929 1.86451 15.4767 1.86451 15.2512C1.86451 15.0257 1.95253 14.8095 2.10922 14.6501C2.2659 14.4907 2.47841 14.4011 2.69999 14.4011ZM28.6 4.20013V16.1013C28.6 17.0417 29.3467 17.8014 30.271 17.8014H31.9419C32.8662 17.8014 33.6129 17.0417 33.6129 16.1013V5.05021C33.6129 4.58267 33.2369 4.20013 32.7774 4.20013H28.6ZM30.271 15.2512C30.271 15.0257 30.359 14.8095 30.5157 14.6501C30.6724 14.4907 30.8849 14.4011 31.1064 14.4011C31.328 14.4011 31.5405 14.4907 31.6972 14.6501C31.8539 14.8095 31.9419 15.0257 31.9419 15.2512C31.9419 15.4767 31.8539 15.6929 31.6972 15.8523C31.5405 16.0117 31.328 16.1013 31.1064 16.1013C30.8849 16.1013 30.6724 16.0117 30.5157 15.8523C30.359 15.6929 30.271 15.4767 30.271 15.2512Z"
                                        fill="#464547" />
                                </svg>
                            </div>
                        </div>

                        <div class="flex items-center pt-8">
                            <div>
                                <h3 class="text-h5 font-bold text-[#604B81]">DEVELOP MULTIYEAR FUNDER-NONPROFIT
                                    PARTNERSHIPS</h3>
                                <p class="text-[trbase] text-h6 font-normal pt-1 text-justify"> Multiyear partnerships nurture trust between
                                    funders and nonprofits while simplifying the grantmaking process. Adopting a
                                    longer-term partnership approach can help funders increasingly focus on creating
                                    lasting change, over immediate and short-term outputs.</p>
                            </div>
                        </div>
                    </router-link>
                    <!-- Card 2 -->
                    <router-link to="/funder/core-costs" class="bg-white shadow-lg rounded-lg p-4 h-56  border-t-4 border-[#136096] ">
                        <div class="rounded-md bg-white relative">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 border-[#136096] absolute -top-14 bg-white justify-center items-center flex">
                                {{ }} <svg width="15" height="24" viewBox="0 0 15 24" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M2 0.75H14.5L13.25 3.25H9.175C9.775 3.975 10.225 4.825 10.4875 5.75H14.5L13.25 8.25H10.75C10.5947 9.80828 9.9176 11.2684 8.82856 12.3938C7.73953 13.5191 6.30235 14.2437 4.75 14.45V14.5H3.875L11.375 23.25H8.25L0.75 14.5V12H3.875C6.075 12 7.9 10.375 8.2 8.25H0.75L2 5.75H7.825C7.125 4.275 5.625 3.25 3.875 3.25H0.75L2 0.75Z"
                                        fill="#464547" />
                                </svg>

                            </div>
                        </div>
                        <div class="flex items-center pt-8">
                            <div>
                                <h3 class=" text-h5 font-bold text-[#145A95]">PAY A FAIR SHARE OF CORE COSTS</h3>
                                <p class="text-[trbase] text-h6 font-normal pt-1 text-justify">Core costs — often referred to as indirect costs —
                                    are functions are essential for nonprofits to conduct day-to-day operations and
                                    deliver on their impact mandates. Supporting nonprofits in this regard aligns with
                                    funders goals of ensuring that nonprofits have the critical investments required to
                                    enable operational effectives, have sound...</p>
                            </div>
                        </div>
                    </router-link>
                    <!-- Card 3 -->
                    <router-link to="/funder/organization-development" class="bg-white shadow-lg rounded-lg h-56  p-4 border-t-4 border-[#029fd9]">
                        <div class="rounded-md bg-white relative">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 border-[#029fd9] absolute -top-14 bg-white justify-center items-center flex">
                                {{ }} <svg width="24" height="25" viewBox="0 0 24 25" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" clip-rule="evenodd"
                                        d="M17.328 0.394218C17.5146 0.205934 17.7527 0.0776973 18.0119 0.0257985C18.2712 -0.0261003 18.5399 0.000680683 18.784 0.102739L22.5653 1.67994C22.8914 1.81538 23.1509 2.0753 23.2868 2.40276C23.4228 2.73022 23.4242 3.09854 23.2907 3.42702L21.7458 7.23055C21.646 7.47616 21.476 7.68646 21.2573 7.83487C21.0386 7.98327 20.7811 8.06309 20.5173 8.06424C20.2536 8.06539 19.9954 7.98781 19.7754 7.84132C19.5555 7.69483 19.3837 7.48601 19.2818 7.24128L18.672 5.77494L3.31556 12.3752C3.15447 12.4445 2.98139 12.4812 2.80621 12.4832C2.63103 12.4852 2.45717 12.4524 2.29456 12.3869C2.13196 12.3213 1.98379 12.2241 1.85852 12.1009C1.73324 11.9777 1.63332 11.8309 1.56444 11.6689C1.49557 11.5069 1.45911 11.3328 1.45712 11.1566C1.45514 10.9803 1.48768 10.8055 1.55289 10.6419C1.6181 10.4783 1.71469 10.3293 1.83716 10.2033C1.95963 10.0773 2.10558 9.97678 2.26667 9.9075L17.6427 3.30006L17.0436 1.86055C16.941 1.61532 16.9133 1.34496 16.964 1.08386C17.0146 0.822751 17.1414 0.582697 17.328 0.394218ZM22.2222 9.80021C22.6937 9.80021 23.1459 9.98861 23.4793 10.324C23.8127 10.6593 24 11.1142 24 11.5884V24.1059C24 24.343 23.9064 24.5704 23.7397 24.7381C23.573 24.9058 23.3469 25 23.1111 25H18.6667C18.4309 25 18.2048 24.9058 18.0381 24.7381C17.8714 24.5704 17.7778 24.343 17.7778 24.1059V11.5884C17.7778 11.1142 17.9651 10.6593 18.2985 10.324C18.6319 9.98861 19.0841 9.80021 19.5556 9.80021H22.2222ZM14.5902 13.0047C14.2566 12.67 13.8045 12.4822 13.3333 12.4825H10.6667C10.1952 12.4825 9.74299 12.6709 9.40959 13.0063C9.07619 13.3416 8.88889 13.7965 8.88889 14.2707V24.1059C8.88889 24.343 8.98254 24.5704 9.14924 24.7381C9.31594 24.9058 9.54203 25 9.77778 25H14.2222C14.458 25 14.6841 24.9058 14.8508 24.7381C15.0175 24.5704 15.1111 24.343 15.1111 24.1059V14.2707C15.1113 14.0356 15.0654 13.8028 14.976 13.5855C14.8866 13.3683 14.7555 13.1709 14.5902 13.0047ZM4.44444 15.1648C4.91594 15.1648 5.36813 15.3532 5.70152 15.6886C6.03492 16.024 6.22222 16.4788 6.22222 16.9531V24.1059C6.22222 24.343 6.12857 24.5704 5.96187 24.7381C5.79517 24.9058 5.56908 25 5.33333 25H0.888889C0.653141 25 0.427049 24.9058 0.26035 24.7381C0.0936505 24.5704 0 24.343 0 24.1059V16.9531C0 16.4788 0.187301 16.024 0.520699 15.6886C0.854097 15.3532 1.30628 15.1648 1.77778 15.1648H4.44444Z"
                                        fill="#464547" />
                                </svg>
                            </div>
                        </div>
                        <div class="flex items-center pt-8">
                            <div>
                                <h3 class=" text-h5 font-bold text-[#00A9E0]">INVEST IN ORGANIZATIONAL DEVELOPMENT
                                </h3>
                                <p class=" text-[trbase] text-h6 font-normal pt-1 text-justify">Organizational development (OD) investments build
                                    and strengthen a range of critical efficiency and growth-oriented capabilities that
                                    enable nonprofits to deliver greater impact.</p>
                            </div>
                        </div>
                    </router-link>
                </div>

                <div class="flex items-center justify-center my-14">
                    <div class="border-t border-[#D0D1D3] flex-grow"></div>
                    <p class="px-4  text-sebase font-bold text-h4 font-serif ">Additional PWIT principles to explore principles</p>
                    <div class="border-t border-[#D0D1D3] flex-grow"></div>
                </div>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-x-4 gap-y-12 py-6">
                    <!-- Card 4 -->
                    <div class="bg-white shadow-lg rounded-lg p-4 border-t-4 border-[#058248]">
                        <div class="rounded-md bg-white relative">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 border-[#058248] absolute -top-14 bg-white justify-center items-center flex">
                                <svg width="26" height="25" viewBox="0 0 26 25" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M21.2687 0.264815C21.4185 0.38164 21.5397 0.531066 21.6231 0.701743C21.7065 0.872419 21.7499 1.05986 21.75 1.24982V3.87607C22.7466 4.89216 23.4803 6.13603 23.8875 7.49981H24.25C24.5815 7.49981 24.8995 7.63151 25.1339 7.86593C25.3683 8.10035 25.5 8.41829 25.5 8.74981V12.4998C25.4999 12.7319 25.4351 12.9594 25.3131 13.1567C25.191 13.3541 25.0164 13.5136 24.8088 13.6173L22.9887 14.5286C22.3541 15.5773 21.5062 16.481 20.5 17.1811V18.7498C20.5 19.0813 20.3683 19.3993 20.1339 19.6337C19.8995 19.8681 19.5815 19.9998 19.25 19.9998H15.5C15.1685 19.9998 14.8505 19.8681 14.6161 19.6337C14.3817 19.3993 14.25 19.0813 14.25 18.7498H13C13 19.0813 12.8683 19.3993 12.6339 19.6337C12.3995 19.8681 12.0815 19.9998 11.75 19.9998H8C7.66848 19.9998 7.35054 19.8681 7.11612 19.6337C6.8817 19.3993 6.75 19.0813 6.75 18.7498V17.1811C5.09016 16.026 3.88166 14.3316 3.33 12.3861C2.52091 12.1813 1.80324 11.7125 1.29064 11.0539C0.778043 10.3952 0.49981 9.58441 0.5 8.74981V8.12481C0.5 7.79329 0.631696 7.47535 0.866117 7.24093C1.10054 7.00651 1.41848 6.87481 1.75 6.87481C2.08152 6.87481 2.39946 7.00651 2.63388 7.24093C2.8683 7.47535 3 7.79329 3 8.12481V8.74981C2.99971 8.86474 3.01528 8.97915 3.04625 9.08982C3.27123 6.93825 4.28527 4.9463 5.89263 3.49845C7.49998 2.05061 9.5867 1.24952 11.75 1.24982H15.3462L20.1963 0.0373155C20.3806 -0.00875602 20.5729 -0.0122134 20.7588 0.0272071C20.9446 0.0666276 21.119 0.147888 21.2687 0.264815ZM18.625 6.24981C18.1277 6.24982 17.6508 6.44736 17.2992 6.79899C16.9475 7.15062 16.75 7.62753 16.75 8.12481C16.75 8.6221 16.9475 9.09901 17.2992 9.45064C17.6508 9.80227 18.1277 9.99981 18.625 9.99981C19.1223 9.99981 19.5992 9.80227 19.9508 9.45064C20.3025 9.09901 20.5 8.6221 20.5 8.12481C20.5 7.62753 20.3025 7.15062 19.9508 6.79899C19.5992 6.44736 19.1223 6.24982 18.625 6.24981Z"
                                        fill="#464547" />
                                </svg>

                            </div>
                        </div>
                        <div class="flex items-center pt-8">
                            <div>
                                <h3 class=" text-h5 font-bold text-[#008542]">BUILD FINANCIAL RESILIENCE</h3>
                                <p class=" text-[trbase] text-h6 font-normal pt-1 text-justify"> Financial resilience refers to a nonprofit’s
                                    ability to sustain its operations over the long term and withstand external stresses
                                    and shocks. By supporting nonprofits build their financial resilience, funders can
                                    ensure the sustainability of the organization and its ability to continue creating
                                    impact in the communities in which they work.</p>
                            </div>
                        </div>
                    </div>
                    <!-- Card 5 -->
                    <div class="bg-white shadow-lg rounded-lg p-4 border-t-4 border-[#f38714]">
                        <div class="rounded-md bg-white relative">
                            <div
                                class="w-[70px] h-[70px] rounded-full border-8 border-[#f38714] absolute -top-14 bg-white justify-center items-center flex">
                                {{ }} <svg width="26" height="25" viewBox="0 0 26 25" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M0.5 24.25V21.75H11.75V7.78125C11.2083 7.59375 10.7396 7.30209 10.3438 6.90625C9.94792 6.51042 9.65625 6.04167 9.46875 5.5H5.5L9.25 14.25C9.25 15.2917 8.82292 16.1771 7.96875 16.9063C7.11458 17.6354 6.08333 18 4.875 18C3.66667 18 2.63542 17.6354 1.78125 16.9063C0.927083 16.1771 0.5 15.2917 0.5 14.25L4.25 5.5H1.75V3H9.46875C9.71875 2.27084 10.1667 1.67209 10.8125 1.20375C11.4583 0.735419 12.1875 0.500836 13 0.500002C13.8125 0.499169 14.5417 0.733752 15.1875 1.20375C15.8333 1.67375 16.2812 2.2725 16.5312 3H24.25V5.5H21.75L25.5 14.25C25.5 15.2917 25.0729 16.1771 24.2188 16.9063C23.3646 17.6354 22.3333 18 21.125 18C19.9167 18 18.8854 17.6354 18.0312 16.9063C17.1771 16.1771 16.75 15.2917 16.75 14.25L20.5 5.5H16.5312C16.3438 6.04167 16.0521 6.51042 15.6562 6.90625C15.2604 7.30209 14.7917 7.59375 14.25 7.78125V21.75H25.5V24.25H0.5ZM18.7812 14.25H23.4688L21.125 8.8125L18.7812 14.25ZM2.53125 14.25H7.21875L4.875 8.8125L2.53125 14.25ZM13 5.5C13.3542 5.5 13.6513 5.38 13.8913 5.14C14.1313 4.9 14.2508 4.60334 14.25 4.25C14.2492 3.89667 14.1292 3.6 13.89 3.36C13.6508 3.12 13.3542 3 13 3C12.6458 3 12.3492 3.12 12.11 3.36C11.8708 3.6 11.7508 3.89667 11.75 4.25C11.7492 4.60334 11.8692 4.90042 12.11 5.14125C12.3508 5.38209 12.6475 5.50167 13 5.5Z"
                                        fill="#464547" />
                                </svg>

                            </div>
                        </div>
                        <div class="flex items-center pt-8 ">
                            <div>
                                <h3 class=" text-h5 font-bold text-[#EF8613]">EMBED DIVERSITY EQUITY, AND INCLUSION
                                    IN GRANTMAKING</h3>
                                <p class=" text-[trbase] text-h6 font-normal pt-1 text-justify"> An intentional focus on DEI can help funders
                                    address the disproportional funding gap that persists by organizations not located
                                    in major cities and headed by members of historically marginalized populations such
                                    as Dalit, Bahujan and Adivasi (DBA) communities. An intentional focus on DEI can
                                    help funders address the disproportionate financial gap these critical agents of
                                    social change face and thus accelerate progress on India’s steepest challenges.
                                </p>
                            </div>
                        </div>
                    </div>
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
console.log(router)
const data = ref([{ name: 1 }, { name: 2 }, { name: 3 }, { name: 4 }, { name: 5 }])
</script>