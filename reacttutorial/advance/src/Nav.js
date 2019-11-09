import React, { useContext } from 'react';
import { MovieContext } from './MovieContext';


const Nav = () => {
  const [movies, setMovies] = useContext(MovieContext);
  return (
    <nav>
      <div> Dev ed </div>
      <div> Movies length {movies.length} </div>
    </nav>
  );
}

export default Nav