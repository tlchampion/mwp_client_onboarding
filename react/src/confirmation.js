import React from 'react';
import "./App.css";
import "./start.css";
import logo from './logo.png';
import "./dropdown.css";
// import { panelURL } from './imports/panel';
import { streamlitURL } from './imports/streamlit';

const Confirmation = () => {
    return (


<div>

      <section data-bs-version="5.1" class="menu cid-s48OLK6784" once="menu" id="menu1-h">

                  <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
                      <div class="container">
                          <div class="navbar-brand">
                              <span class="navbar-logo">
                                  <a href="/">
                                      <img src={logo}  style={{height: '3.8rem'}} alt="company logo"/>
                                  </a>
                              </span>
                              <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-7" href="/"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        MyWealthPath      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   <br/><br/></a></span>
                          </div>

      {/* <button class="navbar-toggler" type="button" data-toggle="collapse" data-bs-toggle="collapse" data-target="#navbarSupportedContent" data-bs-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <div class="hamburger">
              <span></span>
              <span></span>
              <span></span>
              <span></span>
          </div>
      </button> */}

                          <div class="collapse navbar-collapse" id="navbarSupportedContent">
                              <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-black display-4" href={ streamlitURL } target="_blank" rel="noreferrer">Current Clients</a></li>
                                  <li class="nav-item"><a class="nav-link link text-black display-4" href= { streamlitURL } target="_blank" rel="noreferrer">Advisors<br/><br/></a></li></ul>


                          </div>
                      </div>
                  </nav>

              </section>
        <br/><br/><br/><br/><br/>
        <div id="heading">
            <h1>Thank You</h1>
            Your contact information has been received. We will contact you within 7 to 10 days to schedule a meeting to discuss your investment goals and finalize the onboarding process.

            <br/>
            <br/>




        </div>
</div>
    );
};

export default Confirmation;
