import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default class CartService {
    constructor(){}

    getCartItems() {
        const url = `${API_URL}/api/v1/cart/detail`;
        let data = axios.get(url).then(response => response.data);
        console.log(data)
        return data;
    }

    getCustomersList() {
        const url = `${API_URL}/api/v1/cutomer`;
        return axios.get(url).then(response => response.data);
    }

    getCustomer(pk) {
        const url = `${API_URL}/api/v1/${pk}`;
        return axios(url).then(response => response.data);
    }

    getOrdersList() {
        const url = `${API_URL}/api/vi/order`;
        return axios(url).then(response => response.data);
    }

    getOrder(pk) {
        const url = `${API_URL}/api/v1/order/${pk}`;
        return axios(url).then(response => response.data);
    }

    getCartItemsByURL(link) {
        const url = `${API_URL}${link}`;
        return axios(url).then(response => response.data);
    }
}