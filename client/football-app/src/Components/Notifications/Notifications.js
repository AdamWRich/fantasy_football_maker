import React, {useState, useEffect} from 'react'
import axios from 'axios';

const Notifications = () => {
    let [notifications, SetNotifications] = useState({});

    useEffect(() => { 
        axios.get(`https://nfl-schedule.p.rapidapi.com/v1/schedules`, {
            headers: {
                "X-RapidAPI-Key": "8aabf3df13mshf320515c323dc95p151b82jsncb13f13b694a",
	              "X-RapidAPI-Host": "nfl-schedule.p.rapidapi.com",
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
        <img src="#" className="rounded me-2" alt="" />
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