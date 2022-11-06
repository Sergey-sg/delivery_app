import { useEffect } from "react";
import { api } from "../interceptors/axios";
import { useNavigate } from 'react-router-dom';

export const Logout = () => {
  const navigate = useNavigate()

  useEffect(() => {
    (async () => {
      try {
        await api.post("/logout/", {refresh_token: localStorage.getItem("refresh_token")})
        
        localStorage.clear();
        api.defaults.headers.common.Authorization = null;
        navigate('/login');
      } catch (e) {
        console.log("logout not working");
      }
    })();
  }, []);

  return <div></div>;
};
