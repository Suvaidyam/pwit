import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home/Home.vue";
import RecommendedPrinciples from '../views/RecommendedPrinciples.vue';
import FunderDiagnostic from '../views/FunderDiagnostic.vue';
import SubRoute from '../views/Assessment/SubRoute.vue';
import Assessment from '../views/Assessment/Assessment.vue';
import NotFound from '../views/NotFound.vue';
import Results from "../views/Assessment/Results.vue";

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
    path: "/:pathMatch(.*)*",  
    name: "NotFound",
    component: NotFound,
  },
  {
    path: '/funder',
    name: 'Assessment',
    component: SubRoute,
    children: [{
      path:':category/results',
      name: 'Results',
      component: Results
    }]
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

router.beforeEach(async (to, from, next) => {
  const session = JSON.parse(localStorage.getItem('session'))?.data?.name;
  if (to.name && from.name) {
    await fetch('/api/method/pwit.controllers.api.set_route_logs', {
      method: 'POST',
      body: JSON.stringify({ session: session, route: from.name + '/' + to.name }),
      headers: {
        'Content-Type': 'application/json',
      }
    });
  }
  next();
});

export default router;
