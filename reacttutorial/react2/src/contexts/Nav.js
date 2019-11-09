import React, { useContext } from 'react';
import { Link } from 'react-router-dom'
import { ThemeContext } from './ThemeContext';
import { ThemeToggle } from './ThemeToggle';
import { SongList } from './SongList';
import { BookList } from './BookList';

export const Nav = () => {
  const { isLightTheme, dark, light } = useContext(ThemeContext) // magically matches dark, light and islight
  const theme = isLightTheme ? light : dark
  console.log({ dark, isLightTheme, light }) 
  return (
    <nav style={{ background: theme.ui, color: theme.color }}>
      <ul>
        <li> <Link to="/"> Home </Link> </li>
        <li> <Link to="/user"> Userz </Link> </li>
        <li> <Link to="/nonexistentlink"> dead link </Link> </li>
        <ThemeToggle />
      </ul>
      <SongList />
    </nav>
  );
  }

/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
//// THE BELOW DOES THE EXACT SAME AS THE ABOVE 
//// BUT DIFFERENTLY & CLEANER

/*
export class Nav extends React.Component {
  static contextType = ThemeContext; //Goes up the tree and finds the first ThemeContext.Provider
                                    //and uses it's value={Object and stuff} in here at ThemeContext
                                     // Alternatively, can use "ThemeContext.Consumer>{(context)=> { ....}} </themecont.>
  render() {

    const { dark, isLightTheme, light } = this.context
    const theme = isLightTheme ? light : dark
    console.log({ dark, isLightTheme, light }) // magically matches dark, light and islight

    return (
      <nav style={{ background: theme.ui, color: theme.color }}>
        <ul>
          <li> <Link to="/"> Home </Link> </li>
          <li> <Link to="/user"> Userz </Link> </li>
          <li> <Link to="/nonexistentlink"> dead link </Link> </li>
          <ThemeToggle />
        </ul>
        <SongList />
      </nav>
    );
  }
}

 
 */