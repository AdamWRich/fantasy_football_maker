import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

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
      .post('http://localhost:8000/login', user, { withCredentials: true })
      .then((res) => {
        console.log(res.data);
        setIsLoggedin(true);
        navigate('/');
      })
      .catch((err) => console.log(err));
  };
  return (
    <Form onSubmit={handleSubmit}>
      <Form.Label htmlFor="email">Email:</Form.Label>
      <Form.Control type="email" name="email" value={user.email} onChange={handleChange} required placeholder="Enter Email" />
      <Form.Label htmlFor="password">Password:</Form.Label>
      <Form.Control type="password" name="password" value={user.password} onChange={handleChange} required placeholder='Password' />
      <Button variant="primary" type="submit">Login</Button>
    </Form>
  );
};

export default Login;