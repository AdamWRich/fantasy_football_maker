import React, {useEffect, useState} from 'react'; 
import axios from 'axios'; 
import Form from 'react-bootstrap/Form';

const NewTeam = () => {
    //constants
    const [team, setTeam] = useState('')
    //post for team
    useEffect(() => {

    }, [])
  return (
    <div>
    <Form>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Name</Form.Label>
        <Form.Control type="text" value={team} placeholder="Enter Team Name" onChange={(e) => setTeam(e.target.value)} />
        <Form.Text className="text-muted">
          validation goes here
        </Form.Text>
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
    </div>
  )
}

export default NewTeam