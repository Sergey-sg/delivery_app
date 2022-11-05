import { useEffect, useState } from "react";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import { Link } from "react-router-dom";
import { useAppSelector } from "../redux/hooks";

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
        <Nav.Link as={Link} to="#" className='text-black'>Change Account</Nav.Link>
      </NavDropdown.Item>
      <NavDropdown.Item as="li">
        <Nav.Link as={Link} to="#" className='text-black'>Personal Area</Nav.Link>
      </NavDropdown.Item>
      <NavDropdown.Divider />
      <NavDropdown.Item as="li">
        <Nav.Link as={Link} to="/logout/" className='text-black'>Logout</Nav.Link>
      </NavDropdown.Item>
    </NavDropdown>
  );
};

function NavbarHeader() {
  const [isAuth, setIsAuth] = useState(false);
  const user = useAppSelector((state) => state.user);

  useEffect(() => {
    if (localStorage.getItem("access_token") !== null) {
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
      <Navbar.Brand href="/">Shops</Navbar.Brand>
      <Navbar.Brand href="/cart">Shopping Cart</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="me-auto">
          <Navbar.Brand href="/cart/history-orders">History</Navbar.Brand>
        </Nav>
        <Nav className="ml-auto">
          {isAuth ? (
            <NavDropDownMenu user={user} />
          ) : (
            <Nav.Link href="/login/">Login</Nav.Link>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavbarHeader;
