import { useEffect } from "react";
import { fetchLogin } from "../redux/authService/authService";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import { useNavigate } from "react-router-dom";
import { useFormik } from "formik";
import { LoginSchema } from "../schemas/login.schema";

export const Login = () => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const success = useAppSelector((state) => state.success.message);
  const error = useAppSelector((state) => state.error.message);

  useEffect(() => {
    if (success === "login success") {
      navigate("/");
    }
  }, [success]);

  const formik = useFormik({
    initialValues: { email: "", password: "" },
    onSubmit: (values) => dispatch(fetchLogin(values)),
    validationSchema: LoginSchema,
  });

  return (
    <div className="Auth-form-container m-5">
      <form className="Auth-form" onSubmit={formik.handleSubmit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign in</h3>
          {error === "No active account found with the given credentials" && (
            <div className="textError">
              - wrong email or password, please check your login params and try
              again
            </div>
          )}
          <div className="form-group mt-3">
            <label>Email</label>
            <input
              className="form-control mt-1"
              placeholder="enter your email"
              name="email"
              type={"email"}
              value={formik.values.email}
              required
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.touched.email && formik.errors.email && (
              <p className="textError mt-2">{formik.errors.email}</p>
            )}
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              className="form-control mt-1"
              placeholder="enter your password"
              name="password"
              type={"password"}
              value={formik.values.password}
              required
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.touched.password && formik.errors.password && (
              <p className="textError mt-2">{formik.errors.password}</p>
            )}
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
