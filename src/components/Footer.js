// src/components/Footer.js
import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer" id="cta">
      <div className="cta-footer">
        <h3>Ready to Begin Your Quest?</h3>
        <a href="#hero" className="cta-button">Try Wellness Quest Now!</a>
      </div>
      <div className="footer-links">
        <a href="/privacy">Privacy Policy</a>
        <a href="/terms">Terms</a>
        <a href="mailto:contact@wellnessquest.com">Contact Us</a>
      </div>
      <p>&copy; {new Date().getFullYear()} Wellness Quest</p>
    </footer>
  );
}

export default Footer;
