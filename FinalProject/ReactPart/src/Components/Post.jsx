import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import userIMG from '../game/images/user.png';
import { useNavigate } from "react-router-dom";
import axios from "axios";


const Post = ({props, category, comments}) => {

    const [popularNews, setPopularNews] = useState([]);

    useEffect(() =>{
    
        const fetchPNews = () => {
          axios
          .get('http://127.0.0.1:8000/api/v1/news/recomends/')
          .then(res => {
            setPopularNews(res.data);
          }).catch((err)=>{
            console.log(err);
          })    
        };
    
        fetchPNews();

    }, []);

    const navigate = useNavigate();
    // const [user, setUser] = useState("");    
    const [content, setContent] = useState("");
    const [comment, setComment] = useState(comments);

    const [isLoading, setIsLoading] = useState(true);
    const { id } = useParams();

    const post = props.find(({news_id}) => news_id === parseInt(id));
    const postCategory = category.find(({category_id}) => category_id === post?.category_id)

    function formatDate(isoDate) {
        const date = new Date(isoDate);
        const day = date.getDate();
        const month = date.toLocaleString('default', { month: 'long' });
        const year = date.getFullYear();
        return `${day} ${month}, ${year}`;
    }

    function linebreaksFilter(text) {
        const parts = text.split('\n');
        return parts.map((part, i) => <React.Fragment key={i}>{part}<br/></React.Fragment>);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        // Создаем объект FormData для отправки данных на сервер
        const formData = new FormData();
        formData.append("user", 1);
        formData.append("news", parseInt(id));
        formData.append("content", content);
    
        try {
          // Отправляем данные на сервер с помощью axios
          const response = await axios.post("http://127.0.0.1:8000/api/v1/comment/", formData);
          console.log(response.data);
          navigate(`/post/${id}`);
          setComment([...comments, response.data]);
        } catch (error) {
          console.error(error);
        }
      };

    const countComments = (id) => {
        let count = 0;  
        comment.forEach((comment) => {
          if (comment.news === id) {
            count++;
          }
        });
        return count;
      };

      const filteredComments = comment.filter(item => item.news === parseInt(id));
      

    useEffect(() => {
        if (post && postCategory) {
            setIsLoading(false)
        }
    }, [post?.news_id, postCategory?.category_id, post, postCategory]);
    

    return (
        <>
        {isLoading ? (
            <p>Loading...</p>
          ) : (
        <div>
        <div class="nk-gap-1"></div>
        <div class="container">
            <ul class="nk-breadcrumbs">


                <li>
                <Link to="/"> 
                    Home
                </Link> 
                </li>

                <li><svg class="svg-inline--fa fa-angle-right fa-w-8" aria-hidden="true" data-prefix="fa" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"></path></svg></li>

                <li>
                <Link to={`/post/${post.news_id}`}> 
                { postCategory.name }
                </Link> 
                </li>

                <li><svg class="svg-inline--fa fa-angle-right fa-w-8" aria-hidden="true" data-prefix="fa" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"></path></svg></li>

                <li>
                <Link to={`/post/${post.news_id}`}> 
                    Post
                </Link> 
                </li>

                <li><span>{post.title}</span></li>

            </ul>
        </div>


        <div class="nk-gap-1"></div>


        <div class="container">
            <div class="row vertical-gap">
                <div class="col-lg-8">

                    <div class="nk-post-img">
                        <img src={`${post.image}`} alt="" />
                    </div>

                    <div class="nk-gap-1"></div>


                    <div class="nk-post-by">
                                {formatDate(post.time_update)}

                                <div class="nk-post-categories">
                                    <span class={`bg-main-${post.category_id}`}> {postCategory.name} </span>
                                </div>
                    </div>

                    <div class="nk-gap"></div>

                    <div class="nk-gap"></div>

                    <p>{linebreaksFilter(post.content)}</p>

                    <div class="nk-gap"></div>

                    <div class="nk-gap"></div>


                {/* Comment Start */}
                <div id="comments"></div>
                <h3 class="nk-decorated-h-2"><span><span class="text-main-1">{countComments(parseInt(id))}</span> Comments</span></h3>
                <div class="nk-gap"></div>
                <div class="nk-comments">

                {filteredComments.map((comment) => (
                    <div key={comment.comment_id} class="nk-comment">
                        <div class="nk-comment-meta">
                            <img src={userIMG} alt="user" class="rounded-circle" width="35" /> by <a href="/#">{comment.user}</a>
                            {/* <a href="/#" class="nk-btn nk-btn-rounded nk-btn-color-dark-3 float-right">Reply</a> */}
                        </div>
                        <div class="nk-comment-text">
                            <p>{comment.content}</p>
                        </div>
                    </div>
                ))} 

                </div>
                {/* Comment End */}


                {/* Reply Start */}
                <div class="nk-gap-2"></div>
                <h3 class="nk-decorated-h-2"><span><span class="text-main-1">Leave</span> a Reply</span></h3>
                <div class="nk-gap"></div>
                <div class="nk-reply">
                    <form action="#" class="nk-form" novalidate="novalidate" onSubmit={handleSubmit}>
                        <div class="row sm-gap vertical-gap">
                        </div>
                        <div class="nk-gap-1"></div>
                        <textarea class="form-control required" name="message" rows="5" placeholder="Message *" aria-required="true" value={content} onChange={(e) => setContent(e.target.value)}></textarea>
                        <div class="nk-gap-1"></div>
                        <div class="nk-form-response-success"></div>
                        <div class="nk-form-response-error"></div>
                        <button class="nk-btn nk-btn-rounded nk-btn-color-main-1" type="submit">Post Comment</button>
                    </form>
                </div>
                {/* Reply End */}


                </div>
                <div class="col-lg-4">
                    <aside class="nk-sidebar nk-sidebar-right nk-sidebar-sticky">
                        <div class="nk-widget">
            <div class="nk-widget-content">
                <form action="#" class="nk-form nk-form-style-1" novalidate="novalidate">
                    <div class="input-group">
                        <input type="text" class="form-control" placeholder="Type something..." />
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
                </div>
            </div>
        </div>
    </div>
    )}
    </>
    );
}

export default Post;
