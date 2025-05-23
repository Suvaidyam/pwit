import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home/Home.vue";
import RecommendedPrinciples from '../views/RecommendedPrinciples.vue';
import FunderDiagnostic from '../views/FunderDiagnostic.vue';
import SubRoute from '../views/Assessment/SubRoute.vue';
import Assessment from '../views/Assessment/Assessment.vue';
import NotFound from '../views/NotFound.vue';
import Results from "../views/Assessment/Results.vue";
import ChangePass from "../views/ChangePass.vue";
import ComingSoon from "../views/ComingSoon.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/coming-soon",
    name: "ComingSoon",
    component: ComingSoon,
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
    path: "/update-password",
    name: "ChangePass",
    component: ChangePass,
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
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
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
  const session = JSON.parse(sessionStorage.getItem('session'))?.data?.name;
  if (to.name && from.name) {
    await fetch('/api/method/pwit.controllers.api.set_route_logs', {
      method: 'POST',
      body: JSON.stringify({ session: session, from: from.name,to: to.name }),
      headers: {
        'Content-Type': 'application/json',
      }
    });
  }
  next();
});

export default router;
