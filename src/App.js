// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Hero from './components/Hero';
import Features from './components/Features';
import DataVisualization from './components/DataVisualization';
import Testimonials from './components/Testimonials';
import HowItWorks from './components/HowItWorks';
import AboutTeam from './components/AboutTeam';
import Footer from './components/Footer';
import Auth from './components/Auth';


function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route
          path="/"
          element={
            <>
              <Hero />
              <Features />
              <DataVisualization />
              <Testimonials />
              <HowItWorks />
              <AboutTeam />
              <Footer />
            </>
          }
        />
        <Route path="/auth" element={<Auth />} />
      </Routes>
    </Router>
  );
}

export default App;
