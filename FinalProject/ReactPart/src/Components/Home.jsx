import '../game/css/goodgames.css'
import '../game/css/vendor/photoswipe/dist/photoswipe.css'
import '../game/css/vendor/photoswipe/dist/default-skin/default-skin.css'
// import { ThemeContext } from "../Context";
import axios from 'axios';
import React, { useState, useEffect } from 'react';


import Footer from '../Components/Footer';
import BreadCrumbs from '../Components/BreadCrumbs';
import Category from '../Components/Category';

// import logo from './game//images/logo.png'
import Posts from '../Components/Posts';
import Pagination from '../Components/Pagination';
import SearchPanel from '../Components/SearchPanel';


function Home() {

    const [searchValue, setSearchValue] = useState("");

    const [posts, setPosts] = useState([]);
    const [category, setCategory] = useState([]);
    const [comments, setComments] = useState([]);

    const [activeCat, SetActiveCat] = useState(null);
    const [currentPage, setCurrentPage] = useState(1);
    const [postsPerPage] = useState(3)
    const [isLoading, setIsLoading] = useState(true);



    

    const lastPostIndex = currentPage * postsPerPage
    const firstPostIndex = lastPostIndex - postsPerPage
    const paginate = (pageNumber) => setCurrentPage(pageNumber);

    const sortedItems = posts
      .filter((post) =>
      post.title.toLowerCase().includes(searchValue.toLowerCase())
      )
      .filter(
      (post) => activeCat === null || post.category_id === activeCat
      )
      .slice(firstPostIndex, lastPostIndex)
      
      const handleCategoryClick = (category) => {
        SetActiveCat(category);
      };

    const countComments = (postID) => {
      let count = 0;
      comments.forEach((comment) => {
        if (comment.news === postID) {
          count++;
        }
      });
      return count;
    };


    async function getAllPosts() {
      let allPosts = [];
    
      let nextUrl = 'http://127.0.0.1:8000/api/v1/news/';
    
      while (nextUrl !== null) {
        const response = await axios.get(nextUrl);
        allPosts = allPosts.concat(response.data.results);
        nextUrl = response.data.next;
      }
      setPosts(allPosts)
      console.log()
    
      return allPosts;
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
        setIsLoading(false);
      }).catch((err)=>{
        console.log(err);
      })    
    };
  
    const fetchComments = () => {
      setIsLoading(true);
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
  

    function formatDate(isoDate) {
      const date = new Date(isoDate);
      const day = date.getDate();
      const month = date.toLocaleString('default', { month: 'long' });
      const year = date.getFullYear();
      return `${day} ${month} ${year}`;
    }
  
    function truncateWords(text, limit) {
      const words = text.split(' ');
      return words.slice(0, limit).join(' ');
    }
  

    return (
        <>
    {isLoading ? (
        <p>Loading...</p>
      ) : (
      <div class="nk-main">

    <BreadCrumbs />




<div class="container">
    <div class="row vertical-gap">
        <div class="col-lg-8">

            <div class="nk-tabs">

                <Category
                category={category}
                handleCategoryClick={handleCategoryClick}
                activeCat={activeCat}
                />
                <div class="nk-gap"></div>


                <div class="tab-content">
                    <div role="tabpanel" class="tab-pane fade show active" id="tabs-1-1">
                        
                        <div class="nk-gap"></div>
            <Posts 
            data={posts}
            formatDate={formatDate}
            truncateWords={truncateWords}
            sortedItems={sortedItems}
            category={category}
            countComments={countComments}
            />

            <Pagination 
            postsPerPage={postsPerPage}
            totalPosts={posts.length}
            currentPage={currentPage}
            paginate={paginate}
            />
                        
                        <div class="nk-gap"></div>
                    
                    </div>
                </div>
            </div>
        </div>
        
        <SearchPanel 
        setSearchValue={setSearchValue}
        formatDate={formatDate}
        />

    </div>
</div>

<div class="nk-gap-2"></div>
            <Footer />
    </div>
    )}
        </>
    );
}

export default Home;
