// src/components/Footer.js
import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer" id="cta">
      <div className="cta-footer">
        <h3>Ready to Begin Your Quest?</h3>
        <a href="/auth" className="cta-button">Try Wellness Quest Now!</a>
      </div>
      <div className="footer-links">
        <a href="/privacy">Privacy Policy</a>
        <a href="/terms">Terms</a>
        <a href="mailto:hack.athon.02.2025@gmail.com">Contact Us</a>
      </div>
      <p>&copy; {new Date().getFullYear()} Wellness Quest</p>
    </footer>
  );
}

export default Footer;
