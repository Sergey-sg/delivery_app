import * as Yup from "yup";

export const LoginSchema = Yup.object({
  email: Yup.string()
    .required("- email required field")
    .email()
    .max(320, "- email must be less than 320 characters."),

  password: Yup.string().required("- password required field"),
});
