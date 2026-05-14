import { defineStore } from "pinia";
import keycloak from "@/auth/keycloak";
import { profileService } from "@/services/profileService";

export const useAuthStore = defineStore("auth", {

  state: () => ({
    initialized: false,
    isAuthenticated: false,
    token: null,
    user: null,
  }),

  actions: {

    async initAuth() {

      const authenticated = await keycloak.init({
        onLoad: "login-required",
        pkceMethod: "S256",
        checkLoginIframe: false,
      });

      console.log("🚀 initAuth called");

      this.isAuthenticated = authenticated;
      this.token = keycloak.token || null;
      this.initialized = true;

      // login rồi thì call backend
      if (authenticated) {

        await this.getMe();
      }
    },

    async getMe() {

      try {

        const user = await profileService.getProfile();

        this.user = user;
        return user;

      } catch (error) {

        console.error(error);
        return null;
      }
    },

    async loginWithKeycloak() {
      await keycloak.login();
    },

    async logout() {
      await keycloak.logout();
    },
  },
});