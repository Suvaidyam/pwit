import { reactive, ref } from 'vue';

const auth = ref('');  
export const store = reactive({ 
    auth:auth.value,
});
