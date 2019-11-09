import React, { useState } from 'react';

export const NewSongForm = ({ addSong }) => { //addsong comes as a prop from SongList
  const [title, setTitle] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault(); //prevent the refresh that happens on submit
    addSong(title);
    setTitle('') //Clears out textbox after submit
   }

  return (
    <form onSubmit={handleSubmit}>
      <label>Song Name:</label>
      <input type="text" required value={title} onChange={(e) => setTitle(e.target.value) } /> 
      <input type="submit" value="add song" />
    </form>
  )
}