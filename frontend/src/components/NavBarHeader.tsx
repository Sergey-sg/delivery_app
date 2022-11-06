import { useEffect, useState } from "react";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import { Link } from "react-router-dom";
import { useAppDispatch, useAppSelector } from "../redux/hooks";
import profile from "../assets/icons/profile.svg";
import { fetchCurrentAuthUser } from "../redux/authService/authService";

const NavDropDownMenu = (props: {
  user: { first_name: string; email: string };
}) => {
  return (
    <NavDropdown
      title={props.user.first_name || props.user.email}
      id="collasible-nav-dropdown"
      align="end"
    >
      <NavDropdown.Item as="li">
        <Nav.Link as={Link} to="#" className="text-black">
          Change Account
        </Nav.Link>
      </NavDropdown.Item>
      <NavDropdown.Item as="li">
        <Nav.Link as={Link} to="#" className="text-black">
          Personal Area
        </Nav.Link>
      </NavDropdown.Item>
      <NavDropdown.Divider />
      <NavDropdown.Item as="li">
        <Nav.Link as={Link} to="/logout/" className="text-black">
          Logout
        </Nav.Link>
      </NavDropdown.Item>
    </NavDropdown>
  );
};

function NavbarHeader() {
  const [isAuth, setIsAuth] = useState(false);
  const user = useAppSelector((state) => state.user);
  const dispatch = useAppDispatch()
  
  useEffect(() => {
    dispatch(fetchCurrentAuthUser());
  }, [])

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      setIsAuth(true);
    }
  }, [isAuth]);

  return (
    <Navbar
      collapseOnSelect
      expand="lg"
      bg="dark"
      variant="dark"
      className="px-4 mb-4"
    >
      <Navbar.Brand>
        <Nav.Link as={Link} to="/">
          Shop
        </Nav.Link>
      </Navbar.Brand>
      <Navbar.Brand>
        <Nav.Link as={Link} to="/cart">
          Shopping Cart
        </Nav.Link>
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="me-auto">
          <Navbar.Brand>
            <Nav.Link as={Link} to="/cart/history-orders">
              History
            </Nav.Link>
          </Navbar.Brand>
        </Nav>
        <Nav className="ml-auto">
          {isAuth ? (
            <div className="flex-row d-flex">
              <img
                src={user.photo || profile}
                alt={user.img_alt}
                width="32"
                height="32"
                className="rounded-circle me-2 my-auto"
              />
              <NavDropDownMenu user={user} />
            </div>
          ) : (
            <Nav.Link href="/login/">Login</Nav.Link>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavbarHeader;
