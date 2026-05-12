import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState('');
  const [names, setNames] = useState([]);

  const fetchNames = async () => {
    const response = await axios.get('http://127.0.0.1:5000/names');
    setNames(response.data);
  };

  useEffect(() => {
    fetchNames();
  }, []);

  const saveName = async () => {
    await axios.post('http://127.0.0.1:5000/save', {
      name: name,
    });

    setName('');
    fetchNames();
  };

  return (
    <div style={{ padding: '30px' }}>
      <h1>DevOps Learning App - Feature Branch</h1>

      <input
        type="text"
        placeholder="Enter name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <button onClick={saveName}>Save</button>

      <h2>Saved Names</h2>

      <ul>
        {names.map((n, index) => (
          <li key={index}>{n}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
