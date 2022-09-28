import './App.css';
import Notes from './views/Notes';
import Create from './views/Create';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Notes />} />
        <Route path='/create' element={<Create />} />
      </Routes>
    </div>
  );
}

export default App;
