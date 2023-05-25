import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Confirmation from './confirmation';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Start from './start';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route index element={<Start />} />
        <Route path="confirmation" element={<Confirmation />} />
        <Route path="contact" element={<App />} />

        {/* <Route index element={<App />} />
        <Route path="confirmation" element={<Confirmation />} />
        <Route path="start" element={<Start />} /> */}

      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
