import './App.css';
import { BrowserRouter,Routes,Route} from 'react-router-dom';
import Header from './Components/Header/Header';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <Header />
      <Routes>
        <Route path="/" element="home" />
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
