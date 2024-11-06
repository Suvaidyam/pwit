import { reactive, ref } from 'vue';

const auth = ref('');  
const session = ref(JSON.parse(localStorage.getItem('session'))?.data?.name);
const sidebar = ref(false);  
const funder_loading = ref(false);  
export const store = reactive({ 
    auth:auth.value,
    sidebar:sidebar.value,
    session:session.value,
    funder_loading:funder_loading.value
});
