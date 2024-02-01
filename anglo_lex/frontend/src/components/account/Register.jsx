import {
    Container,
     Button,
     Card,
     Row,
    Form } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.min.css';
import {useForm} from 'react-hook-form';
import { FaEyeSlash, FaEye } from "react-icons/fa";
import { useState} from 'react';
import axios from 'axios'

const Register = () => {

  const [passwordEye, setPasswordEye] = useState(false)

  const handlePasswordClick = () => {
    setPasswordEye(!passwordEye)
  }

  const {
    register,
    watch,
    reset,
    formState: { errors, isValid },
    handleSubmit,
  } = useForm({
    mode: 'onBlur'
  })

  const password = watch('password')

  const onSubmit = (data) => {
    const username = data['username']
    const email = data['email']
    const password = data['password']

    try {
      const response = axios.post('http://127.0.0.1:8000/api/v1/account/signup/', {
           username,
           email,
           password
      });
    } catch (error) {
      console.error('Registration failed', error);
    }
    reset()
  }

    return(
    <section className='vh-100'>
    <div className='mask d-flex align-items-center h-100 gradient-custom-3'>
    <Container className='h-100'>
      <Row className='d-flex justify-content-center align-items-center h-100'>
        <div className="col-12 col-md-9 col-lg-7 col-xl-5">
          <Card className='card border-0'>
            <Card className='card-body p-5 border-0'>
            <h2 className="text-uppercase text-center mb-5">Create an account</h2>
              <Form onSubmit={handleSubmit(onSubmit)}>
              <Form.Group className="form-outline mb-4" controlId="formName">
                <Form.Label>Your username</Form.Label>
                <Form.Control type="text" name='username' {...register('username', {
                  required: 'Username is required',
                  minLength: {
                    value: 5,
                    message: 'The min field length is 5'
                  },
                  maxLength: {
                    value: 15,
                    message: 'The max field length is 15'
                  },

                })}/>
                <div style={{ color:'red' }}>{ errors?.username && <p>{ errors?.username?.message || 'Error!'}</p> }</div>
              </Form.Group>


              <Form.Group className="form-outline mb-4" controlId="formEmail">
                <Form.Label>Your Email</Form.Label>
                <Form.Control type="email" {...register('email', {
                  required: 'Email is required',
                  pattern: {
                    value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
                    message: 'Invalid email address'
                  }
                })} />
                <div style={{ color:'red' }}>{ errors?.email && <p>{ errors?.email?.message || 'Error!'}</p> }</div>
              </Form.Group>

              <Form.Group className="form-outline mb-4" controlId="formPassword">
                <Form.Label>Password</Form.Label>
                <div className='d-flex justify-content-end'>
                  <Form.Control className='form-control' type={(passwordEye === false)? 'password': 'text'} {...register('password', {
                    required: 'Password is required',
                    pattern: {
                      value: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/,
                      message: 'Password must at least one upper case letter, one lower case letter,one number, and one special character and length is at least 8 characters'
                    }
                  })}/>

                  <span className='position-absolute pt-1 pe-3'>
                    {
                      (passwordEye === false)?<FaEyeSlash onClick={handlePasswordClick}/>:
                      <FaEye onClick={handlePasswordClick}/>
                    }
                  </span>
                </div>
                <div style={{ color:'red' }}>{ errors?.password && <p>{ errors?.password?.message || 'Error!'}</p> }</div>
              </Form.Group>


              <Form.Group className="form-outline mb-4" controlId="formConfirmPassword">
                <Form.Label>Confirm your password</Form.Label>
                <div className='d-flex justify-content-end'>
                  <Form.Control type={(passwordEye === false)? 'password': 'text'} {...register('confirm_password', {
                    required: 'Confirm password is required',
                    validate: (value) => value === password || 'The passwords do not match'

                  })}/>
                  <span className='position-absolute pt-1 pe-3'>
                      {
                        (passwordEye === false)?<FaEyeSlash onClick={handlePasswordClick}/>:
                        <FaEye onClick={handlePasswordClick}/>
                      }
                    </span>
                  </div>
                <div style={{ color:'red' }}>{ errors?.confirm_password && <p>{ errors?.confirm_password?.message || 'Error!'}</p> }</div>
              </Form.Group>

              <div className='d-flex justify-content-center'>
                <Button className='btn btn-success btn-block btn-lg gradient-custom-4 text-body border-0' type="submit" disabled={!isValid}>
                  Sign Up
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

export default Register;