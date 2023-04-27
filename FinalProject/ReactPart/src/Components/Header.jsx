// import { AppBar, Toolbar, Typography, MenuItem } from "@mui/material";
import React from "react";
import logo from '../game/images/logo.png';
import { Link } from "react-router-dom";

function Header() {

    return (
        <>
        <header class="nk-header nk-header-opaque">
        <div class="nk-contacts-top">
            <div class="container">
            </div>
        </div>
        </header>

      <nav className="nk-navbar nk-navbar-top nk-navbar-sticky nk-navbar-autohide">
              <div className="container">
                  <div className="nk-nav-table">

    
                      <Link to="/" className="nk-nav-logo">
                            <img component={Link} to='/characters' src={logo} alt="GoodGames" width="50" />
                      </Link>

                      <ul className="nk-nav nk-nav-right d-none d-lg-table-cell" data-nav-mobile="#nk-nav-mobile">

              <li>
                  <Link to="/addpost">
                      Add Post
                  </Link>
              </li>


              <li>
                  <Link to="/register">
                      Sign Up
                  </Link>
              </li>

              <li>
                  <Link to="/login">
                      Log In
                  </Link>
              </li>

              <li>
                  <Link to="/about">
                      About
                  </Link>
              </li>



                        </ul>

                    <ul className="nk-nav nk-nav-right nk-nav-icons">

                            <li className="single-icon d-lg-none">
                                <a href="saf" className="no-link-effect" data-nav-toggle="#nk-nav-mobile">
                                    <span className="nk-icon-burger">
                                        <span className="nk-t-1"></span>
                                        <span className="nk-t-2"></span>
                                        <span className="nk-t-3"></span>
                                    </span>
                                </a>
                            </li>


                    </ul>
                </div>
            </div>
        </nav>
        

        </>
    );
}

export default Header;
