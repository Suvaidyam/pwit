import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';
import RecommendedPrinciples from '../views/RecommendedPrinciples.vue'
import FunderDiagnostic from '../views/FunderDiagnostic.vue'
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
  ...authRoutes,
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory('/pwit'),
  routes,
});

export default router;
