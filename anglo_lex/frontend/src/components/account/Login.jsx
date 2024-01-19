import {
    Container,
     Button,
     Card,
     Row,
    Form } from 'react-bootstrap';

const Login = () => {
    return (
    <section className="login__section vh-100">
        <div className='mask d-flex align-items-center h-100 gradient-custom-3'>
            <Container className='h-100'>
                <Row className='d-flex justify-content-center align-items-center h-100'>
                    <div className="col-12 col-md-9 col-lg-7 col-xl-6">
                        <Card className='card border-0'>
                            <Card className='card-body p-5 border-0'>
                            <h2 className="text-uppercase text-center mb-5">Login</h2>
                                <Form>

                                <Form.Group className="form-outline mb-4" controlId="formEmail">
                                    <Form.Label>Email address</Form.Label>
                                    <Form.Control type="email"/>
                                </Form.Group>

                                <Form.Group className="form-outline mb-4" controlId="formPassword">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control type="password"/>
                                </Form.Group>

                                <div className='d-flex justify-content-center mt-4'>
                                    <Button className='btn btn-success btn-block btn-lg gradient-custom-4 text-body border-0' type="submit">
                                    Sign In
                                    </Button>
                                </div>

                                <div class="text-center mt-4">
                                    <p className="text-center text-muted mt-5 mb-0">Not a member? <a href="/register" className="fw-bold text-body"><u>Register here</u></a></p>
                                    <p>or sign up with:</p>
                                    <button type="button" class="btn btn-link btn-floating mx-1">
                                    <i class="fab fa-facebook-f"></i>
                                    </button>

                                    <button type="button" class="btn btn-link btn-floating mx-1">
                                    <i class="fab fa-google"></i>
                                    </button>

                                    <button type="button" class="btn btn-link btn-floating mx-1">
                                    <i class="fab fa-twitter"></i>
                                    </button>

                                    <button type="button" class="btn btn-link btn-floating mx-1">
                                    <i class="fab fa-github"></i>
                                    </button>
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