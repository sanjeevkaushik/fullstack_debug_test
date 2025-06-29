import { useState, useEffect } from 'react'
import './App.css'
import config from "./config.js";


function App() {

    const [feedback, setFeedback] = useState([]);
    const [rating, setRating] = useState(null);


  useEffect(() => {
      fetch(  `${config.API_BASE_URL}/feedback?rating=${rating}`)
      .then(res => res.json())
      .then(data => setFeedback(data));
  }, [rating]);

  return (
    <div>

      <h1>Feedback Dashboard</h1>

      <select onChange={(e) => setRating(e.target.value)}>
        <option value="">All Ratings</option>
        <option value="5">5 Stars</option>
        <option value="1">1 Star</option>
      </select>
      <ul>
        {feedback.map((f, i) => (
          <li key={i}>{f[0]} - {f[1]} stars </li>
        ))}
      </ul>

    </div>
  );

}

export default App
