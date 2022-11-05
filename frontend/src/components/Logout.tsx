import { useEffect } from "react";
import { api } from "../interceptors/axios";

export const Logout = () => {
  useEffect(() => {
    (async () => {
      try {
        await api.post("/logout/", {refresh_token: localStorage.getItem("refresh_token")})
        
        localStorage.clear();
        api.defaults.headers.common.Authorization = null;
        window.location.href = "/login";
      } catch (e) {
        console.log("logout not working");
      }
    })();
  }, []);

  return <div></div>;
};
