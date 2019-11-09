import React from 'react';

import { Nav } from './Nav'
import  About  from './About'
import { Home } from './Home'
import Imdb from './branches/imdb'
import Youtube from './branches/youtube'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import { ThemeContextProvider } from './contexts/ThemeContext'
import { ThemeToggle } from './contexts/ThemeToggle'

function App() {
  return (
    <Router>
      <ThemeContextProvider>
        <Nav />
        <ThemeToggle />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/youtube" component={Youtube} />
        <Route path="/imdb" component={Imdb} />
      </Switch>
      </ThemeContextProvider>
    </Router>

  );
}

const Home2 = () => (
  <div> HOMEPAGE </div>
);

export default App;