import React, { useEffect } from "react";
import "./App.css";
import { Route, Routes, useNavigate } from "react-router-dom";
import { Login } from "./components/Login";
import { Logout } from "./components/Logout";
import "bootstrap/dist/css/bootstrap.min.css";
import NavbarHeader from "./components/NavBarHeader";
import NavBarFooter from "./components/NavBarFooter";
import ProductList from "./components/ProductListPage";
import { useAppSelector } from "./redux/hooks";

function App() {
  const navigate = useNavigate();
  const isAuth = useAppSelector((state) => state.user.isAuth);

  useEffect(() => {
    console.log("start App");
    if (!localStorage.getItem("access_token")) {
      navigate("/login/");
    }
  }, [isAuth]);

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
