// src/components/Auth.js
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Auth.css";
import axios from "axios";
import { FaUser, FaEnvelope, FaLock, FaBrain } from "react-icons/fa";

function Auth({ setIsAuthenticated }) {
  const [isSignIn, setIsSignIn] = useState(true);
  const [error, setError] = useState(null);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");

  const navigate = useNavigate();
  const API_URL = "http://127.0.0.1:8000/"; // Ensure this is your FastAPI backend URL

  const handleToggle = () => {
    setIsSignIn(!isSignIn);
    setError(null);
  };

  // const handleSubmit = async (e) => {
  //   e.preventDefault();

  //   // Mock authentication success
  //   setIsAuthenticated(true);
  //   navigate("/dashboard");
  // };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      if (isSignIn) {
        // 🔹 Login Request
        const response = await axios.post(`${API_URL}/login`, {
          email,
          password,
        });

        localStorage.setItem("token", response.data.access_token);
        localStorage.setItem("email", email);
        setIsAuthenticated(true);
        navigate("/dashboard");
      } else {
        // 🔹 Signup Request
        await axios.post(`${API_URL}/register`, {
          name,
          email,
          password,
        });

        alert("Signup successful! Please login.");
        setIsSignIn(true); // Switch to login view after signup
      }
    } catch (error) {
      setError(error.response?.data?.detail || "Something went wrong");
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
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
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div className="input-group">
            <FaLock className="icon" />
            <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <button type="submit" className="auth-button">{isSignIn ? "Sign In" : "Sign Up"}</button>
        </form>
        {error && <div className="form-feedback error">{error}</div>}
        <div className="auth-toggle">
          {isSignIn ? <p>New user? <span onClick={handleToggle} className="toggle-link">Sign Up</span></p> 
          : <p>Already have an account? <span onClick={handleToggle} className="toggle-link">Sign In</span></p>}
        </div>
      </div>
    </div>
  );
}

export default Auth;
