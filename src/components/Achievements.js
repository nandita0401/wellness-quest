import React from "react";
import { motion } from "framer-motion";
import { FaMedal, FaLock, FaTimes } from "react-icons/fa";
import "./Achievements.css";

const badgeCriteria = [
  { id: "firstQuest", name: "First Quest Completed", xpRequired: 10 },
  { id: "xp50", name: "Level 1 Achiever", xpRequired: 30 },
  { id: "xp100", name: "Level 2 Achiever", xpRequired: 40 },
  { id: "xp100", name: "Level 3 Achiever", xpRequired: 150 },
];

// Mood Options
const moodOptions = [
    "Anxiety/Stress", "Sadness/Despair", "Happiness/Joy",
    "Disappointment/Regret", "Shame/Guilt", "Pride/Confidence",
    "Comparison/Social Pressure", "Empathy/Compassion", "Anger/Resentment",
    "Curiosity/Awe", "Belonging/Connection", "Nostalgia/Irony",
    "Love/Trust"
  ];

const Achievements = ({ onLogMood, isMoodPopupOpen, setIsMoodPopupOpen, achievements }) => {
  return (
    <div className="achievements-container">
      <h2>🏆 Your Achievements</h2>
      <div className="achievement-grid">
        {badgeCriteria.map((badge, index) => (
          <motion.div
            key={index}
            className={`achievement-card ${achievements.includes(badge.name) ? "unlocked" : "locked"}`}
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5, delay: index * 0.2 }}
          >
            {achievements.includes(badge.name) ? (
              <>
                <FaMedal className="badge-icon" />
                <p>{badge.name}</p>
              </>
            ) : (
              <>
                <FaLock className="badge-icon locked-icon" />
                <p>{badge.name}</p>
              </>
            )}
          </motion.div>
        ))}
      </div>

      {/* Mood Popup */}
      {isMoodPopupOpen && (
        <div className="mood-popup">
          <div className="mood-popup-content">
            <div className="mood-popup-header">
              <h3 className="select-heading">Select Your Mood</h3>
              <FaTimes className="close-btn" onClick={() => setIsMoodPopupOpen(false)} />
            </div>
            <div className="mood-options">
              {moodOptions.map((mood, index) => (
                <button key={index} className="mood-btn" onClick={() => setIsMoodPopupOpen(false)}>
                  {mood}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}


    </div>
  );
};

export default Achievements;
