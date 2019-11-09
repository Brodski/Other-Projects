import React, { useState, createContext } from 'react';

 export const MovieContext = createContext();

  export const MovieProvider = props => {
    const [movies, setMovies] = useState([
    {
      name: 'Rambo',
      price: '10',
      id: 1
    },
    {
      name: 'Inception',
      price: '10',
      id: 2
    },
    {
      name: 'Terminator',
      price: '10',
      id: 3
    }
    ]);

   
  // The information in MovieProvider is provided to MovieContext.Provider
  // "this.props.children" refers to to <Nav /> & everything esle that <Movie.Context.provider> is wrapped around in the App.js file
return (
  <MovieContext.Provider value={[movies, setMovies]}>
    {props.children}
  </MovieContext.Provider>
  );
};