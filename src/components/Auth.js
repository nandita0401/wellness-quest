// src/components/Auth.js
import React, { useState } from 'react';
import './Auth.css';
import { FaUser, FaEnvelope, FaLock, FaBrain } from 'react-icons/fa';

function Auth() {
  const [isSignIn, setIsSignIn] = useState(true);
  const [formSubmitted, setFormSubmitted] = useState(false);
  
  const handleToggle = () => {
    setIsSignIn(!isSignIn);
    setFormSubmitted(false);
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate a sign in/up process (replace with your actual logic)
    setFormSubmitted(true);
    // Optionally clear the success message after a delay:
    setTimeout(() => {
      setFormSubmitted(false);
      // You could also redirect the user here
    }, 2000);
  };
  
  return (
    <div className="auth-container">
      <div className="auth-card" data-aos="fade-up">
        <div className="auth-header">
          <FaBrain className="auth-brain-icon" />
          <h2>{isSignIn ? "Sign In" : "Sign Up"}</h2>
        </div>
        <form onSubmit={handleSubmit} className="auth-form">
          {!isSignIn && (
            <div className="input-group">
              <FaUser className="icon" />
              <input type="text" placeholder="Name" required />
            </div>
          )}
          <div className="input-group">
            <FaEnvelope className="icon" />
            <input type="email" placeholder="Email" required />
          </div>
          <div className="input-group">
            <FaLock className="icon" />
            <input type="password" placeholder="Password" required />
          </div>
          { !isSignIn && (
            <div className="input-group">
              <FaLock className="icon" />
              <input type="password" placeholder="Confirm Password" required />
            </div>
          )}
          <button type="submit" className="auth-button">
            {isSignIn ? "Sign In" : "Sign Up"}
          </button>
        </form>
        <div className="auth-toggle">
          {isSignIn ? (
            <p>
              New user?{" "}
              <span onClick={handleToggle} className="toggle-link">
                Sign Up
              </span>
            </p>
          ) : (
            <p>
              Already have an account?{" "}
              <span onClick={handleToggle} className="toggle-link">
                Sign In
              </span>
            </p>
          )}
        </div>
        {formSubmitted && (
          <div className="form-feedback" data-aos="fade-in">
            <p>{isSignIn ? "Signed in successfully!" : "Signed up successfully!"}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Auth;
