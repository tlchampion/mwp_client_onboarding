import React from 'react';
import "./App.css";
import "./start.css";
// import { Panel } from "./panel";
import logo from './logo.png';
// import header from './header.jpg';
import "./dropdown.css";
import { panelURL } from './imports/panel';
import { streamlitURL } from './imports/streamlit';

const Start = () => {
    return (


<div>

        <section data-bs-version="5.1" class="menu cid-s48OLK6784" once="menu" id="menu1-h">

            <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
                <div class="container">
                    <div class="navbar-brand">
                        <span class="navbar-logo">
                            <a href="/">
                                <img src={logo}  style={{height: '3.8rem'}} alt="company logo" />
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
                        <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-black display-4" href= { streamlitURL } target="_blank" rel="noreferrer">Current Clients</a></li>
                            <li class="nav-item"><a class="nav-link link text-black display-4" href={ streamlitURL } target="_blank" rel="noreferrer">Advisors<br/><br/></a></li></ul>


                    </div>
                </div>
            </nav>

        </section>

        <section data-bs-version="5.1" class="header1 cid-s48MCQYojq mbr-fullscreen mbr-parallax-background" id="header1-f">



            <div class="mbr-overlay" style={{opacity: '0.8',backgroundColor: '#ffffff'}}> </div>

            <div class="align-center container">
                <div class="row justify-content-center">
                    <div class="col-12 col-lg-8">
                        {/* <img src={header}   /> */}
                        <h1 class="mbr-section-title mbr-fonts-style mb-3 display-1"><strong>Welcome</strong></h1>

                        <p class="mbr-text mbr-fonts-style display-7">Here at MyWealthPath we are dedicated to your financial success. Offering multiple investment opportunities we have not doubt that we can find a solution to meet your needs, whatever they are.<br/><br/>To review information about our investment strategies please use the button below.</p>
                        <div class="mbr-section-btn mt-3"><a class="btn btn-success display-4" href= { panelURL } target="_blank" rel="noreferrer">Show Me!</a></div>

                       <p class="mbr-text mbr-fonts-style display-7"> If you would like to work with us to meet your investment needs, please use the button below to access our contact form.  Once we receive your information we will initiate the account creation process and reach out to you within 7 to 10 business days to answer any questions you have and complete the onboarding process.</p>

                        <div class="mbr-section-btn mt-3"><a class="btn btn-success display-4" href="/contact"  >Let's Go!</a></div>
                    </div>
                </div>
            </div>
        </section>

        <section data-bs-version="5.1" class="content1 cid-s48udlf8KU" id="content1-8">

            <div class="container">
                <div class="row justify-content-center">
                    <div class="title col-12 col-md-9">
                        <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2"><strong>Wauris Vitae Ultricies Leo</strong></h3>
                        <h4 class="mbr-section-subtitle align-center mbr-fonts-style mb-4 display-7">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ornare massa eget egestas purus. Mauris rhoncus aenean vel elit. Fames ac turpis egestas sed tempus urna et pharetra. Quisque id diam vel quam elementum. Venenatis tellus in metus vulputate eu scelerisque. Tellus in metus vulputate eu scelerisque felis. Volutpat lacus laoreet non curabitur gravida arcu ac tortor. Congue quisque egestas diam in. Sodales neque sodales ut etiam sit. Nisi est sit amet facilisis magna. Urna cursus eget nunc scelerisque viverra. Tempus egestas sed sed risus pretium quam vulputate dignissim suspendisse.<div><br/></div><div>Odio euismod lacinia at quis risus sed vulputate. Leo duis ut diam quam nulla porttitor. Tincidunt nunc pulvinar sapien et ligula ullamcorper. Amet tellus cras adipiscing enim eu turpis egestas pretium. Metus aliquam eleifend mi in nulla. Vulputate mi sit amet mauris commodo quis imperdiet. Nisi quis eleifend quam adipiscing vitae. Natoque penatibus et magnis dis parturient montes. Turpis egestas sed tempus urna et pharetra. Pellentesque nec nam aliquam sem. Aliquam faucibus purus in massa tempor nec feugiat nisl pretium. Urna porttitor rhoncus dolor purus. Blandit turpis cursus in hac habitasse. Posuere sollicitudin aliquam ultrices sagittis orci a. Non arcu risus quis varius quam. Dapibus ultrices in iaculis nunc sed augue lacus viverra. Ullamcorper morbi tincidunt ornare massa eget. Ipsum a arcu cursus vitae congue. Dolor sit amet consectetur adipiscing elit ut aliquam purus sit.</div><div>/<br/></div><div>Cras tincidunt lobortis feugiat vivamus. Sed adipiscing diam donec adipiscing tristique risus nec feugiat in. Viverra vitae congue eu consequat ac. Adipiscing commodo elit at imperdiet dui accumsan sit. Et ultrices neque ornare aenean euismod. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque dignissim. Cum sociis natoque penatibus et magnis dis. Blandit libero volutpat sed cras. Vulputate ut pharetra sit amet aliquam id diam maecenas ultricies. Viverra nibh cras pulvinar mattis nunc sed blandit. Condimentum vitae sapien pellentesque habitant morbi tristique senectus. Purus sit amet volutpat consequat mauris. At lectus urna duis convallis convallis tellus id interdum velit. Quisque non tellus orci ac auctor augue mauris augue neque. Amet porttitor eget dolor morbi. Leo duis ut diam quam nulla. Amet porttitor eget dolor morbi non arcu risus. Orci ac auctor augue mauris.</div><div><br/></div><div>Senectus et netus et malesuada fames ac turpis egestas integer. Dolor sit amet consectetur adipiscing. Feugiat nibh sed pulvinar proin. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Cras fermentum odio eu feugiat pretium nibh ipsum consequat. Eget mauris pharetra et ultrices neque. Eu feugiat pretium nibh ipsum consequat nisl vel. Tristique magna sit amet purus gravida quis blandit turpis cursus. Accumsan lacus vel facilisis volutpat est velit egestas dui id. Amet est placerat in egestas. Vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis. Sed egestas egestas fringilla phasellus faucibus. Gravida arcu ac tortor dignissim convallis. Purus in mollis nunc sed id. Urna condimentum mattis pellentesque id nibh tortor id aliquet lectus. Libero nunc consequat interdum varius sit amet mattis vulputate. Euismod quis viverra nibh cras pulvinar. Sed arcu non odio euismod lacinia at quis risus sed.</div><div><br/></div><div>Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula ipsum. In fermentum posuere urna nec. Tempor orci eu lobortis elementum nibh tellus molestie. Elit eget gravida cum sociis natoque penatibus et magnis dis. Suscipit tellus mauris a diam maecenas sed. Sed id semper risus in hendrerit gravida rutrum quisque non. Vitae turpis massa sed elementum tempus egestas. Ut diam quam nulla porttitor massa. Libero volutpat sed cras ornare arcu dui vivamus. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Purus faucibus ornare suspendisse sed nisi lacus sed viverra tellus. Suspendisse sed nisi lacus sed viverra tellus in. Fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec. Nunc consequat interdum varius sit amet. Mauris rhoncus aenean vel elit scelerisque.</div></h4>

                    </div>
                </div>
            </div>
        </section>

        <section data-bs-version="5.1" class="content1 cid-s48vaXqeL6" id="content1-b">

            <div class="container">
                <div class="row justify-content-center">
                    <div class="title col-12 col-md-9">
                        <h3 class="mbr-section-title mbr-fonts-style align-center mb-4 display-2"><strong>Dui Vivamus Arcu Felis Bibendum</strong></h3>
                        <h4 class="mbr-section-subtitle align-center mbr-fonts-style mb-4 display-7">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed blandit libero volutpat sed cras ornare arcu dui. Eget nunc scelerisque viverra mauris. Purus viverra accumsan in nisl nisi. In est ante in nibh mauris cursus mattis molestie a. Adipiscing elit pellentesque habitant morbi tristique senectus. Vel pharetra vel turpis nunc eget lorem dolor sed. Tempus iaculis urna id volutpat. Consectetur adipiscing elit ut aliquam purus sit. Volutpat odio facilisis mauris sit. Elit pellentesque habitant morbi tristique senectus et netus et. Luctus accumsan tortor posuere ac ut consequat semper. Mauris pellentesque pulvinar pellentesque habitant morbi tristique. Id donec ultrices tincidunt arcu non sodales neque sodales ut. Semper risus in hendrerit gravida rutrum quisque. Diam ut venenatis tellus in metus vulputate eu scelerisque. Dictumst quisque sagittis purus sit. Volutpat diam ut venenatis tellus in metus.</h4>

                    </div>
                </div>
            </div>
        </section>
</div>

    );
};

export default Start;
