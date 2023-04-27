import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useState } from 'react';

const Login = (props) => {
    

    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

      const handleSubmit = async (e) => {
        e.preventDefault();

        // Получение токена
        const getAuthToken = async (username, password) => {
            try {
            const response = await axios.post("http://127.0.0.1:8000/api/v1/token/", {
                username,
                password,
            });
            const { access } = response.data;
            axios.defaults.headers.common["Authorization"] = `Bearer ${access}`;
            // сохраняем токен в localStorage
            localStorage.setItem("token", access);
            return access;
            } catch (error) {
            console.error(error);
            throw error;
            }
        };

        // Проверяем, есть ли токен в localStorage и устанавливаем его
        const token = localStorage.getItem("token");
        if (token) {
            axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
        }

        getAuthToken(username, password)
        
        
        // Вызываем колбэк функцию, передавая ей значения `username` и `password`
        props.onLogin(username, password);

        navigate('/')
    };
    


    return (
        <>
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '10%'}}>
            <div style={{width: '700px', marginLeft: '250px'}}>
                <h4 class="mb-0"><span class="text-main-1">Sign</span> In</h4>
                <div class="nk-gap-1"></div>
                <form class="nk-form text-white" novalidate="novalidate" method="post" onSubmit={handleSubmit}>
                    <div class="row vertical-gap">
                        <div class="col-md-6">
                            Use username and password:

                            <div class="nk-gap"></div>
                            <div class="nk-gap"></div>
                            <input type="text" name="username" class=" form-control" placeholder="User Name" value={username} onChange={(e) => setUsername(e.target.value)} />

                            <div class="nk-gap"></div>
                            <input type="password" name="password" class="required form-control" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                            
                            <div class="nk-gap"></div>
                            <div class="form-error"> </div>
                           
                           

                                <p> </p>
                                <div class="form-error"> </div>
                            
                            
                        </div>
                    </div>

                    <div class="nk-gap-1"></div>
                    <div class="row vertical-gap">
                        <div class="col-md-6">
                            <button type="submit" class="nk-btn nk-btn-rounded nk-btn-color-white nk-btn-block">Sign In</button>
                            <div class="nk-gap-1"></div>
                            <div class="mnt-5">
                                <small>
                                <Link to="/register">
                                    Not a member? Sign up
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

export default Login;
