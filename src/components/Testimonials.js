// src/components/Testimonials.js
import React from 'react';
import './Testimonials.css';

function Testimonials() {
  return (
    <section className="testimonials" data-aos="fade-up">
      <h2>What People Are Saying</h2>
      <div className="testimonials-wrap">
        <div className="testimonial">
          <p>
            "I overcame my stress by using daily quests in Wellness Quest. 
            It turned my mundane routines into a fun challenge!"
          </p>
          <h4>- Jane D.</h4>
        </div>
        <div className="testimonial">
          <p>
            "Tracking my mood daily and seeing progress on the leaderboard 
            really kept me motivated."
          </p>
          <h4>- Mark S.</h4>
        </div>
      </div>
    </section>
  );
}

export default Testimonials;
