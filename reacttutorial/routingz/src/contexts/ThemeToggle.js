import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext'


export const ThemeToggle = () => {
    const { toggleTheme } = useContext(ThemeContext)
    return (
      <button onClick={toggleTheme}> Toggle theme </button>
    );
}
