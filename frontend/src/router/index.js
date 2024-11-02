import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import authRoutes from './auth';
import RecommendedPrinciples from '../views/RecommendedPrinciples.vue'
import FunderDiagnostic from '../views/FunderDiagnostic.vue'
import SubRoute from '../views/funder/SubRoute.vue'
import CoreCosts from '../views/funder/CoreCosts.vue'
import MultiPartnerships from '../views/funder/MultiPartnerships.vue'
import OrganizationDev from '../views/funder/OrganizationDev.vue'
import DiversityEquity from '../views/funder/DiversityEquity.vue'
 
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
    path: "/funder",
    name: "Funders",
    component: SubRoute,
    children: [
      {
        path: "core-costs",
        name: "CoreCosts",
        component: CoreCosts,
      },
      {
        path: "multi-year-artnerships",
        name: "MultiPartnerships",
        component: MultiPartnerships,
      },
      {
        path: "organization-development",
        name: "OrganizationDev",
        component: OrganizationDev,
      },
      {
        path: "organization-development",
        name: "OrganizationDevelopment",
        component: CoreCosts,
      },
      {
        path: "rinancial-resilience",
        name: "FinancialResilience",
        component: CoreCosts,
      },
      {
        path: "diversity-equity-inclusion",
        name: "DiversityEquity",
        component: DiversityEquity,
      },
    ],
  },
  ...authRoutes,
];

const router = createRouter({
  base: "/frontend/",
  history: createWebHistory('/pwit'),
  routes,
});

export default router;
