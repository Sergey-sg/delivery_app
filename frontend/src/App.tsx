import { useEffect } from "react";
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Navigation } from "./components/Navigation";
import { Home } from "./components/Home";
import { Login } from "./components/Login";
import { Logout } from "./components/Logout";
import "bootstrap/dist/css/bootstrap.min.css";
import { useAppDispatch } from "./redux/hooks";
import { fetchCurrentAuthUser } from "./redux/authService/authService";

function App() {
  const dispatch = useAppDispatch()

  useEffect(() => {
    dispatch(fetchCurrentAuthUser())
  }, [])
  
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
