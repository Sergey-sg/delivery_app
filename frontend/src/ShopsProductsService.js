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
        const url = `${API_URL}/api/v1/product/list/${slug}/`;
        return axios.get(url).then((response) => response.data);
    }

    getProductsForShop(pk){
        const url = `${API_URL}/api/v1/product/list/?shop=${pk}`;
        return axios.get(url).then((response) => response.data);
    }

    getProductsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then((response) => response.data);
    }
}