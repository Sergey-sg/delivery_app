import { configureStore, ThunkAction, Action } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import errorSlice from './loader/error.slice';
import loaderSlice from './loader/loader.slice';
import successSlice from './loader/success.slice';
import userSlice from './authService/auth.slice';
import shopSlice from './shopService/shop.slice';
import productSlice from './productService/product.slice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
    user: userSlice,
    success: successSlice,
    error: errorSlice,
    loader: loaderSlice,
    shops: shopSlice,
    products: productSlice
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
