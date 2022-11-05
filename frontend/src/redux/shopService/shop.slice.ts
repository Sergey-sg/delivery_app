import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { IShop } from "../../interfaces/shop.interface";

const initialState: IShop[] = [];

const shopSlice = createSlice({
  name: "shops",
  initialState,
  reducers: {
    initialShops: (state, action: PayloadAction<IShop[]>) => [
      ...action.payload,
    ]
  }
});

export const {
  initialShops,
} = shopSlice.actions;

export default shopSlice.reducer;
