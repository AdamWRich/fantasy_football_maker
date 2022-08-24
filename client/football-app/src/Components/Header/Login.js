import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

const Login = ({ setIsLoggedin }) => {
  const navigate = useNavigate();
  const [user, setUser] = useState({
    email: '',
    password: '',
  });
  const handleChange = (e) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value,
    });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://127.0.0.1:5000/user/login', user)
      .then((res) => {
        console.log(res.data);
        setIsLoggedin(true);
        navigate('/');
      })
      .catch((err) => console.log(err));
  };
  return (
    <Form onSubmit={handleSubmit}>
      <Row className="mb-3">
        <Form.Group as={Col} controlId="formGridEmail">
          <Form.Label htmlFor="email">Email:</Form.Label>
          <Form.Control type="email" name="email" value={user.email} onChange={handleChange} required placeholder="Enter Email" />
        </Form.Group>
        <Form.Group as={Col} controlId="formGridPassword">
          <Form.Label htmlFor="password">Password:</Form.Label>
          <Form.Control type="password" name="password" value={user.password} onChange={handleChange} required placeholder='Password' />
        </Form.Group>
      </Row>
      <Button variant="primary" type="submit">Login</Button>
    </Form>
  );
};

export default Login;