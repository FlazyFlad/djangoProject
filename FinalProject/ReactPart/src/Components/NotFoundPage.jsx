// import { AppBar, Toolbar, Typography, MenuItem } from "@mui/material";
import React from "react";


function NotFoundPage() {

    return (
        <>
        <div class="nk-main">



            <div class="nk-fullscreen-block">
                <div class="nk-fullscreen-block-top">
                    <div class="text-center">
                        <div class="nk-gap-4"></div>
                    </div>
                </div>
                <div class="nk-fullscreen-block-middle">
                    <div class="container text-center">
                        <div class="row">
                            <div class="col-md-6 offset-md-3 col-lg-4 offset-lg-4">
                                <h1 class="text-main-1" style={{fontSize: '150px'}}>404</h1>

                                <div class="nk-gap"></div>
                                <h2 class="h4">You chose the wrong path!</h2>

                                <div>Or such a page just doesn't exist... <br /> Would you like to go back to the homepage?</div>
                                <div class="nk-gap-3"></div>

                                <a href="{% url 'home' %}" class="nk-btn nk-btn-rounded nk-btn-color-white">Return to Homepage</a>
                            </div>
                        </div>
                        <div class="nk-gap-3"></div>
                    </div>
                </div>
                <div class="nk-fullscreen-block-bottom">
                    <div class="nk-gap-2"></div>
                    <div class="nk-gap-2"></div>
                </div>
            </div>
        </div>
        </>
    );
}

export default NotFoundPage;
