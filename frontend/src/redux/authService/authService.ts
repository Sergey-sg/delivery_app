import { AxiosError } from "axios";
import { api } from "../../interceptors/axios";
import { ILoginParams } from "../../interfaces/login.interface";
import { errorOccurred, resetError } from "../loader/error.slice";
import { startLoading } from "../loader/loader.slice";
import { resetSuccess, successAction } from "../loader/success.slice";
import { AppDispatch } from "../store";
import { initialUser } from "./auth.slice";

const getCurrentAuthUser = () => {
  return api.get("/users/current");
};

const login = async (authParams: ILoginParams) => {
  return await api.post("/token/", authParams);
};

export const fetchCurrentAuthUser = () => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(resetSuccess());
      dispatch(startLoading());

      const response = await getCurrentAuthUser();

      dispatch(initialUser(response.data));
      dispatch(successAction({ message: "user in stor" }));
    } catch (e) {
      const axiosErr = e as AxiosError;
      const status = axiosErr.response?.status;
      const message = axiosErr.message;

      dispatch(errorOccurred({ statusCode: status, message: message }));
    }
  };
};

export const fetchLogin = (authParams: ILoginParams) => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(resetSuccess());
      dispatch(startLoading());

      const response = await login(authParams);

      localStorage.clear();
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);

      api.defaults.headers.common.Authorization = `Bearer ${response.data.access}`;

      dispatch(successAction({ message: "login success" }));
    } catch (e) {
      const axiosErr = e as AxiosError;
      const status = axiosErr.response?.status;
      const message = axiosErr.message;

      dispatch(errorOccurred({ statusCode: status, message: message }));
    }
  };
};
