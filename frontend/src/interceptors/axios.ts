import axios from "axios";

export const api = axios.create({
  baseURL: process.env.BACKEND_URL || 'http://localhost:8000/api/v1',
  withCredentials: true,
})


api.interceptors.request.use((config: any) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem('access_token')}`
  return config
})

api.interceptors.response.use(
  (resp) => resp,
  async (error) => {
    let refresh = false;
    if (error.response?.status === 401 && !refresh) {
      refresh = true;

      const response = await api.post("/token/refresh/", { refresh: localStorage.getItem("refresh_token") });

      if (response.status === 200) {
        api.defaults.headers.common.Authorization = `Bearer ${response.data.access}`;

        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        return axios(error.config);
      }
    }
    refresh = false;

    return error;
  }
);
