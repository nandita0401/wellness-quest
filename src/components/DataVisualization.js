// src/components/DataVisualization.js
import React from 'react';
import './DataVisualization.css';
import CountUp from 'react-countup';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip
);

function DataVisualization() {
  const barData = {
    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
    datasets: [
      {
        label: 'Average Mood (1-10)',
        data: [5, 6, 7, 8],
        backgroundColor: '#ff6e6c',
      },
    ],
  };

  const barOptions = {
    responsive: true,
    scales: {
      y: {
        min: 0,
        max: 10,
      },
    },
  };

  return (
    <section className="data-visual" id="data" data-aos="fade-up">
      <h2>Our Impact</h2>

      {/* Animated Counters */}
      <div className="counters">
        <div className="counter-box">
          <h3>Users</h3>
          <CountUp end={4500} duration={2} />
        </div>
        <div className="counter-box">
          <h3>Total Quests</h3>
          <CountUp end={12340} duration={2.5} />
        </div>
      </div>

      {/* Chart */}
      <div className="chart-container">
        <h3>User Mood Improvement Over Time</h3>
        <Bar data={barData} options={barOptions} />
      </div>
    </section>
  );
}

export default DataVisualization;
