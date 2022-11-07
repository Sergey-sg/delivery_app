import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { IUser } from "../../interfaces/user.interface";

const initialState: IUser = {
  pk: "",
  first_name: "",
  last_name: "",
  email: "",
  address: "",
  phone_number: "",
  photo: "",
  img_alt: "",
  isAuth: false,
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    initialUser: (state, action: PayloadAction<IUser>) => ({
      ...state,
      ...action.payload,
      isAuth: true,
    }),
    updateUserSuccess: (state, action: PayloadAction<IUser>) => ({
      ...state,
      ...action.payload,
    }),
    removeUserSuccess: () => ({ ...initialState }),
  },
});

export const {
    initialUser,
    updateUserSuccess,
    removeUserSuccess,
} = userSlice.actions;

export default userSlice.reducer;