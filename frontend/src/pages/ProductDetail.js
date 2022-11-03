import React, { Component } from 'react';
import ShopsProductsService from './ShopsProductsService';


const shopsProductsService = new ShopsProductsService();


export default class ProductDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {
            product: []
        }
    }

    componentDidMount() {
        const productSlug = window.location.href.split('/')[4];
        if (productSlug){
            shopsProductsService.getProduct(productSlug).then((result) => {
                this.setState({product: result});
            });
        }
    }

    render() {
        return (
            <div className="container-fluid bg-dark me-md-3 pt-3 px-3 pt-md-5 px-md-5 text-white overflow-hidden">
                <div className="my-3 py-3">
                    <h2 className="display-5 text-center">{this.state.product.name}</h2>
                    <p className="lead">{this.state.product.description}</p>
                    <div>price: {this.state.product.price}$</div>
                    <div>stock: {this.state.product.stock}</div>
                    <button className="btn btn-primary add-cart" data-id={this.state.product.id} data-name={this.state.product.name}>Add to cart</button>
                </div>
                <div className="bg-light shadow-sm mx-auto product-img-detail">
                    <p className="text-center">
                        <img src={this.state.product.image} alt={ this.state.product.img_alt } width="50%" />
                    </p>
                </div>
                <p className="text-center">
                    View all products of
                    <a href={"/shop/" + this.state.product.shop}>
                        {this.state.product.shop}
                    </a>
                </p>
            </div>
        )
    }
}