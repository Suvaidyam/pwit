import { reactive, ref } from 'vue';

const auth = ref('');  
const session = ref(JSON.parse(localStorage.getItem('session'))?.data?.name);
// if(!session.value){
//     session.value = JSON.parse(localStorage.getItem('session'))?.data?.name;
// } 
const sidebar = ref(false);  
export const store = reactive({ 
    auth:auth.value,
    sidebar:sidebar.value,
    session:session.value,
});
