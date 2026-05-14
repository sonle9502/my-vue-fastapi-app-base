import axios from "axios";
import keycloak from "@/auth/keycloak";

const http = axios.create({
  baseURL: "http://localhost:8000",
});

http.interceptors.request.use((config) => {
  if (keycloak?.token) {
    config.headers.Authorization = `Bearer ${keycloak.token}`;
  }

  return config;
});

export default http;