import {
    Container,
     Button,
     Card,
     Row,
    Form } from 'react-bootstrap';

import {useForm} from 'react-hook-form';
import { createBrowserHistory } from "history";
import axios from 'axios'


const Login = () => {

    const {
        register,
        reset,
        handleSubmit,
        formState: {errors, isValid},

    } = useForm({
        mode: 'onBlur'
    })

    const history = createBrowserHistory();

    const onSubmit = (data) => {
    const email = data['email']
    const password = data['password']

     try {
        const response = axios.post('http://127.0.0.1:8000/api/v1/account/signin/', {
        email,
        password
      }).then(function (response){
        console.log(response.data)
        window.location = '/home'
      });

    } catch (error) {
    if (error.response && error.response.status === 401) {
        window.location = '/login'
        console.log('Ошибка 401: Пользователь не авторизован');

    }

    }

    reset()
   }


    return (
    <section className="login__section vh-100">
        <div className='mask d-flex align-items-center h-100 gradient-custom-3'>
            <Container className='h-100'>
                <Row className='d-flex justify-content-center align-items-center h-100'>
                    <div className="col-12 col-md-9 col-lg-7 col-xl-6">
                        <Card className='card border-0'>
                            <Card className='card-body p-5 border-0'>
                            <h2 className="text-uppercase text-center mb-5">Login</h2>
                                <Form onSubmit={handleSubmit(onSubmit)}>

                                <Form.Group className="form-outline mb-4" controlId="formEmail">
                                    <Form.Label>Email address</Form.Label>
                                    <Form.Control type="email" name="email" {... register('email', {
                                        required: 'Email is required',
                                        pattern: {
                                            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
                                            message: 'Invalid email address'
                                        }
                                    })}/>

                                <div style={{ color:'red' }}>{ errors?.email && <p>{ errors?.email?.message || 'Error!'}</p> }</div>
                                </Form.Group>

                                <Form.Group className="form-outline mb-4" controlId="formPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control type="password" name="password" {... register('password', {
                                        required: 'Password is required',
                                    })}/>

                                <div style={{ color:'red' }}>{ errors?.password && <p>{ errors?.password?.message || 'Error!'}</p> }</div>
                                </Form.Group>

                                <div className='d-flex justify-content-center mt-4'>
                                    <Button className='btn btn-success btn-block btn-lg gradient-custom-4 text-body border-0'
                                    type="submit" disabled={!isValid}>
                                    Sign In
                                    </Button>
                                </div>

                                </Form>
                            </Card>
                        </Card>
                    </div>
                </Row>
            </Container>
        </div>
    </section>
    )
}

export default Login