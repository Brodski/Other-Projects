import React, { useState, useEffect } from 'react';
import uuid from 'uuid/v1';
import { NewSongForm } from './NewSongForm'

export const SongList = () => {
  const [songs, set] = useState([ // usestate returns 2 values, 
                                  // 1st is the array, 2nd is a function (arbitrary name) to change the data
    { title: 'Brand new Rollers', id: 1 },
    { title: 'Revive', id: 2 },
    { title: 'Funk Mix', id: 3 },
    { title: 'All I Want', id: 4 }
  ]);

  useEffect(() => { // 2 paramaters, 1st = code that runs when *it* renders/re-renders. 2nd = array of variables, if 1 variable is updated then it triggers 1st param's code
    console.log('useEffect hook ran', songs)
  }, [songs]) 

  const addSong = (title) => {               //Everything inside of "set"'s paratheses will replace "songs"
    set([...songs, { title, id: uuid() }])   // "title" is ES6 shorthand for "title: title" (since same name)
  }

  return (
  <div>
    <ul>
      {songs.map(song => {
        return (<li key={song.id}> {song.title} </li> )
        } ) }
    </ul>
    <NewSongForm addSong={addSong}/>
  </div>

  );
}