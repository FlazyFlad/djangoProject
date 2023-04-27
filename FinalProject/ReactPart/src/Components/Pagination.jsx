// import { AppBar, Toolbar, Typography, MenuItem } from "@mui/material";
import React from "react";


function Pagination({ postsPerPage, totalPosts, currentPage, paginate  }) {
    const pageNumbers = []

    for (let i=1; i<=Math.ceil(totalPosts / postsPerPage); i++){
        pageNumbers.push(i)
    }

    return (
        <>
        <div class="nk-pagination nk-pagination-center">
            <nav>
            
                <a href="/#" onClick={() => paginate(1)}>&lt;&lt;</a>

                {currentPage !== 1 ?
                <a href="/#" onClick={() => paginate(currentPage-1)}>&lt;</a>
                :
                <a href="/#">&lt;</a>
                }
    
                    {pageNumbers.map((number) => (
                        <a  key={number} href="/#" onClick={() => paginate(number)} className={`${currentPage === number ? "nk-pagination-current" : ""}`}> {number} </a>
                    ))}


                {currentPage !== pageNumbers.length ?
                <a href="/#" onClick={() => paginate(currentPage+1)}>&gt;</a>
                :
                <a href="/#">&gt;</a>
                }


                <a href="/#" onClick={() => paginate(pageNumbers.length)}>&gt;&gt;</a>
            
            </nav>
        </div>

        </>
    );
}

export default Pagination;
