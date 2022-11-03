import axios from 'axios';

const API_URL = 'http://localhost:8000';


export default class ShopsProductsService {

    constructor(){}

    getShops(){
        const url = `${API_URL}/api/v1/shops/`;
        return axios.get(url).then((response) => response.data);
    }

    getProducts(){
        const url = `${API_URL}/api/v1/product/list/`;
        return axios.get(url).then((response) => response.data);
    }

    getProduct(slug){
        const url = `${API_URL}/api/v1/product/${slug}/`;
        return axios.get(url).then((response) => response.data);
    }

    getProductsForShop(pk){
        const url = `${API_URL}/api/v1/product/list/?shop=${pk}/`;
        return axios.get(url).then((response) => response.data);
    }

    getProductsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then((response) => response.data);
    }

    addProductToCart(pk) {
        // let data = {product: product, quantity: 1, cart: null, order: null, sub_total: product.price};
        const url = `${API_URL}/cart/${pk}/add/`;
        const config = {headers: {"HTTP_REFERER": window.location.href, "Accept": "application/json",
        "Access-Control-Allow-Origin": "*",
        "X-Requested-With": "XMLHttpRequest",
        "Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"}};
        return axios.get(url).then((response) => {
            console.log('in cart');
            console.log(response);
            return response.data;
        });
    }
}