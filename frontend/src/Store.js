import { reactive, ref } from 'vue';

const auth = ref(false);  
const isOpen = ref(false);
const isOpenPas = ref(false);
const session = ref(JSON.parse(localStorage.getItem('session'))?.data?.name);
const sidebar = ref(false);  
export const store = reactive({ 
    auth:auth.value,
    sidebar:sidebar.value,
    session:session.value,
    isOpen:isOpen.value,
    isOpenPas:isOpenPas.value
});
