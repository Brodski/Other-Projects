import React from 'react';
import './App.css';
import MovieList from './MovieList';
import Nav from './Nav'
import { MovieProvider } from './MovieContext';
import AddMovie from './AddMovie';

function App() {
  return (
  <MovieProvider>
    <div className="App">
      <Nav />
        <MovieList />
        <AddMovie/>
      </div>
    </MovieProvider>
  );
}

export default App;
