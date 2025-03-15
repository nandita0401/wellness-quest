// src/components/AboutTeam.js
import React from 'react';
import './AboutTeam.css';

function AboutTeam() {
  const teamMembers = [
    {
      name: 'Alice',
      role: 'Frontend Engineer',
    },
    {
      name: 'Bob',
      role: 'Backend Engineer',
    },
    {
      name: 'Charlie',
      role: 'UX/UI Designer',
    }
  ];

  return (
    <section className="about-team" id="team" data-aos="fade-up">
      <h2>Meet the Team</h2>
      <div className="team-container">
        {teamMembers.map((member, index) => (
          <div className="team-member" key={index}>
            {/* Insert <img> for photo if you want */}
            <h3>{member.name}</h3>
            <p>{member.role}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default AboutTeam;
