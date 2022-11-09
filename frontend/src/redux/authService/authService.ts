import { AxiosError } from "axios";
import { api } from "../../interceptors/axios";
import { ILoginParams } from "../../interfaces/login.interface";
import { errorOccurred, resetError } from "../loader/error.slice";
import { startLoading, stopLoading } from "../loader/loader.slice";
import { resetSuccess, successAction } from "../loader/success.slice";
import { AppDispatch } from "../store";
import { initialUser, removeUserSuccess } from "./auth.slice";

export const fetchCurrentAuthUser = () => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(resetSuccess());
      dispatch(startLoading());

      const response = await api.get("/auth/users/current");

      dispatch(initialUser(response?.data));
      dispatch(successAction({ message: "user in stor" }));
    } catch (e) {
      const axiosErr = e as AxiosError;
      const status = axiosErr.response?.status;
      const message = axiosErr.message;

      dispatch(errorOccurred({ statusCode: status, message: message }));
    } finally {
      dispatch(stopLoading());
    }
  };
};

export const fetchLogin = (authParams: ILoginParams) => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(resetSuccess());
      dispatch(startLoading());

      const response = await api.post("/auth/token/", authParams);

      localStorage.clear();
      localStorage.setItem("access_token", response?.data.access);
      localStorage.setItem("refresh_token", response?.data.refresh);

      dispatch(fetchCurrentAuthUser())
      dispatch(successAction({ message: "login success" }));
    } catch (e: any) {
      let message;
      const axiosErr = e as AxiosError;
      const status = axiosErr.response?.status;
      if (e.response?.data.detail === 'No active account found with the given credentials') {
        message = e.response?.data.detail;
      } else {
        message = axiosErr.message;
      }
      dispatch(errorOccurred({ statusCode: status, message: message }));
    } finally {
      dispatch(stopLoading());
    }
  };
};

export const fetchLogout = () => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(resetSuccess());
      dispatch(startLoading());

      await api.post("/auth/logout/", {
        refresh_token: localStorage.getItem("refresh_token"),
      });

      localStorage.clear();
      api.defaults.headers.common.Authorization = null;

      dispatch(removeUserSuccess());
      dispatch(successAction({ message: "logout success" }));
    } catch (e) {
      const axiosErr = e as AxiosError;
      const status = axiosErr.response?.status;
      const message = axiosErr.message;

      dispatch(errorOccurred({ statusCode: status, message: message }));
    } finally {
      dispatch(stopLoading());
    }
  };
};
