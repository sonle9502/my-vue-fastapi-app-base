import { getProfileApi, updateProfileApi } from "@/api/profileApi";

export const profileService = {
  async getProfile() {
    const res = await getProfileApi();
    return res.data;
  },

  async updateProfile(payload) {
    const res = await updateProfileApi(payload);
    return res.data;
  },
};