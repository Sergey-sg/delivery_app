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
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    initialUser: (state, action: PayloadAction<IUser>) => ({
      ...state,
      ...action.payload,
    }),
    updateUserSuccess: (state, action: PayloadAction<IUser>) => ({
      ...state,
      ...action.payload,
    }),
  },
});

export const {
    initialUser,
    updateUserSuccess,
} = userSlice.actions;

export default userSlice.reducer;