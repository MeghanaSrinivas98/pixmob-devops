import React from 'react';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Signin from './Signin';
import Profile from './Profile';

function App() {
  const token = localStorage.getItem('user');

  if(!token) {
    return <Signin />
  }

  return <Profile />
}

export default App;
