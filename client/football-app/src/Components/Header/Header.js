import React from 'react'
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import {Link} from 'react-router-dom'

const Header = () => {
  return (
    <div>
    <Navbar>
      <Container>
        <Navbar.Brand href="#home">Logo Here</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
            <Link to="/">Home</Link>
            <Link to="#">Teams</Link>
            <Link to="#">Players</Link>
          <Navbar.Text>
            Signed in as: <a href="#login">Mark Otto</a>
          </Navbar.Text>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    </div>
  )
}

export default Header