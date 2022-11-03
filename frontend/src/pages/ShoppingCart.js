import React, {Component} from "react";
import CartService from "./CartService";

const cartService = new CartService;

export default class ShoppingCart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            cartItems: [],
            customer: {
                address: '',
                geolocation: '',
                name: '',
                email: '',
                phone: ''
            },
            nextPageURL: '',
            previousPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.previousPage = this.previousPage.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.domain = `${window.location.href.split('/')[0]}//${window.location.href.split('/')[2]}`;
    }

    componentDidMount() {
        cartService.getCartItems().then((result) => {
            this.setState({cartItems: result.results, nextPageURL: result.next, previousPageURL: result.previous});
        });
    }

    nextPage() {
        cartService.getCartItemsByURL(this.state.nextPageURL).then((result) => {
            this.setState({cartItems: result.results, nextPageURL: result.next, previousPageURL: result.previous});
        });
    }

    previousPage() {
        cartService.getCartItemsByURL(this.state.previousPageURL).then((result) => {
            this.setState({cartItems: result.results, nextPageURL: result.next, previousPageURL: result.previous});
        });
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        this.setState((state) => {
            state.customer[name] = value;
        });
    }

    handleSubmit(event) {
        console.log(this.state.customer);
        event.preventDefault();
    }

    render() {
        if (this.state.cartItems[0]) {
            return (
                <div>
                    <form action="" method="post" onSubmit={this.handleSubmit}>
                        <div className="row">
                            <div className="container col-lg-5 col-md-5 col-sm-10 border rounded">
                                <table id="table">
                                    <br/>
                                    <tr><label>Address:</label></tr>
                                    <input name="address" type="text" onChange={this.handleInputChange}/>
                                    <tr><label>Geolocation:</label></tr>
                                    <input name="geolocation" type="text" onChange={this.handleInputChange}/>
                                    <tr><label>Name:</label></tr>
                                    <input name="name" type="text" onChange={this.handleInputChange}/>
                                    <tr><label>Email:</label></tr>
                                    <input name="email" type="email" onChange={this.handleInputChange}/>
                                    <tr><label>Phone:</label></tr> 
                                    <input name="phone" type="text" onChange={this.handleInputChange}/>
                                </table>
                            </div>
                            <div id="cart-items" className="container col-lg-6 col-md-6 col-sm-10 border rounded">
                                <table className="table cart-table">
                                    <thead className="cart-thead">
                                        <tr>
                                            <th colSpan="4">
                                                Your items
                                            </th>
                                        </tr>
                                    </thead>
                                        <tbody>
                                            {this.state.cartItems.map(cartItem =>
                                                <tr key={cartItem.pk}>
                                                    <td>
                                                        <a href={`/product/${cartItem.product.slug}`}><img id="order-product-image" src={cartItem.product.image} alt={cartItem.product.img_alt }/></a>
                                                    </td>
                                                    <td className="text-start">
                                                        <a href={`/product/${cartItem.product.slug}`}>
                                                            {cartItem.product.name}
                                                        </a>
                                                        <br/>
                                                        Price: {cartItem.product.price}
                                                        <br/>
                                                        <div id="quantity">Quantity: {cartItem.quantity} x {cartItem.product.name}</div>
                                                    </td>
                                                    <td>
                                                        ${cartItem.sub_total}
                                                    </td>
                                                    <td>
                                                        <a href="{{ url('add_cart', cart_item.product_id) }}" className="add-cart" data-id="{{ cart_item.product.id }}" data-name="{{ cart_item.product.name }}"><i className="material-icons cart-icon">add_shopping_cart</i></a>
                                                        <a href="{{ url('cart_remove', cart_item.product_id) }}"><i className="material-icons cart-icon">remove_circle_outline</i></a>
                                                        <a href="{{ url('cart_remove_product', cart_item.product_id) }}"><i className="material-icons cart-icon">delete</i></a>
                                                    </td>
                                                </tr>)}    
                                        </tbody>
                                </table>
                            </div>
                            <div className="container">
                                <br/>
                                <div id="order-footer" className="text-end">
                                    Total price: <strong id="total-price">$total </strong>
                                    <input id="submit-order" className="btn btn-primary text-black" type="submit" value="Submit"/>
                                </div>
                            </div>
                        </div>
                    </form>  
                </div>    
            )
        }
        return (
            <div className="text-center">
                <br/>
                <h1 className="text-center product_title">
                    Your cart is empty
                </h1>
                <br/>
                <p className="text-center">
                    Click <a href={this.domain}>here</a> to go back to products
                </p>
            </div>
        )        
    }
}