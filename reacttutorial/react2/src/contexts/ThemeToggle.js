import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext'


export const ThemeToggle = () => {
  const { toggleTheme } = useContext(ThemeContext)
  return (
    <button onClick={toggleTheme}> Toggle theme </button>         
  );
}



















/* Same as above.
 * 
export class ThemeToggle extends React.Component {
  static contextType = ThemeContext;
  render() {
    const { toggleTheme } = this.context
    return (
      <button onClick={toggleTheme}> Toggle theme </button>
    );
  }
}
 */