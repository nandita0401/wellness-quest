// src/components/Header.js
import React from 'react';
import './Header.css';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="header">
      <div className="logo">
      <Link to="/">Wellness Quest</Link></div>
      <nav>
        <ul>
          <li><a href="#features">Features</a></li>
          <li><a href="#data">Data</a></li>
          <li><a href="#howitworks">How It Works</a></li>
          <li><a href="#team">Team</a></li>
          <li><Link to="/auth">Sign Up</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
