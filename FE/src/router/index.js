import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/authStore";

import Login from "@/views/auth/LoginView.vue";
import Dashboard from "@/views/dashboard/DashboardView.vue";
import Profile from "@/views/profile/Profile.vue";


const routes = [
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/",
    component: Dashboard,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/profile",
    component: Profile,
    meta: {
      requiresAuth: true,
    },
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to) => {
  const auth = useAuthStore();

  if (!auth.initialized) {
    await auth.initAuth(); // QUAN TRỌNG
  }

  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    return "/login";
  }

  if (to.path === "/login" && auth.isAuthenticated) {
    return "/";
  }
});

export default router;