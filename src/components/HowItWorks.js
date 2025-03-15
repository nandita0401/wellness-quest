// src/components/HowItWorks.js
import React from 'react';
import './HowItWorks.css';

function HowItWorks() {
  const steps = [
    {
      title: 'Sign Up',
      text: 'Create your account and customize your profile.'
    },
    {
      title: 'Log Your Mood',
      text: 'Record your daily mood and small wins each day.'
    },
    {
      title: 'Get AI Quests',
      text: 'Receive curated tasks for workouts, mindfulness, or mental health.'
    },
    {
      title: 'Earn XP & Level Up',
      text: 'Unlock achievements and watch your wellness improve!'
    }
  ];

  return (
    <section className="how-it-works" id="howitworks" data-aos="fade-up">
      <h2>How It Works</h2>
      <div className="steps-container">
        {steps.map((step, idx) => (
          <div className="step" key={idx}>
            <div className="step-number">{idx + 1}</div>
            <h3>{step.title}</h3>
            <p>{step.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default HowItWorks;
