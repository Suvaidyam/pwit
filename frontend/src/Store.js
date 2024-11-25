import { reactive, ref } from 'vue';

const auth = ref(false); 
const authPopup = ref(false); 
const isOpen = ref(false);
const isForgetPas = ref(false);
const isOpenPas = ref(false);
const session = ref(JSON.parse(localStorage.getItem('session'))?.data?.name);
const sidebar = ref(false);
const save_as_login = ref(false);
export const store = reactive({ 
    auth:auth.value,
    sidebar:sidebar.value,
    session:session.value,
    isOpen:isOpen.value,
    isOpenPas:isOpenPas.value,
    isForgetPas:isForgetPas.value,
    save_as_login:save_as_login.value,
    authPopup:authPopup.value,
});
