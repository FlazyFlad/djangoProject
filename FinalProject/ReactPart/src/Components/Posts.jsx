import React from "react";
import { Link } from 'react-router-dom';

function Posts( props ) {

    const {formatDate, truncateWords, sortedItems, category, countComments} = props;


    return (
        <>
        
        {/* {% for p in news %} */}
            {sortedItems.map((post) => (
            <div key={post.news_id} class="nk-blog-post nk-blog-post-border-bottom">
                <div class="row vertical-gap">
                    <div class="col-lg-3 col-md-6">
                        <Link to={`/post/${post.news_id}`} key={post.news_id} id={post.news_id} class="nk-post-img">

                            <img src={`${post.image}`} alt="" />
                            
                            <span class="nk-post-categories">
                                {post.category_id === category[post.category_id - 1].category_id ?
                                <span class={'bg-main-' + post.category_id}> {category[post.category_id - 1].name} </span>
                                :
                                <span class={'bg-main-' + post.category_id}> Category </span>
                                }
                            </span>

                        </Link>


                        
                    </div>
                    <div class="col-lg-9 col-md-7">
                        <h2 class="nk-post-title h4">
                        <Link to={`/post/${post.news_id}`} key={post.news_id} id={post.news_id} >{post.title}</Link>
                        </h2>
                        <div class="nk-post-date mt-10 mb-10">
                            <span class="fa fa-calendar"></span> {formatDate(post.time_update)}
                            <span class="fa fa-comments"></span> <a href="da">{countComments(post.news_id)} comments</a>
                        </div>
                        <div class="nk-post-text">
                            <p> {truncateWords(post.content, 25)}  </p>
                        </div>
                    </div>
                </div>

        {/* {#    <div class="nk-gap"></div>#}
        {#    <a href="{{ p.get_absolute_url }}" class="nk-btn nk-btn-rounded nk-btn-color-dark-3 nk-btn-hover-color-main-1" style="padding: 10px 210px">Read More</a>#} */}
            </div>
            ))} 

        </>
        );
    }
    
    export default Posts;
    