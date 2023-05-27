
import './App.css';
import { useNavigate } from 'react-router-dom';
// import { ContactFormAbi } from './abi/abis';
import React from 'react';
import Web3 from 'web3';
// import { contractAddr } from './abi/address';
import { contractAddr } from './imports/contract';
import { contractABI } from './imports/abi';
import "./start.css";
import logo from './logo.png';
import "./dropdown.css";
// import { panelURL } from './imports/panel';
import { streamlitURL } from './imports/streamlit';

const web3 = new Web3(Web3.givenProvider);
// const contractAddr = "0xAa1FDC199fD3bB6165fab7EeDF6504276F3DE3DA";
const CFContract = new web3.eth.Contract(contractABI, contractAddr);

function App() {
const navigate = useNavigate()
const [formStatus, setFormStatus] = React.useState('Send')
const onSubmit =  async (e) => {
  e.preventDefault()
  setFormStatus('Submitting...')
  const { FirstName, LastName, Email, Portfolio } = e.target.elements
  let conFom = {
    FirstName: FirstName.value,
    LastName: LastName.value,
    Email: Email.value,
    Portfolio: Portfolio.value,

  }

  console.log(conFom)
  console.log(FirstName.value, LastName.value, Email.value, Portfolio.value)

const accounts = await window.ethereum.enable();
const account = accounts[0];
// const gas = await CFContract.methods.insertUpdateUser(FirstName.value, LastName.value, Email.value, Portfolio.value)
//                     .estimateGas();
const result = await CFContract.methods.insertUpdateUser(FirstName.value, LastName.value, Email.value, Portfolio.value).send({
  from: account
})
console.log(result);


  setFormStatus('Sent!')
  navigate('/confirmation')
}


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
                              <li class="nav-item"><a class="nav-link link text-black display-4" href= { streamlitURL } target="_blank" rel="noreferrer">Advisors<br/><br/></a></li></ul>


                      </div>
                  </div>
              </nav>

          </section>
<br/><br/><br/><br/><br/>

    <div id="heading">
            <div className="title">
                <h1>Client Engagement Form</h1>
            </div>







    <form onSubmit={onSubmit}>
      <div className="mb-3">
        <label className="form-label" htmlFor="FirstName">
          First Name
        </label>
        <input className="form-control" type="text" id="FirstName" required />
      </div>
      <br/><br/>
      <div className="mb-3">
        <label className="form-label" htmlFor="LastName">
          Last Name
        </label>
        <input className="form-control" type="text" id="LastName" required />
      </div>
      <br/><br/>
      <div className="mb-3">
        <label className="form-label" htmlFor="Email">
          Email
        </label>
        <input className="form-control" type="email" id="Email" required />
      </div>
      <br/><br/>
      {/* <div className="mb-3">
        <label className="form-label" htmlFor="Portfolio">
          Desired Portfolio
        </label>
        <input className="form-control" id="Portfolio" required />
      </div> */}
      <div className="mb-3">
        <label className="form-label" htmlFor="Portfolio">
          Desired Portfolio
        </label><br></br>
        <input className="form-control" type="text" id="Portfolio" required />

      </div>
      <br/><br/>
      <button className="btn btn-danger" type="submit">
        {formStatus}
      </button>
    </form>

        </div>

</div>
  );
}

export default App;
