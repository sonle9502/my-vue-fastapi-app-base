import http from "./http";

export const getProfileApi = () => {
  return http.get("/api/me");
};

export const updateProfileApi = (data) => {
  return http.put("/api/me", data);
};