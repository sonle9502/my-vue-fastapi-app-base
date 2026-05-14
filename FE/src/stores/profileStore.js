import { defineStore } from "pinia";
import { profileService } from "@/services/profileService";

export const useProfileStore = defineStore("profile", {
  state: () => ({
    profile: null,
    phone: null,
    loading: false,
    message: "",
  }),

  actions: {
    async fetchProfile() {
      this.loading = true;
      try {
        this.profile = await profileService.getProfile();
      } catch (err) {
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    async updateProfile() {
        try {

            const response = await profileService.updateProfile(this.profile);

            this.profile = response.profile;
            this.message = "Update successfully";
        
        } catch (err) {

            console.error(err);

            this.message = "Update failed";
        }
        }
    },
});