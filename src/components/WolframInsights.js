import { useEffect, useState } from "react";

function WolframInsights() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/recommendation/wolfram-insights")
      .then((response) => response.json())
      .then((result) => setData(result.data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h2>🌿 Wolfram Insights</h2>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading...</p>}
    </div>
  );
}

export default WolframInsights;
