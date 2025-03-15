// src/components/Hero.js
import React from 'react';
import './Hero.css'; // Specific hero styles (optional)

function Hero() {
  return (
    <section 
      className="hero" 
      id="hero" 
      data-aos="fade-up"
    >
      <div className="hero-content">
        <h1>Transform Your Wellness Journey into an Epic Quest</h1>
        <p>Track mental health, complete fun challenges, and level up daily.</p>
        <a href="#features" className="cta-button">Get Started</a>
      </div>
    </section>
  );
}

export default Hero;
