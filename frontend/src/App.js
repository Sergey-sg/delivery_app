import './App.css';
import React, { Component } from 'react';
import { BrowserRouter } from  'react-router-dom'
import {Routes, Route} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import ProductList from './ProductsList';
import ProductDetail from './ProductDetail'
import NavbarHeader from './NavbarHeader';
import NavbarFooter from './NavbarFooter';


const BaseLayout = () => (
  <div>
    <NavbarHeader />
    <div className="content">
      <Routes>
        <Route path="/" extact element={<ProductList/>} />
        <Route path="/shop/:pk" extact element={<ProductList/>} />
        <Route path="/product/:slug" element={<ProductDetail/>} />
      </Routes>
    </div>
    <NavbarFooter />
  </div>
)


class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;
