import React, { Component } from 'react';
import ShopsProductsService from './ShopsProductsService';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';


const shopsProductsService = new ShopsProductsService();


export default class ProductList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            products: [],
            shops: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleFilterShop = this.handleFilterShop.bind(this);
    }

    componentDidMount() {
        const shopPk = parseInt(window.location.href.split('/')[4]);
        if (shopPk && typeof shopPk === 'number') {
            shopsProductsService.getProductsForShop(shopPk).then((result) => {
                this.setState({products: result.results, nextPageURL: result.next});
            })
        } else {
            shopsProductsService.getProducts().then((result) => {
                this.setState({products: result.results, nextPageURL: result.next});
            });
        }
        shopsProductsService.getShops().then((result) => {
            this.setState({shops: result.results, nextPageURL: result.next});
        });
    }

    handleFilterShop(e, pk) {
        shopsProductsService.getProductsForShop(pk).then((result) => {
            this.setState({products: result.results, nextPageURL: result.next});
        });
    }

    nextPage() {
        shopsProductsService.getProductsByURL(this.state.nextPageURL).then((result) => {
            this.setState({products: result.results, nextPageURL: result.next});
        });
    }    

    render() {
        return (
                <div className="row">
                <div className="container col-3 border rounded">
                    <div className="text-center">Shops:
                        <br/>
                        { this.state.shops?.map( shop => 
                            <p key={shop.pk}>
                                <a className="container border rounded btn btn-link" href={"/shop/" + shop.pk} onClick={(e) => this.handleFilterShop(e, shop.pk)}>
                                    <img className="shop-logo" src={ shop.image } alt={ shop.img_alt } />
                                    <br/>
                                    {shop.name}
                                </a>
                            </p>
                        )} 
                    </div>
                </div>
                <div id="product-items" className="container col-8 border rounded">
                    <br/>
                    <Row className="justify-content-evenly">
                        { this.state.products?.map( product => 
                            <Col xs={10} md={5} lg={5} key={product.pk}>
                                <Card>
                                    <a href={"/product/" + product.slug }>
                                        <Card.Img variant="top" src={ product.image } alt={ product.img_alt }/>
                                    </a>
                                    <Card.Body>
                                        <Card.Title><h5><a href={ "product/" + product.slug }>{ product.name }</a></h5></Card.Title>
                                        <Card.Text>{ product.description }</Card.Text>
                                    </Card.Body>
                                    <ListGroup className="list-group-flush">
                                        <ListGroup.Item>
                                            <div>price: { product.price }$</div>
                                            <div>stock: { product.stock }</div>
                                        </ListGroup.Item>
                                    </ListGroup>
                                    <Card.Footer className="text-muted">
                                        <Button className="add-cart btn btn-primary text-end" data-id={ product.id } data-name={ product.name }>
                                            Add to cart
                                        </Button>
                                    </Card.Footer>
                                </Card>
                            </Col>
                        )}
                    </Row>
                </div>
            </div>   
        );
    }

}