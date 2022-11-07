import { AxiosError } from "axios";
import { api } from "../../interceptors/axios";
import { resetError, errorOccurred } from "../loader/error.slice";
import { startLoading, stopLoading } from "../loader/loader.slice";
import { successAction } from "../loader/success.slice";
import { AppDispatch } from "../store";
import { initialProducts } from "./product.slice";

const getOneProductBySlug = (slug: string) => {
  return api.get(`shop/product/${slug}/`);
};

const getProductsByURL = (link: string) => {
  return api.get(`shop/${link}/`);
};

const addProductToCart = (pk: number) => {
  // let data = {product: product, quantity: 1, cart: null, order: null, sub_total: product.price};
  return api.get(`cart/${pk}/add/`);
};

export const fetchAllProducts = () => {
  return async (dispatch: AppDispatch) => {
    try {
      dispatch(resetError());
      dispatch(startLoading());

      const response = await api.get("shop/product/list/");

      dispatch(initialProducts(response?.data.results));
      dispatch(successAction({ message: 'Products list loaded successfully' }));
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

export const fetchAllProductsForShop = (pk: string) => {
    return async (dispatch: AppDispatch) => {
      try {
        dispatch(resetError());
        dispatch(startLoading());
  
        const response = await api.get(`shop/product/list/?shop=${pk}`);
  
        dispatch(initialProducts(response?.data.results));
        dispatch(successAction({ message: 'Products list for shop loaded successfully' }));
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
