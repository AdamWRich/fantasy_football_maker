import React, {useEffect, useState} from 'react';
import axios from 'axios';

const Main = () => {
    let [players, setPlayers] = useState([])

    useEffect(() => {
        axios.get('http://127.0.0.1:5000')
        .then((res) => {
            console.log(res.data)
            setPlayers(res.data)
        })
        .catch((err) => console.log('error in axios', err))
    }, [])
  return (
    <div>
        <h1></h1>
    </div>
  )
}

export default Main