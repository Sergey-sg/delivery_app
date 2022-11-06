import { useEffect, useState } from "react";
import { ILoginParams } from "../interfaces/login.interface";
import { fetchLogin } from "../redux/authService/authService";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { useNavigate } from 'react-router-dom';

export const Login = () => {
  const dispatch = useAppDispatch()
  const navigate = useNavigate()
  const success = useAppSelector((state) => state.success.message)
  const [userEmail, setUserEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    if (success === "login success") {
      navigate('/');
    }
  }, [success])

  const submit = (e: { preventDefault: () => void; }) => {
    e.preventDefault();

    const authParams: ILoginParams = {
      email: userEmail,
      password: password,
    };

    dispatch(fetchLogin(authParams))
  }

  return (
    <div className="Auth-form-container m-5">
      <form className="Auth-form" onSubmit={submit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign in</h3>
          <div className="form-group mt-3">
            <label>Email</label>
            <input
              className="form-control mt-1"
              placeholder="enter your email"
              name="email"
              type="email"
              value={userEmail}
              required
              onChange={(e) => setUserEmail(e.target.value)}
            />
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              className="form-control mt-1"
              placeholder="enter your password"
              name="password"
              type="password"
              value={password}
              required
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};
