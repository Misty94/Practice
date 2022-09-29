import './App.css';
import Notes from './views/Notes';
import Create from './views/Create';
import { Routes, Route } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@material-ui/core';
import { purple } from '@material-ui/core/colors';

const theme = createTheme({
  palette: {
    primary: {
      main: '#fefefe'
    },
    secondary: purple
  },
  typography: {
    fontFamily: 'Quicksand',
    fontWeightLight: 400,
    fontWeightRegular: 500,
    fontWeightMedium: 600,
    fontWeightBold: 700
  }
})

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Routes>
          <Route path='/' element={<Notes />} />
          <Route path='/create' element={<Create />} />
        </Routes>
      </ThemeProvider>
    </div>
  );
}

export default App;
