import React from "react";
import { Link } from "react-router-dom";

function Breadcrumbs() {

    return (
        <>
        {/* <!-- START: Breadcrumbs --> */}
        <div class="nk-gap-1"></div>
        <div class="container">
            <ul class="nk-breadcrumbs">
    
    
                <li>
                    <Link to="/">
                        Home
                    </Link>
                </li>

                <li><span class="fa fa-angle-right"></span></li>
    
                <li><span>News</span></li>
    
            </ul>
        </div>
        <div class="nk-gap-1"></div>
        {/* <!-- END: Breadcrumbs --> */}
        </>
    );
}

export default Breadcrumbs;
