import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register = () => {

    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [repassword, setRepassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        if (password === repassword){
        // Создаем объект FormData для отправки данных на сервер
        const formData = new FormData();
        formData.append("email", email);
        formData.append("username", username);
        formData.append("password", password);
    
        try {
          // Отправляем данные на сервер с помощью axios
          const response = await axios.post("http://127.0.0.1:8000/api/v1/auth/users/", formData);
          console.log(response.data);
          navigate('/login');
        } catch (error) {
          console.error(error);
        }
        }else{
            console.log("Пароли не совпадают")
        }
    };
    

    return (
        <>
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '10%'}}>
            <div style={{width: '700px', marginLeft: '250px'}}>
                <h4 class="mb-0"><span class="text-main-1">Sign</span> Up</h4>

                <div class="nk-gap-1"></div>
                
                <form class="nk-form text-white" novalidate="novalidate" onSubmit={handleSubmit}>
                    <div class="row vertical-gap">
                        <div class="col-md-6">
                            Insert data:

                            *While write an pass, make sure it has at least 8 characters, also use both number, and letters*
                        <div class="nk-gap"></div>
                            <div class="nk-gap"></div>
                            <input type="email" name="email" class=" form-control" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                            <div class="nk-gap"></div>
                            <input type="text" name="username" class="required form-control" placeholder="UserName" value={username} onChange={(e) => setUsername(e.target.value)}/>
                            <div class="nk-gap"></div>
                            <input type="password" name="password" class="required form-control" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                            <div class="nk-gap"></div>
                            <input type="password" name="repassword" class="required form-control" placeholder="Repeat Password" value={repassword} onChange={(e) => setRepassword(e.target.value)}/>
                            <p> </p>
                            <div class="form-error"> </div>
                        </div>

                    </div>

                    <div class="nk-gap-1"></div>
                    <div class="row vertical-gap">
                        <div class="col-md-6">
                            <button type="submit" class="nk-btn nk-btn-rounded nk-btn-color-white nk-btn-block" >Sign Up</button>
                            <div class="nk-gap-1"></div>
                            <div class="mnt-5">
                                <small>
                                <Link to="/login">
                                    Already have an account? Sign in
                                </Link>
                                </small>
                            </div>
                        </div>
                    </div>
                </form>


            </div>
        </div>
        </>
    );
}

export default Register;
