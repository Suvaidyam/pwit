import './index.css';
import { createApp, reactive } from "vue";
import App from "./App.vue";

import router, { initializeDynamicRoutes } from './router';
import resourceManager from "./libs/resourceManager";
import call from "./libs/controllers/call";
import socket from "./libs/controllers/socket";
import Auth from "./libs/controllers/auth";
import {FeatherIcon} from 'frappe-ui';
import { store } from "./Store";
import {session} from './data/session'

initializeDynamicRoutes().then(() => {
    
    const app = createApp(App);
    const auth = reactive(new Auth());
    app.provide('store', store);
    
    // Plugins
    app.use(router);
    app.use(resourceManager);
    app.component("FeatherIcon",FeatherIcon)
    // Global Properties,
    // components can inject this
    app.provide("$auth", auth);
    app.provide("$call", call);
    app.provide("$socket", socket);
    app.provide("$session", session);
    
    (function addGoogleAnalyticsScript() {
      const script = document.createElement('script');
      script.async = true;
      script.src = 'https://www.googletagmanager.com/gtag/js?id=G-SXKY993N5R';
      document.head.appendChild(script);
    
      script.onload = () => {
        window.dataLayer = window.dataLayer || [];
        function gtag() { window.dataLayer.push(arguments); }
        window.gtag = gtag;
        gtag('js', new Date());
        gtag('config', 'G-SXKY993N5R'); // Replace with your Measurement ID
      };
    })();
    
    // Track Page Views Dynamically
    router.afterEach((to) => {
      if (window.gtag) {
        window.gtag('config', 'G-SXKY993N5R', {
          page_path: to.fullPath,
        });
      }
    });
   
    app.mount("#app");
  });

