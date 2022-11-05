import { useEffect } from "react";
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Login } from "./components/Login";
import { Logout } from "./components/Logout";
import "bootstrap/dist/css/bootstrap.min.css";
import { useAppDispatch } from "./redux/hooks";
import { fetchCurrentAuthUser } from "./redux/authService/authService";
import NavbarHeader from "./components/NavBarHeader";
import NavBarFooter from "./components/NavBarFooter";
import ProductList from "./components/ProductListPage";
import { fetchAllShops } from "./redux/shopService/shopServices";

function App() {
  const dispatch = useAppDispatch()

  useEffect(() => {
    dispatch(fetchCurrentAuthUser());
    dispatch(fetchAllShops());
  })
  
  return (
    <BrowserRouter>
      <NavbarHeader />
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
      <NavBarFooter/>
    </BrowserRouter>
  );
}

export default App;
