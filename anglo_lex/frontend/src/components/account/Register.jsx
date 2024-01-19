import {
    Container,
     Button,
     Card,
     Row,
    Form } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

function App() {
   /*const [currentUser, setCurrentUser] = useState();*/
   const [username, setUsername] = useState('');
   const [email, setEmail] = useState('');
   const [password, setPassword] = useState('');

   /*const [dict, setDict] = useState([])*/

   /*useEffect(() => {
        axios({
            'method': 'GET',
            'url': 'http://127.0.0.1:8000/api/v1/dictionary/'
        }).then(response => {
            setDict(response.data)
        })
   },[])*/

   function submitRegistration(e) {
    e.preventDefault();
    console.log(email);
    client.post(
      "/api/v1/account/signup/",
      {
        email: email,
        username: username,
        password: password
      }
    )
    }

  return (
    <section className='vh-100 bg-image'>
    <div className='mask d-flex align-items-center h-100 gradient-custom-3'>
    <Container className='h-100'>
      <Row className='d-flex justify-content-center align-items-center h-100'>
        <div className="col-12 col-md-9 col-lg-7 col-xl-6">
          <Card className='card border-0'>
            <Card className='card-body p-5 border-0'>
            <h2 className="text-uppercase text-center mb-5">Create an account</h2>
              <Form onSubmit={e => submitRegistration(e)}>
              <Form.Group className="form-outline mb-4" controlId="formName">
                <Form.Label>Your name</Form.Label>
                <Form.Control type="text" name='username' value={username} onChange={(e) => setUsername(e.target.value)}/>
              </Form.Group>

              <Form.Group className="form-outline mb-4" controlId="formEmail">
                <Form.Label>Your Email</Form.Label>
                <Form.Control type="email" value={email} onChange={(e) => setEmail(e.target.value)}/>
              </Form.Group>

              <Form.Group className="form-outline mb-4" controlId="formPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
              </Form.Group>

              <Form.Group className="form-outline mb-4" controlId="formRepeatPassword">
                <Form.Label>Repeat your password</Form.Label>
                <Form.Control type="password"/>
              </Form.Group>

              <div className='d-flex justify-content-center'>
                <Button className='btn btn-success btn-block btn-lg gradient-custom-4 text-body border-0' type="submit">
                  Register
                </Button>
              </div>

              <p className="text-center text-muted mt-5 mb-0">Have already an account? <a href="/login"
                    className="fw-bold text-body"><u>Login here</u></a></p>

              </Form>
            </Card>
          </Card>
        </div>
      </Row>
    </Container>
    </div>
    </section>

  );
}

export default App;
