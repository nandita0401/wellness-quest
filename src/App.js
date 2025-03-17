import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Features from "./components/Features";
import DataVisualization from "./components/DataVisualization";
import Testimonials from "./components/Testimonials";
import HowItWorks from "./components/HowItWorks";
import AboutTeam from "./components/AboutTeam";
import Footer from "./components/Footer";
import Auth from "./components/Auth";
import Dashboard from "./components/Dashboard";
import Quests from "./components/Quests"; // Import Quests Page
import Achievements from "./components/Achievements";

const initialQuests = [
  { id: 1, name: '5-Minute Meditation', xp: 10, completed: false },
  { id: 2, name: '10 Squats', xp: 15, completed: false },
  { id: 3, name: 'Drink 8 Glasses of Water', xp: 5, completed: false },
  { id: 4, name: 'Read for 10 Minutes', xp: 10, completed: false },
];

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isMoodPopupOpen, setIsMoodPopupOpen] = useState(false);
  const [achievements, setAchievements] = useState([]);

  // ✅ NEW: Store XP, level, and quests globally
  const [xp, setXp] = useState(0);
  const [level, setLevel] = useState(1);
  const [quests, setQuests] = useState(initialQuests);

  return (
    <Router>
      <Header onLogMood={() => setIsMoodPopupOpen(true)} />
      <Routes>
        <Route path="/" element={<>
          <Hero />
          <Features />
          <DataVisualization />
          <Testimonials />
          <HowItWorks />
          <AboutTeam />
          <Footer />
        </>} />
        <Route path="/auth" element={<Auth setIsAuthenticated={setIsAuthenticated} />} />
        <Route path="/dashboard" element={
          isAuthenticated ? <Dashboard isMoodPopupOpen={isMoodPopupOpen} setIsMoodPopupOpen={setIsMoodPopupOpen} /> : <Navigate to="/auth" />
        } />
        <Route path="/quests" element={
          isAuthenticated ? <Quests onLogMood={() => setIsMoodPopupOpen(true)} isMoodPopupOpen={isMoodPopupOpen} setIsMoodPopupOpen={setIsMoodPopupOpen} achievements={achievements} setAchievements={setAchievements} xp={xp} setXp={setXp} level={level} setLevel={setLevel} quests={quests} setQuests={setQuests} /> : <Navigate to="/auth" />
        } />
        <Route path="/achievements" element={ 
          isAuthenticated ? <Achievements onLogMood={() => setIsMoodPopupOpen(true)} isMoodPopupOpen={isMoodPopupOpen} setIsMoodPopupOpen={setIsMoodPopupOpen} achievements={achievements} /> : <Navigate to="/auth" />
        } />
      </Routes>
    </Router>


  );
}

export default App;
