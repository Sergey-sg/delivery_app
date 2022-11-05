export interface IUser {
  pk?: number | string;
  first_name: string;
  last_name: string;
  email: string;
  address: string;
  phone_number: string;
  photo?: string;
  img_alt?: string;
  password?: string;
}
