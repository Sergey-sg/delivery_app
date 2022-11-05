import { IShop } from "./shop.interface";

export interface IProduct {
  pk: number;
  name: string;
  shop?: IShop;
  slug: string;
  description?: string;
  price: number;
  image?: string;
  img_alt?: string;
  stock?: number;
  available: boolean;
}
