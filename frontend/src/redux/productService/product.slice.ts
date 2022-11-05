import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { IProduct } from "../../interfaces/product.interface";

const initialState: IProduct[] = [];

const productSlice = createSlice({
  name: "products",
  initialState,
  reducers: {
    initialProducts: (state, action: PayloadAction<IProduct[]>) => [
      ...action.payload,
    ],
    updateProductSuccess: (state, action: PayloadAction<IProduct>) => [
      ...state,
      action.payload,
    ],
    addNewPageOfProducts: (state, action: PayloadAction<IProduct[]>) => [
      ...state,
      ...action.payload,
    ],
    removeProductSuccess: (state, action) => {
      state = state.filter((product) => product.pk !== action.payload);
    },
    setOneProduct: (state, action: PayloadAction<IProduct>) => [action.payload],
  },
});

export const {
  initialProducts,
  updateProductSuccess,
  addNewPageOfProducts,
  removeProductSuccess,
  setOneProduct,
} = productSlice.actions;

export default productSlice.reducer;
