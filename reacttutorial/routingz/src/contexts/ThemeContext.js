import React, { createContext, Component } from 'react';

export const ThemeContext = createContext();

export class ThemeContextProvider extends Component {
  state = {
    isLightTheme: true,
    light: { color: '#555', ui: '#ddd', bg: '#eee' },
    dark: { color: '#ddd', ui: '#333', bg: '#555' }
  }

  toggleTheme = () => {
    this.setState({ isLightTheme: !this.state.isLightTheme });
  }
  // "this.props.children" refers to to <Nav /> & everything esle that <themeContext.provider> is wrapped around
  // in the App.js file
  render() {
    return (
      <ThemeContext.Provider value={{...this.state, toggleTheme: this.toggleTheme }} >
        {this.props.children} 
      </ThemeContext.Provider>

    );
  }
}

