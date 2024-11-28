<template>
    <button @click="openDialog" :disabled="props.disabled"
        :class="[props.disabled?'cursor-not-allowed':'cursor-pointer']"
        class="border flex items-center justify-center gap-2 px-2 md:px-4 h-7 md:h-9 text-sm border-[#27853F] text-[#27853F] rounded-md">
        <span class="hidden lg:block">Download Result </span>
        <Download class="w-4" />
    </button>
    <!--  -->
    <TransitionRoot as="template" :show="open">
        <Dialog class="relative z-30">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full items-center justify-center p-4 text-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class="flex justify-between">
                                    <h1 class="text-h3 font-serif font-bold text-primary">Provide the following
                                        information</h1>
                                    <X @click="open = false" class="text-sm  cursor-pointer" />
                                </div>
                                <p class="text-sm font-normal text=[#21272A] py-1">Lorem ipsum dolor sit amet,
                                    consectetur adipiscing elit, sed do
                                    eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                                <hr class="pb-2 mt-2">
                                <div class="flex flex-col gap-1.5">
                                    <label for="" class="text-h5 font-normal text=[#21272A] py-1 ">Please share your
                                        designation</label>
                                    <select name="" id="" class="h-12 outline-none border-b px-2 bg-slate-50">
                                        <option value="" selected>Select </option>
                                    </select>
                                </div>
                                <div class="pt-3 ">
                                    <h1 class="pb-2 text-h5 font-normal text=[#21272A] py-1 ">Please select which funder
                                        type your organization identifies as</h1>
                                    <label
                                        :class="`w-full px-4 py-2 bg-white flex gap-2 border rounded-md cursor-pointer ${isActive ? 'border-slate-600' : ''}`"
                                        @click="isActive = !isActive" for="input1">
                                        <input id="input1" type="radio" />
                                        <span class="font-normal text-sm text-slate-600 cursor-pointer">
                                            Corporate Social Responsibility (CSR)
                                        </span>
                                    </label>
                                    <label for="input2"
                                        class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md mt-3 cursor-pointer">
                                        <input id="input2" type="radio" class="p-8" />
                                        <span for="input2" class="font-normal text-sm text-sebase cursor-pointer">
                                            Domestic Foundation</span>
                                    </label>
                                    <label for="input3"
                                        class="w-full px-4 py-2 bg-white flex gap-2 border rounded-md mt-3 cursor-pointer">
                                        <input id="input3" type="radio" class="p-8" />
                                        <span for="input3" class="font-normal text-sm text-sebase cursor-pointer">
                                            Global Foundation</span>
                                    </label>
                                </div>
                                <div class="flex flex-col gap-1.5 pt-2 ">
                                    <label for="" class="text-h5  font-normal text=[#21272A] py-1 ">Your organisation’s
                                        approximate annual budget
                                        allocation</label>
                                    <select name="" id="" class="h-12 outline-none border-b px-2 bg-slate-50">
                                        <option value="" selected>Select </option>
                                    </select>
                                </div>
                                <div class="flex justify-end pt-2">
                                    <button class="bg-secondary text-white rounded-md w-28 h-12 text-h5">Submit</button>
                                </div>
                            </div>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
    <!--  -->
    <TransitionRoot as="template" :show="open_ass">
        <Dialog class="relative z-30" @close="open_ass = false">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full justify-center p-4 text-center items-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
                            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                                <div class=" border-b w-full py-2">
                                    <DialogTitle as="h3" class="text-xl font-semibold text-primary font-serif">Pick an
                                        Assessment </DialogTitle>
                                </div>
                                <div class="flex flex-col gap-3 pt-4">
                                    <div class="flex flex-col gap-2">
                                        <h2 class="font-serif font-semibold text-gray-800 tracking-wider">Funder
                                            diagnostic</h2>
                                        <p class="text-xs text-gray-600">Lorem ipsum dolor sit amet consectetur
                                            adipisicing elit. veniam, reprehenderit</p>
                                        <div class="flex justify-between items-center gap-1 border-b pb-4">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <svg width="14" height="16" viewBox="0 0 14 16" fill="none"
                                                        xmlns="http://www.w3.org/2000/svg">
                                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                                            d="M1.129 1.379C0.25 2.25725 0.25 3.67175 0.25 6.5V9.5C0.25 12.3282 0.25 13.7427 1.129 14.621C2.008 15.4992 3.42175 15.5 6.25 15.5H7.75C10.5782 15.5 11.9927 15.5 12.871 14.621C13.7357 13.757 13.75 12.374 13.75 9.635L11.6365 11.7485C11.434 11.951 11.2682 12.1167 11.0815 12.263C10.8625 12.4346 10.625 12.5812 10.3735 12.7003C10.1433 12.8038 9.90687 12.8927 9.6655 12.9665L7.9315 13.5448C7.65624 13.6365 7.36085 13.6499 7.07844 13.5832C6.79603 13.5166 6.53776 13.3726 6.33258 13.1674C6.1274 12.9622 5.98342 12.704 5.91678 12.4216C5.85013 12.1392 5.86345 11.8438 5.95525 11.5685L6.16075 10.9535L6.517 9.884L6.53275 9.8345C6.6235 9.563 6.69775 9.341 6.79975 9.1265C6.91975 8.8745 7.0655 8.63875 7.237 8.41925C7.38325 8.23175 7.549 8.06675 7.7515 7.86425L10.756 4.859L11.59 4.025L11.6852 3.92975C11.9401 3.67412 12.243 3.47141 12.5765 3.3333C12.91 3.19519 13.2675 3.12439 13.6285 3.125C13.5152 2.3525 13.2955 1.80275 12.871 1.379C11.9927 0.5 10.5782 0.5 7.75 0.5H6.25C3.42175 0.5 2.00725 0.5 1.129 1.379ZM3.4375 5.75C3.4375 5.60082 3.49676 5.45774 3.60225 5.35225C3.70774 5.24676 3.85082 5.1875 4 5.1875H8.875C9.02418 5.1875 9.16726 5.24676 9.27275 5.35225C9.37824 5.45774 9.4375 5.60082 9.4375 5.75C9.4375 5.89918 9.37824 6.04226 9.27275 6.14775C9.16726 6.25324 9.02418 6.3125 8.875 6.3125H4C3.85082 6.3125 3.70774 6.25324 3.60225 6.14775C3.49676 6.04226 3.4375 5.89918 3.4375 5.75ZM3.4375 8.75C3.4375 8.60082 3.49676 8.45774 3.60225 8.35225C3.70774 8.24676 3.85082 8.1875 4 8.1875H5.875C6.02418 8.1875 6.16726 8.24676 6.27275 8.35225C6.37824 8.45774 6.4375 8.60082 6.4375 8.75C6.4375 8.89918 6.37824 9.04226 6.27275 9.14775C6.16726 9.25324 6.02418 9.3125 5.875 9.3125H4C3.85082 9.3125 3.70774 9.25324 3.60225 9.14775C3.49676 9.04226 3.4375 8.89918 3.4375 8.75ZM3.4375 11.75C3.4375 11.6008 3.49676 11.4577 3.60225 11.3523C3.70774 11.2468 3.85082 11.1875 4 11.1875H5.125C5.27418 11.1875 5.41726 11.2468 5.52275 11.3523C5.62824 11.4577 5.6875 11.6008 5.6875 11.75C5.6875 11.8992 5.62824 12.0423 5.52275 12.1477C5.41726 12.2532 5.27418 12.3125 5.125 12.3125H4C3.85082 12.3125 3.70774 12.2532 3.60225 12.1477C3.49676 12.0423 3.4375 11.8992 3.4375 11.75Z"
                                                            fill="#27853F" />
                                                    </svg>
                                                </div>
                                                <p class="text-sm font-medium">Funding practics diagnostic</p>
                                            </div>
                                            <router-link to="/funder-diagnostic"
                                                class="text-primary text-sm cursor-pointer">View</router-link>
                                        </div>
                                    </div>
                                    <div class="flex flex-col gap-2">
                                        <h2 class="font-serif font-semibold text-gray-800 tracking-wider">Assistive
                                            Guides</h2>
                                        <p class="text-xs text-gray-600">Lorem ipsum dolor sit amet consectetur
                                            adipisicing elit. veniam, reprehenderit</p>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <svg width="22" height="14" viewBox="0 0 22 14" fill="none"
                                                        xmlns="http://www.w3.org/2000/svg">
                                                        <path
                                                            d="M11.2394 1.55582L8.09731 4.05506C7.57471 4.46948 7.47408 5.21542 7.87009 5.74779C8.28882 6.31522 9.10356 6.42679 9.66511 5.99643L12.8884 3.53545C13.1156 3.36331 13.4402 3.40156 13.6187 3.62471C13.7972 3.84785 13.755 4.16663 13.5278 4.34196L12.8494 4.85839L17.3613 8.93878V2.9202H17.3386L17.212 2.84051L14.8554 1.35818C14.3588 1.04577 13.7777 0.880005 13.187 0.880005C12.4794 0.880005 11.7912 1.11909 11.2394 1.55582ZM11.9795 5.52145L10.3013 6.80295C9.27884 7.58715 7.79543 7.38313 7.02938 6.35028C6.30878 5.378 6.49055 4.01999 7.44162 3.26448L10.1423 1.11909C9.76573 0.962888 9.35999 0.883193 8.94775 0.883193C8.33751 0.880005 7.7435 1.05852 7.23388 1.39005L4.89678 2.9202V10.0609H5.81214L8.77896 12.7195C9.41517 13.2901 10.3987 13.2455 10.9797 12.6207C11.1583 12.4262 11.2784 12.1999 11.34 11.964L11.8918 12.4613C12.5248 13.0319 13.5116 12.9905 14.0926 12.3689C14.2387 12.2127 14.3458 12.031 14.414 11.8429C15.0437 12.2573 15.9006 12.1712 16.4297 11.6038C17.0107 10.9822 16.9685 10.0131 16.3356 9.44245L11.9795 5.52145ZM1.2613 2.9202C0.975653 2.9202 0.741943 3.14972 0.741943 3.43025V10.0609C0.741943 10.6251 1.20612 11.081 1.78065 11.081H2.81936C3.3939 11.081 3.85807 10.6251 3.85807 10.0609V2.9202H1.2613ZM2.30001 9.04079C2.43775 9.04079 2.56985 9.09453 2.66725 9.19018C2.76465 9.28583 2.81936 9.41557 2.81936 9.55084C2.81936 9.68611 2.76465 9.81585 2.66725 9.9115C2.56985 10.0072 2.43775 10.0609 2.30001 10.0609C2.16227 10.0609 2.03017 10.0072 1.93277 9.9115C1.83537 9.81585 1.78065 9.68611 1.78065 9.55084C1.78065 9.41557 1.83537 9.28583 1.93277 9.19018C2.03017 9.09453 2.16227 9.04079 2.30001 9.04079ZM18.4 2.9202V10.0609C18.4 10.6251 18.8642 11.081 19.4387 11.081H20.4774C21.052 11.081 21.5161 10.6251 21.5161 10.0609V3.43025C21.5161 3.14972 21.2824 2.9202 20.9968 2.9202H18.4ZM19.4387 9.55084C19.4387 9.41557 19.4934 9.28583 19.5908 9.19018C19.6882 9.09453 19.8203 9.04079 19.9581 9.04079C20.0958 9.04079 20.2279 9.09453 20.3253 9.19018C20.4227 9.28583 20.4774 9.41557 20.4774 9.55084C20.4774 9.68611 20.4227 9.81585 20.3253 9.9115C20.2279 10.0072 20.0958 10.0609 19.9581 10.0609C19.8203 10.0609 19.6882 10.0072 19.5908 9.9115C19.4934 9.81585 19.4387 9.68611 19.4387 9.55084Z"
                                                            fill="#27853F" />
                                                    </svg>

                                                </div>
                                                <p class="text-sm font-medium">Develop multiyear funder-nonprofit
                                                    partnerships</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <svg width="9" height="14" viewBox="0 0 9 14" fill="none"
                                                        xmlns="http://www.w3.org/2000/svg">
                                                        <path
                                                            d="M1 0.25H8.5L7.75 1.75H5.305C5.665 2.185 5.935 2.695 6.0925 3.25H8.5L7.75 4.75H6.25C6.1568 5.68497 5.75056 6.56106 5.09714 7.23626C4.44372 7.91146 3.58141 8.3462 2.65 8.47V8.5H2.125L6.625 13.75H4.75L0.25 8.5V7H2.125C3.445 7 4.54 6.025 4.72 4.75H0.25L1 3.25H4.495C4.075 2.365 3.175 1.75 2.125 1.75H0.25L1 0.25Z"
                                                            fill="#27853F" />
                                                    </svg>

                                                </div>
                                                <p class="text-sm font-medium">Pay a fair share of core costs</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"
                                                        xmlns="http://www.w3.org/2000/svg">
                                                        <path fill-rule="evenodd" clip-rule="evenodd"
                                                            d="M11.1968 0.436482C11.3088 0.323511 11.4517 0.24657 11.6072 0.21543C11.7628 0.184291 11.924 0.20036 12.0704 0.261595L14.3392 1.20792C14.5349 1.28918 14.6906 1.44513 14.7721 1.64161C14.8537 1.83808 14.8545 2.05907 14.7744 2.25617L13.8475 4.53828C13.7876 4.68564 13.6856 4.81183 13.5544 4.90087C13.4232 4.98991 13.2687 5.03781 13.1105 5.0385C12.9522 5.03919 12.7973 4.99264 12.6653 4.90474C12.5333 4.81685 12.4303 4.69155 12.3691 4.54472L12.0032 3.66492L2.78938 7.62509C2.69273 7.66666 2.58888 7.68866 2.48377 7.68986C2.37867 7.69106 2.27435 7.67142 2.17679 7.63206C2.07922 7.59271 1.99032 7.53441 1.91516 7.4605C1.83999 7.38658 1.78004 7.2985 1.73872 7.20128C1.69739 7.10406 1.67551 6.99961 1.67432 6.89388C1.67313 6.78816 1.69266 6.68323 1.73178 6.58509C1.77091 6.48696 1.82886 6.39753 1.90235 6.32193C1.97583 6.24632 2.0634 6.18602 2.16005 6.14445L11.3856 2.17999L11.0262 1.31628C10.9647 1.16914 10.9481 1.00693 10.9784 0.850265C11.0088 0.693602 11.0849 0.549569 11.1968 0.436482ZM14.1334 6.08008C14.4163 6.08008 14.6876 6.19312 14.8876 6.39433C15.0877 6.59554 15.2 6.86844 15.2 7.153V14.6635C15.2 14.8058 15.1439 14.9422 15.0438 15.0428C14.9438 15.1434 14.8082 15.2 14.6667 15.2H12C11.8586 15.2 11.7229 15.1434 11.6229 15.0428C11.5229 14.9422 11.4667 14.8058 11.4667 14.6635V7.153C11.4667 6.86844 11.5791 6.59554 11.7791 6.39433C11.9792 6.19312 12.2505 6.08008 12.5334 6.08008H14.1334ZM9.55418 8.00276C9.35401 7.80193 9.08277 7.68924 8.80005 7.68947H7.20005C6.91715 7.68947 6.64584 7.80251 6.4458 8.00372C6.24576 8.20493 6.13338 8.47783 6.13338 8.76239V14.6635C6.13338 14.8058 6.18957 14.9422 6.28959 15.0428C6.38961 15.1434 6.52527 15.2 6.66672 15.2H9.33338C9.47483 15.2 9.61049 15.1434 9.71051 15.0428C9.81052 14.9422 9.86671 14.8058 9.86671 14.6635V8.76239C9.86683 8.62132 9.83928 8.48162 9.78565 8.35127C9.73202 8.22093 9.65336 8.10249 9.55418 8.00276ZM3.46672 9.29885C3.74961 9.29885 4.02092 9.41189 4.22096 9.61311C4.421 9.81432 4.53338 10.0872 4.53338 10.3718V14.6635C4.53338 14.8058 4.47719 14.9422 4.37717 15.0428C4.27715 15.1434 4.1415 15.2 4.00005 15.2H1.33338C1.19193 15.2 1.05628 15.1434 0.956259 15.0428C0.856239 14.9422 0.800049 14.8058 0.800049 14.6635V10.3718C0.800049 10.0872 0.912429 9.81432 1.11247 9.61311C1.31251 9.41189 1.58382 9.29885 1.86672 9.29885H3.46672Z"
                                                            fill="#27853F" />
                                                    </svg>

                                                </div>
                                                <p class="text-sm font-medium">Invest in organizational development</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <svg width="16" height="12" viewBox="0 0 16 12" fill="none"
                                                        xmlns="http://www.w3.org/2000/svg">
                                                        <path
                                                            d="M12.9613 0.159011C13.0511 0.229106 13.1238 0.318762 13.1739 0.421168C13.2239 0.523574 13.2499 0.636036 13.25 0.750011V2.32576C13.848 2.93542 14.2882 3.68174 14.5325 4.50001H14.75C14.9489 4.50001 15.1397 4.57903 15.2803 4.71968C15.421 4.86033 15.5 5.0511 15.5 5.25001V7.50001C15.4999 7.63926 15.4611 7.77573 15.3878 7.89416C15.3146 8.01258 15.2098 8.10827 15.0853 8.17051L13.9932 8.71726C13.6125 9.3465 13.1037 9.88871 12.5 10.3088V11.25C12.5 11.4489 12.421 11.6397 12.2803 11.7803C12.1397 11.921 11.9489 12 11.75 12H9.5C9.30109 12 9.11032 11.921 8.96967 11.7803C8.82902 11.6397 8.75 11.4489 8.75 11.25H8C8 11.4489 7.92098 11.6397 7.78033 11.7803C7.63968 11.921 7.44891 12 7.25 12H5C4.80109 12 4.61032 11.921 4.46967 11.7803C4.32902 11.6397 4.25 11.4489 4.25 11.25V10.3088C3.2541 9.61569 2.529 8.59907 2.198 7.43176C1.71254 7.30891 1.28194 7.02762 0.974385 6.63244C0.666826 6.23726 0.499886 5.75077 0.5 5.25001V4.87501C0.5 4.6761 0.579018 4.48533 0.71967 4.34468C0.860322 4.20403 1.05109 4.12501 1.25 4.12501C1.44891 4.12501 1.63968 4.20403 1.78033 4.34468C1.92098 4.48533 2 4.6761 2 4.87501V5.25001C1.99983 5.31896 2.00917 5.38761 2.02775 5.45401C2.16274 4.16307 2.77116 2.9679 3.73558 2.09919C4.69999 1.23049 5.95202 0.749833 7.25 0.750011H9.40775L12.3177 0.0225113C12.4283 -0.00513154 12.5438 -0.00720597 12.6553 0.0164463C12.7668 0.0400986 12.8714 0.0888551 12.9613 0.159011ZM11.375 3.75001C11.0766 3.75001 10.7905 3.86854 10.5795 4.07952C10.3685 4.29049 10.25 4.57664 10.25 4.87501C10.25 5.17338 10.3685 5.45953 10.5795 5.67051C10.7905 5.88148 11.0766 6.00001 11.375 6.00001C11.6734 6.00001 11.9595 5.88148 12.1705 5.67051C12.3815 5.45953 12.5 5.17338 12.5 4.87501C12.5 4.57664 12.3815 4.29049 12.1705 4.07952C11.9595 3.86854 11.6734 3.75001 11.375 3.75001Z"
                                                            fill="#27853F" />
                                                    </svg>

                                                </div>
                                                <p class="text-sm font-medium">Build financial resilience</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                        <div class="flex justify-between items-center gap-1">
                                            <div class="flex gap-2 pt-3 items-center">
                                                <div
                                                    class="w-7 h-7 min-w-7 rounded-full bg-gray-200 flex justify-center items-center">
                                                    <svg width="16" height="15" viewBox="0 0 16 15" fill="none"
                                                        xmlns="http://www.w3.org/2000/svg">
                                                        <path
                                                            d="M0.5 14.75V13.25H7.25V4.86875C6.925 4.75625 6.64375 4.58125 6.40625 4.34375C6.16875 4.10625 5.99375 3.825 5.88125 3.5H3.5L5.75 8.75C5.75 9.375 5.49375 9.90625 4.98125 10.3438C4.46875 10.7813 3.85 11 3.125 11C2.4 11 1.78125 10.7813 1.26875 10.3438C0.75625 9.90625 0.5 9.375 0.5 8.75L2.75 3.5H1.25V2H5.88125C6.03125 1.5625 6.3 1.20325 6.6875 0.922251C7.075 0.641251 7.5125 0.500501 8 0.500001C8.4875 0.499501 8.925 0.640251 9.3125 0.922251C9.7 1.20425 9.96875 1.5635 10.1187 2H14.75V3.5H13.25L15.5 8.75C15.5 9.375 15.2438 9.90625 14.7313 10.3438C14.2188 10.7813 13.6 11 12.875 11C12.15 11 11.5312 10.7813 11.0187 10.3438C10.5062 9.90625 10.25 9.375 10.25 8.75L12.5 3.5H10.1187C10.0062 3.825 9.83125 4.10625 9.59375 4.34375C9.35625 4.58125 9.075 4.75625 8.75 4.86875V13.25H15.5V14.75H0.5ZM11.4688 8.75H14.2812L12.875 5.4875L11.4688 8.75ZM1.71875 8.75H4.53125L3.125 5.4875L1.71875 8.75ZM8 3.5C8.2125 3.5 8.39075 3.428 8.53475 3.284C8.67875 3.14 8.7505 2.962 8.75 2.75C8.7495 2.538 8.6775 2.36 8.534 2.216C8.3905 2.072 8.2125 2 8 2C7.7875 2 7.6095 2.072 7.466 2.216C7.3225 2.36 7.2505 2.538 7.25 2.75C7.2495 2.962 7.3215 3.14025 7.466 3.28475C7.6105 3.42925 7.7885 3.501 8 3.5Z"
                                                            fill="#27853F" />
                                                    </svg>

                                                </div>
                                                <p class="text-sm font-medium">Embed diversity, equity and inclusion in
                                                    grantmaking</p>
                                            </div>
                                            <p class="text-primary text-sm cursor-pointer">View</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { Download, X } from 'lucide-vue-next'

const open = ref(false)
const open_ass = ref(false)
const condision = ref(false)
const isActive = ref(false);

const props = defineProps({
    disabled: {
        type: Boolean,
        default: false
    }
})
const openDialog = () => {
    open.value = true;
}
const assessment = () => {
    open.value = false;
    open_ass.value = true;
}

</script>