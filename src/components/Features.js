// src/components/Features.js
import React from 'react';
import './Features.css';
import { FaSmile, FaRunning, FaBrain, FaLightbulb } from 'react-icons/fa';

function Features() {
  const featureData = [
    {
      icon: <FaSmile size={40} />,
      title: 'Daily Mood Logging',
      text: 'Track how you feel each day with simple check-ins.'
    },
    {
      icon: <FaRunning size={40} />,
      title: 'Quest-based Workouts',
      text: 'Gamify your fitness with daily challenges.'
    },
    {
      icon: <FaBrain size={40} />,
      title: 'Mindfulness Exercises',
      text: 'Guided meditations and exercises to stay centered.'
    },
    {
      icon: <FaLightbulb size={40} />,
      title: 'AI Recommendation Engine',
      text: 'Personalized suggestions to boost mood & progress.'
    }
  ];

  return (
    <section className="features" id="features" data-aos="fade-up">
      <h2>Features</h2>
      <div className="features-grid">
        {featureData.map((feature, idx) => (
          <div className="feature-card" key={idx}>
            <div className="feature-icon">{feature.icon}</div>
            <h3>{feature.title}</h3>
            <p>{feature.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Features;
