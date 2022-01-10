import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Home from './components/Home';
import "react-router";
import Edit from './components/Edit';

function App() {
  return (
    <div className="App">
      <Header />
      <Home />  
      {/* <Edit /> */}
    </div>
  );
}

export default App;