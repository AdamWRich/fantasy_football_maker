import React, {useState, useEffect} from 'react'
import axios from 'axios';

const Notifications = () => {
    let [notifications, SetNotifications] = useState({});

    useEffect(() => {
        let url = 
        axios.get(``, {
            headers: {
                "X-RapidAPI-Key": process.env.RAPID_API_KEY,
	            "X-RapidAPI-Host": process.env.RAPID_HOST,
            }
        }).then((res) => {
            console.log(res.data);
            SetNotifications(res.data);
        }).catch((err) => console.log('error in axios call', err))
    }, [])

  return (
    <div>
    <Toast>
      <Toast.Header>
        <img src="holder.js/20x20?text=%20" className="rounded me-2" alt="" />
        <strong className="me-auto">Name</strong>
        <small>venue</small>
      </Toast.Header>
      <Toast.Body className={variant === 'Info' && 'text-white'}>
        <h2>Away Team: AwayTeam.name + score</h2>
        <h1>Home Team: HomeTeam.name + score</h1>
      </Toast.Body>
    </Toast>
    </div>
  )
}

export default Notifications