import React from 'react';
import { Link } from 'react-router-dom'
import { ThemeContext } from './contexts/ThemeContext';
import { ThemeToggle } from './contexts/ThemeToggle'

export class Nav extends React.Component {
  static contextType = ThemeContext; //Goes up the tree and finds the first ThemeContext.Provider
                                    //and uses it's value={Object and stuff} in here at ThemeContext
                                     // Alternatively, can use "ThemeContext.Consumer>{(context)=> { ....}} </themecont.>
  render() {

    const { dark, isLightTheme, light } = this.context
    const theme = isLightTheme ? light : dark

    return (      
      <nav style={{ background: theme.ui, color: theme.color }}>
        <ul>
          <li> <Link to='/'> Home </Link> </li>
          <li> <Link to='/about'> About </Link> </li>
          <li> <Link to='/youtube'> youtube </Link> </li>
          <li> <Link to='/imdb'> imdb </Link> </li>
        </ul>
      </nav>
    );
  }
}
