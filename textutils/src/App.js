import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import './App.css';
import Navbar from './components/Navbar';
import Textform from './components/Textform';
import Alert from './components/Alert';
function App() {
  const [mode, setMode] = useState('light');
  const [alert, setAlert] = useState(null);
  const showAlert =(message)=> {
     setAlert({
      msg: message
     })
      
  }
  const toggleMode =()=> {
    if(mode === 'light'){
      setMode('dark');
      document.body.style.backgroundColor='#050A30';
      showAlert("Dark mode has been enabled")
    }
    else{
      setMode('light');
      document.body.style.backgroundColor='white';
      showAlert("Light mode has been enabled")
    }
  }
  

  return (
    <>
    <Navbar title="Textutils" mode={mode} toggleMode={toggleMode} />
    <div className="container" my-3>
    <Alert alert={alert}/>
    </div>
    <div className="container my-3" >
    <Textform heading="Enter text here:" mode={mode} />
    </div>
    </>
      );
}

export default App;
