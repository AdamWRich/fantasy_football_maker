import { useState } from 'react';
import './App.css';
import { BrowserRouter,Routes,Route} from 'react-router-dom';
import Header from './Components/Header/Header';
import Login from './Components/Header/Login';
import Register from './Components/Header/Register';
import Main from './Components/Main/Main';

function App() {
  const [isLoggedin, setIsLoggedin] = useState(false);
  return (
    <BrowserRouter>
    <div className="App">
      <Header isLoggedin={isLoggedin} setIsLoggedin={setIsLoggedin}/>
      <Routes>
        <Route path="/" element={<Main/>} />
        <Route path="/login" element={<Login setIsLoggedin={setIsLoggedin} />} />
        <Route path="/register" element={<Register setIsLoggedin={setIsLoggedin} />} />
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
