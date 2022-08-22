import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

const Register = ({ setIsLoggedin }) => {
  const navigate = useNavigate();
  const [user, setUser] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
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
      .post('http://localhost:8000/register', user, { withCredentials: true })
      .then((res) => {
        console.log(res.data);
        setIsLoggedin(true);
        navigate('/');
      })
      .catch((err) => console.log(err));
  };
  return (
    <Form onSubmit={handleSubmit}>
      <Row className="align-items-center">
        <Form.Group as={Col} controlID="formGridUsername">
          <Form.Label htmlFor="username">Username:</Form.Label>
          <Form.Control type="text" name="username" value={user.username} onChange={handleChange} required />
        </Form.Group>
        <Form.Group as={Col} controlID="formGridEmail">
          <Form.Label htmlFor="email">Email:</Form.Label>
          <Form.Control type="email" name="email" value={user.email} onChange={handleChange} required />
        </Form.Group>
      </Row>
      <Row className="mb-3">
        <Form.Group as={Col} controlID="formGridPassword">
          <Form.Label htmlFor="password">Password:</Form.Label>
          <Form.Control type="text" name="password" value={user.password} onChange={handleChange} required />
        </Form.Group>
        <Form.Group as={Col} controlID="formGridConfirmPassword">
          <Form.Label htmlFor="confirmPassword">Confirm Password:</Form.Label>
          <Form.Control type="text" name="confirmPassword" value={user.confirmPassword} onChange={handleChange} required />
        </Form.Group>
      </Row>
      <Button variant="primary">Register</Button>
    </Form>
  );
};

export default Register;