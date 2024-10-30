import { reactive, ref } from 'vue';

const auth = ref('Log In');  
export const store = reactive({ 
    auth:auth.value,
});
