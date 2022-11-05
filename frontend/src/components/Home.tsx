import { useEffect, useState } from "react";
import { api } from "../interceptors/axios";
import { useAppSelector } from "../redux/hooks";

const fetchHome = async () => {
  const response = await api.get("/home/")
    .catch((e) => console.log("not auth"));

  return response?.data.message
}

export const Home = () => {
  const [message, setMessage] = useState("");
  const user = useAppSelector((state) => state.user)

  useEffect(() => {
    if (localStorage.getItem("access_token") === null) {
      window.location.href = "/login";
    } else {
      fetchHome().then(message => setMessage(message))
    }
  }, []);

  return (
    <div className="form-signin m-5 text-center">
      <h3>Hi {message}</h3>
      <p>{user.email}</p>
    </div>
  );
};
