import React from "react";
import "./App.css";
import { Route, Routes } from "react-router-dom";
import { Login } from "./components/Login";
import { Logout } from "./components/Logout";
import "bootstrap/dist/css/bootstrap.min.css";
import NavbarHeader from "./components/NavBarHeader";
import NavBarFooter from "./components/NavBarFooter";
import ProductList from "./components/ProductListPage";

function App() {
  return (
    <>
      <NavbarHeader />
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
      <NavBarFooter />
    </>
  );
}

export default App;
