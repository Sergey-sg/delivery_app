import React, { useEffect } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import { Link, useLocation } from "react-router-dom";
import {
  fetchAllProducts,
  fetchAllProductsForShop,
} from "../redux/productService/productServices";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { fetchAllShops } from "../redux/shopService/shopServices";

const ProductList = () => {
  const dispatch = useAppDispatch();
  const queryParamsFromUrl = new URLSearchParams(useLocation().search);
  const shopPk = queryParamsFromUrl.get("shopPk") || "";
  const products = useAppSelector((state) => state.products);
  const shops = useAppSelector((state) => state.shops);

  useEffect(() => {
    if (shopPk) {
      dispatch(fetchAllProductsForShop(shopPk));
    } else {
      dispatch(fetchAllProducts());
    }
  }, []);

  useEffect(() => {
    dispatch(fetchAllShops());
  }, []);

  const productAddToCart = (pk: number) => {
    console.log("add product to cart");
  };

  return (
    <Row>
      <Col 
        className="container col-3 border rounded"
      >
        <div className="text-center">
          Shops:
          <br />
          {shops?.map((shop) => (
            <p key={shop.pk}>
              <Link
                className="container border rounded btn btn-link"
                to={"/shop/" + shop.pk}
              >
                <img
                  className="shop-logo"
                  src={shop.image}
                  alt={shop.img_alt}
                />
                <br />
                {shop.name}
              </Link>
            </p>
          ))}
        </div>
      </Col>
      <div id="product-items" className="container col-8 border rounded">
        <br />
        <Row className="justify-content-evenly">
          {products?.map((product) => (
            <Col xs={10} md={5} lg={5} key={product.pk}>
              <Card>
                <Link to={`product/${product.slug}`}>
                  <Card.Img
                    variant="top"
                    src={product.image}
                    alt={product.img_alt}
                  />
                </Link>
                <Card.Body>
                  <Card.Title>
                    <h5>
                      <Link to={`product/${product.slug}`}>{product.name}</Link>
                    </h5>
                  </Card.Title>
                  <Card.Text>{product.description}</Card.Text>
                </Card.Body>
                <ListGroup className="list-group-flush">
                  <ListGroup.Item>
                    <div>price: {product.price}$</div>
                    <div>stock: {product.stock}</div>
                  </ListGroup.Item>
                </ListGroup>
                <Card.Footer className="text-muted">
                  <Button
                    className="add-cart btn btn-primary text-end"
                    onClick={() => productAddToCart(product.pk)}
                  >
                    Add to cart
                  </Button>
                </Card.Footer>
              </Card>
            </Col>
          ))}
        </Row>
      </div>
    </Row>
  );
};

export default ProductList;
