import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext'
import { BookContext } from './BookContext'

export const BookList = () => {

  const { books } = useContext(BookContext);
  const { isLightTheme, dark, light } = useContext(ThemeContext) // magically matches dark, light and islight
  const theme = isLightTheme ? light : dark

  console.log({ dark, isLightTheme, light })
  return (
    <nav style={{ background: theme.ui, color: theme.color }}>
      <ul>
        {books.map(book => {
          return (
            <li> {book.title} </li>
          )
        } ) }
      </ul>
    </nav>
  );
}