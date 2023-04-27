import './game/css/vendor/photoswipe/dist/photoswipe.css'
import './game/css/vendor/photoswipe/dist/default-skin/default-skin.css'
import './game/css/vendor/bootstrap/dist/css/bootstrap.min.css'
import './game/css/vendor/ionicons/css/ionicons.min.css'
import './game/css/goodgames.css'

import { DefaultContext } from "./Context";
import { LoginContext } from "./Context";
import { Route, Routes } from "react-router-dom";
import axios from 'axios';
import { useEffect, useState } from 'react';


import NotFoundPage from './Components/NotFoundPage';
import Home from './Components/Home';
import About from './Components/About';
import Header from './Components/Header';
import Post from './Components/Post';
import AddPost from './Components/AddPost';
import Register from './Components/Register'
import Login from './Components/Login'

function App(username, password) {
  const [post, setPost] = useState([]);
  const [category, setCategory] = useState([]);
  const [comments, setComments] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  async function getAllPosts() {
    let allPosts = [];
  
    let nextUrl = 'http://127.0.0.1:8000/api/v1/news/';
  
    while (nextUrl !== null) {
      const response = await axios.get(nextUrl);
      allPosts = allPosts.concat(response.data.results);
      nextUrl = response.data.next;
    }
    setPost(allPosts)
    console.log()
  
    return allPosts;
  }

  function handleLogin(username, password) {
    // Обработка авторизации
    console.log('username:', username);
    console.log('password:', password);
  }

  useEffect(() =>{

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
    


  const fetchPost = () => {
    getAllPosts();
    setIsLoading(false);
  };

    const fetchCategory = () => {
      setIsLoading(true);
      axios
      .get('http://127.0.0.1:8000/api/v1/category/')
      .then(res => {
        setCategory(res.data.results);
      }).catch((err)=>{
        console.log(err);
      })    
    };

    const fetchComments = () => {
      axios
      .get('http://127.0.0.1:8000/api/v1/comment/')
      .then(res => {
        setComments(res.data.results);
      }).catch((err)=>{
        console.log(err);
      })    
    };


      getAuthToken("user", "1234").then(() => {
        fetchComments();
  
        fetchCategory();
        fetchPost();
      });
    }, []);

  
  return (
    <>
    {isLoading ? (
        <p>Loading...</p>
      ) : (
    <LoginContext.Provider>

    <Header />

    <DefaultContext.Provider>
            <Routes>
                <Route path="/" element={<Home />}/>
                <Route path="/about" element={<About />}/>
                <Route path="/addpost" element={<AddPost />}/>
                <Route path="/login" element={<Login onLogin={handleLogin} />}/>
                <Route path="/register" element={<Register />}/>
                <Route path="/post/:id" element={<Post props={post} category={category} comments={comments} />} />
                <Route path="*" element={<NotFoundPage />} />
            </Routes>

    </DefaultContext.Provider>

    </LoginContext.Provider>
    )}
    </>
  );
}

export default App;
