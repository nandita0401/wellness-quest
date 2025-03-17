import React, { useState } from 'react';
import { motion, AnimatePresence } from "framer-motion";
import './Quests.css';
import Confetti from "react-confetti";
import { FaMedal, FaTimes } from "react-icons/fa";
import useSound from "use-sound";
// import badgeSound from "../assets/badge-unlock.mp3"; 

const initialQuests = [
  { id: 1, name: '5-Minute Meditation', xp: 10, completed: false },
  { id: 2, name: '10 Squats', xp: 15, completed: false },
  { id: 3, name: 'Drink 8 Glasses of Water', xp: 5, completed: false },
  { id: 4, name: 'Read for 10 Minutes', xp: 10, completed: false },
];

const badgeCriteria = [
    { id: "firstQuest", name: "First Quest Completed", xpRequired: 10 },
    { id: "xp50", name: "Level 1 Achiever", xpRequired: 30 },
    { id: "xp100", name: "Level 2 Achiever", xpRequired: 40 },
    { id: "xp100", name: "Level 2 Achiever", xpRequired: 100 }
  ];

// Mood Options
const moodOptions = [
    "Anxiety/Stress", "Sadness/Despair", "Happiness/Joy",
    "Disappointment/Regret", "Shame/Guilt", "Pride/Confidence",
    "Comparison/Social Pressure", "Empathy/Compassion", "Anger/Resentment",
    "Curiosity/Awe", "Belonging/Connection", "Nostalgia/Irony",
    "Love/Trust"
  ];

  // Hardcoded AI Suggestions (Later, we will fetch these from AI backend)
const suggestions = {
    "Anxiety/Stress": "Try a 5-minute deep breathing exercise 🧘‍♂️",
    "Sadness/Despair": "Watch a short uplifting video or listen to a happy song 🎶",
    "Happiness/Joy": "Celebrate your mood! Share a positive thought with a friend 😊",
    "Disappointment/Regret": "Write down your feelings and one lesson learned from this experience 📖",
    "Curiosity/Awe": "Explore something new! Read an interesting fact or try a new hobby 🌎",
    "Love/Trust": "Express gratitude to someone close to you 💖",
  };

  

const Quests = ({ onLogMood, isMoodPopupOpen, setIsMoodPopupOpen, achievements, setAchievements, xp, setXp, level, setLevel, quests, setQuests }) => {
//   const [quests, setQuests] = useState(initialQuests);
//   const [xp, setXp] = useState(0);
//   const [level, setLevel] = useState(1);
//   const [isMoodPopupOpen, setIsMoodPopupOpen] = useState(false);

//   const [achievements, setAchievements] = useState([]);
  const [newBadge, setNewBadge] = useState(null);
  const [showConfetti, setShowConfetti] = useState(false);
//   const [play] = useSound(badgeSound, { volume: 0.5 });
const [isFlipped, setIsFlipped] = useState(false);
const [selectedMood, setSelectedMood] = useState(null);


const handleMoodSelect = (mood) => {
    setSelectedMood(mood);
    setIsFlipped(true);
  };

  
const checkAchievements = (newXp) => {
    const newAchievements = badgeCriteria.filter(
      (badge) => newXp >= badge.xpRequired && !achievements.includes(badge.name)
    );

    if (newAchievements.length > 0) {
      setAchievements([...achievements, ...newAchievements.map((b) => b.name)]);
      setNewBadge(newAchievements[0].name);
    //   play(); // Play badge unlock sound
      setShowConfetti(true);

      // Stop confetti after 3 seconds
      setTimeout(() => {
        setShowConfetti(false);
      }, 3000);
    }
  };

  const completeQuest = (id, questXp) => {
    setQuests((prevQuests) =>
      prevQuests.map((quest) =>
        quest.id === id ? { ...quest, completed: true } : quest
      )
    );

    setXp((prevXp) => {
      const newXp = prevXp + questXp;
      checkAchievements(newXp);
      if (newXp >= level * 50) {
        setLevel((prevLevel) => prevLevel + 1);
        return newXp - level * 50; // Reset XP after leveling up
      }
      return newXp;
    });
  };

  return (
    <div className="quests-container">
      {showConfetti && <Confetti numberOfPieces={200} />}
      <h2>Daily Quests</h2>
      <div className="progress-bar">
        <div className="progress" style={{ width: `${(xp / (level * 50)) * 100}%` }}></div>
      </div>
      <p>Level: {level} | XP: {xp}/{level * 50}</p>
      <div className="quest-list">
        {quests.map((quest) => (
          <div key={quest.id} className={`quest-card ${quest.completed ? 'completed' : ''}`}>
            <h3>{quest.name}</h3>
            <p>XP: {quest.xp}</p>
            {!quest.completed ? (
              <button className="complete-btn" onClick={() => completeQuest(quest.id, quest.xp)}>
                Complete
              </button>
            ) : (
              <p className="completed-text">✔ Completed</p>
            )}
          </div>
        ))}
      </div>


      {/* Recent Achievements Section */}
      <h3 className="achievements-title">Recent Achievements</h3>
      <div className="achievement-list">
        {achievements.length === 0 ? (
          <p>No achievements unlocked yet.</p>
        ) : (
          achievements.slice(-3).map((badge, index) => (
            <motion.div
              key={index}
              className="achievement-card"
              initial={{ opacity: 0, scale: 0.5 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5 }}
            >
              <FaMedal className="badge-icon" />
              <p>{badge}</p>
            </motion.div>
          ))
        )}
      </div>


      {/* 🎉 New Badge Pop-up Animation */}
      <AnimatePresence>
        {newBadge && (
          <motion.div
            className="badge-popup"
            initial={{ scale: 0, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0, opacity: 0 }}
            transition={{ duration: 0.5, ease: "easeOut" }}
          >
            <div className="badge-popup-content">
              <FaMedal className="popup-badge-icon" />
              <h3>New Achievement Unlocked!</h3>
              <p>{newBadge}</p>
              <button className="close-badge-btn" onClick={() => setNewBadge(null)}>
                <FaTimes /> Close
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>




      {/* Mood Popup */}
{isMoodPopupOpen && (
  <div className="mood-popup">
    <motion.div 
      className={`mood-popup-content ${isFlipped ? "flipped" : ""}`} 
      animate={{ rotateY: isFlipped ? 180 : 0 }} 
      transition={{ duration: 0.6 }}
    >
      {/* Front Side - Mood Selection */}
      {!isFlipped ? (
        <div className="mood-selection">
          <div className="mood-popup-header">
            <h3 className="select-heading">Select Your Mood</h3>
            <FaTimes className="close-btn" onClick={() => setIsMoodPopupOpen(false)} />
          </div>
          <div className="mood-options">
            {moodOptions.map((mood, index) => (
              <button key={index} className="mood-btn" onClick={() => handleMoodSelect(mood)}>
                {mood}
              </button>
            ))}
          </div>
        </div>
      ) : (
        /* Back Side - AI Suggestion */
        <div className="mood-selection">
          <div className="mood-popup-header">
            <h3 className="select-heading-card">💡 Wellness Suggestion 💡</h3>
            <FaTimes className="close-btn-card" onClick={() => setIsMoodPopupOpen(false)} />
          </div>
          <div className="mood-options">
          <p className="suggestion-text">{suggestions[selectedMood] || "Take a mindful break!"}</p>
          </div>
        </div>
        // <div className="suggestion-card">
        //   <h3 className="suggestion-heading">💡 Wellness Suggestion</h3>
        //   <p className="suggestion-text">{suggestions[selectedMood] || "Take a mindful break!"}</p>
        //   <button className="close-btn" onClick={() => setIsMoodPopupOpen(false)}>
        //     Close
        //   </button>
        // </div>
      )}
    </motion.div>
  </div>
)}

    </div>

    
  );
};

export default Quests;
