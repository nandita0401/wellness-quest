import React from "react";
import { useNavigate, Link, useLocation } from "react-router-dom";
import "./Header.css";

function Header({ onLogMood }) {
  const navigate = useNavigate();
  const location = useLocation();
  const isDashboard = location.pathname === "/dashboard" || location.pathname === "/quests" || location.pathname === "/achievements";

  return (
    <header className="header">
      <div className="logo">
        <Link to="/">Wellness Quest</Link>
      </div>

      {isDashboard ? (
        <nav>
        <ul>
          {/* <li>
            <Link to="/quests" className="nav-link quests-link">Quests</Link>
          </li> */}
          <li>
            <button className="nav-link quest-link" onClick={() => navigate("/quests")}>
              Quests
            </button>
          </li>
          <li>
            <button className="nav-link log-mood-link" onClick={onLogMood}>
              Log Your Mood
            </button>
          </li>
          <li>
            <button className="nav-link achievement-link" onClick={() => navigate("/achievements")}>
              Achievements
            </button>
          </li>
        </ul>
      </nav>
      
      ) : (
        <nav>
          <ul>
            <li><a href="#features" className="nav-link">Features</a></li>
            <li><a href="#data" className="nav-link">Data</a></li>
            <li><a href="#howitworks" className="nav-link">How It Works</a></li>
            <li><a href="#team" className="nav-link">Team</a></li>
            <li><Link to="/auth" className="nav-link">Sign Up</Link></li>
          </ul>
        </nav>
      )}
    </header>
  );
}

export default Header;
