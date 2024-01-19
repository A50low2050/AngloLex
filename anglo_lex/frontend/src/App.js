
import './App.css';
import { Route, Routes } from "react-router-dom";
import { BrowserRouter } from "react-router-dom";
import Register from './components/account/Register';
import Login from './components/account/Login';
import Home from './components/home/Home';


function App() {
  return (
    <div className='test__app'>
      <BrowserRouter>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
      </BrowserRouter>
    </div>

  );
}

export default App;
