import { AxiosError } from "axios";
import { api } from "../../interceptors/axios";
import { resetError, errorOccurred } from "../loader/error.slice";
import { startLoading, stopLoading } from "../loader/loader.slice";
import { successAction } from "../loader/success.slice";
import { AppDispatch } from "../store";
import { initialShops } from "./shop.slice";

export const fetchAllShops = () => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(startLoading());

      const response = await api.get("shop/shops/");

      dispatch(initialShops(response?.data.results));
      dispatch(successAction({ message: "Shops list loaded successfully" }));
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
