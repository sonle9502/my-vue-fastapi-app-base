import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import { useAuthStore } from "@/stores/authStore";

async function bootstrap() {
  const app = createApp(App);
  const pinia = createPinia();

  app.use(pinia);

  const auth = useAuthStore(pinia);

  // 🔥 CHỜ Keycloak init xong
  await auth.initAuth();

  app.use(router);

  app.mount("#app");
}

bootstrap();