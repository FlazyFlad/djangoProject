// import { AppBar, Toolbar, Typography, MenuItem } from "@mui/material";
import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

function SearchPanel({setSearchValue, formatDate}) {

    const [popularNews, setPopularNews] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() =>{
    
        const fetchPNews = () => {
          axios
          .get('http://127.0.0.1:8000/api/v1/news/recomends/')
          .then(res => {
            setPopularNews(res.data);
            setIsLoading(false);
          }).catch((err)=>{
            console.log(err);
          })    
        };
    
        fetchPNews();

        }, []);

    return (
        <>

        {isLoading ? (
            <p>Loading...</p>
        ) : (
        <div class="col-lg-4">
            {/* <!--
                START: Sidebar

                Additional Classes:
                    .nk-sidebar-left
                    .nk-sidebar-right
                    .nk-sidebar-sticky
            --> */}
            <aside class="nk-sidebar nk-sidebar-right nk-sidebar-sticky">
                <div class="nk-widget">
            <div class="nk-widget-content">
            <form action="{% url 'search' %}" class="nk-form nk-form-style-1" novalidate="novalidate" method="get">
            <div class="input-group">
                <input type="text" class="form-control" placeholder="Type something..." onChange={(event) => setSearchValue(event.target.value)} />
                <button class="nk-btn nk-btn-color-main-1"><span class="ion-search"></span></button>
            </div>
            </form>
            </div>
            </div>


            <div class="nk-widget nk-widget-highlighted">
                <h4 class="nk-widget-title"><span><span class="text-main-1">Popular</span> News</span></h4>
                <div class="nk-widget-content">

                        {popularNews.map((post) => (  
                        
                        <div key={post.news_id} class="nk-widget-post">

                            <Link to={`/post/${post.news_id}`} key={post.news_id} id={post.news_id} class="nk-post-image">

                                <img src={`${post.image}`} alt="" />

                            </Link>

                            <h3 class="nk-post-title"> <Link to={`/post/${post.news_id}`} key={post.news_id} id={post.news_id}> {post.title} </Link></h3>
                            <div class="nk-post-date"><span class="fa fa-calendar"></span>{formatDate(post.time_update)}</div>
                        </div> 

                        ))}
                </div>
            </div>



            </aside>
            {/* <!-- END: Sidebar --> */}
        </div>
        )}
        </>
    );
}

export default SearchPanel;
