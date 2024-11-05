import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home/Home.vue";
import RecommendedPrinciples from '../views/RecommendedPrinciples.vue';
import FunderDiagnostic from '../views/FunderDiagnostic.vue';
import SubRoute from '../views/Assessment/SubRoute.vue';
import Assessment from '../views/Assessment/Assessment.vue';

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/recommended",
    name: "Recommended",
    component: RecommendedPrinciples,
  },
  {
    path: "/funder-diagnostic",
    name: "Funder",
    component: FunderDiagnostic,
  },
  {
    path: '/funder',
    name: 'Assessment',
    component: SubRoute,
    children: []  
  }
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory('/pwit'),
  routes,
});
 
export const initializeDynamicRoutes = async () => {
  try {
    const res = await fetch('/api/method/pwit.controllers.api.route');
    const routeList = await res.json();
    const funderRoutes = routeList?.message?.data?.map(route => ({
      ...route,
      component: Assessment,  
    }));
 
    for (const route of funderRoutes) {
      router.addRoute('Assessment', route);
    }
  } catch (error) {
    console.error("Failed to fetch routes:", error);
  }
};

export default router;
