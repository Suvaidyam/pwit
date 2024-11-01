import { reactive, ref } from 'vue';

const auth = ref('');  
const sidebar = ref(false);  
export const store = reactive({ 
    auth:auth.value,
    sidebar:sidebar.value
});
