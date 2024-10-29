import './index.css';
import { createApp, reactive } from "vue";
import App from "./App.vue";

import router from './router';
import resourceManager from "./libs/resourceManager";
import call from "./libs/controllers/call";
import socket from "./libs/controllers/socket";
import Auth from "./libs/controllers/auth";

const app = createApp(App);
const auth = reactive(new Auth());

// Plugins
app.use(router);
app.use(resourceManager);

// Global Properties,
// components can inject this
app.provide("$auth", auth);
app.provide("$call", call);
app.provide("$socket", socket);


app.mount("#app");
