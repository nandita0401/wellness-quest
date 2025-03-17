// src/components/Dashboard.js
import React from "react";
import "./Dashboard.css";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend } from "chart.js";
import { FaQuoteLeft, FaTimes } from "react-icons/fa";

// Register required Chart.js components
ChartJS.register(BarElement, CategoryScale, LinearScale, Title, Tooltip, Legend);

const Dashboard = ({ isMoodPopupOpen, setIsMoodPopupOpen }) => {
  // Chart Options (Ensures rounded edges & elegant styling)
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
    },
    scales: {
      x: { grid: { display: false } },
      y: { grid: { drawBorder: false, color: "#e0e0e0" } },
    },
    elements: {
      bar: {
        borderRadius: 8, // Rounded bars
      },
    },
  };

  // Mood Trends Data
  const moodTrendsData = {
    labels: ["Happy", "Neutral", "Sad", "Angry", "Anxious"],
    datasets: [{ label: "Mood Trends", data: [30, 20, 10, 5, 15], backgroundColor: "#ff6e6c" }],
  };

  const userMoodData = {
    labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    datasets: [{ label: "Your Mood Trend", data: [3, 4, 2, 5, 4], backgroundColor: "#ff6e6c" }],
  };

  // Motivational Quotes
  const quotes = ["Keep going, you're doing great!", "Every day is a new beginning.", "Your mental health matters.", "Be kind to yourself."];
  const firstQuote = quotes[Math.floor(Math.random() * quotes.length)];
  const secondQuote = quotes[Math.floor(Math.random() * quotes.length)];

  // Mood Options
  const moodOptions = [
    "Anxiety/Stress", "Sadness/Despair", "Happiness/Joy",
    "Disappointment/Regret", "Shame/Guilt", "Pride/Confidence",
    "Comparison/Social Pressure", "Empathy/Compassion", "Anger/Resentment",
    "Curiosity/Awe", "Belonging/Connection", "Nostalgia/Irony",
    "Love/Trust"
  ];

  return (
    <div className="dashboard-container">
      <h1>Welcome Back!</h1>

      {/* Motivational Quote Above Charts */}
      <div className="quote-box">
        <FaQuoteLeft className="quote-icon" />
        <p>{firstQuote}</p>
      </div>

      {/* Mood Trends Charts */}
      <div className="charts-container">
        <div className="chart-box">
          <h3>All Users' Mood Trends</h3>
          <div className="chart-wrapper">
            <Bar data={moodTrendsData} options={chartOptions} />
          </div>
        </div>

        <div className="chart-box">
          <h3>Your Mood Trends</h3>
          <div className="chart-wrapper">
            <Bar data={userMoodData} options={chartOptions} />
          </div>
        </div>
      </div>

      {/* Motivational Quote Below Charts */}
      <div className="quote-box">
        <FaQuoteLeft className="quote-icon" />
        <p>{secondQuote}</p>
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

export default Dashboard;
