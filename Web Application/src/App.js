import React, { useState, useEffect } from "react";
import axios from "axios";
import { LineChart } from "@mui/x-charts";

function App() {
  const [xValues, setXValues] = useState([]);
  const [yValues, setYValues] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/")
      .then((response) => {
        setXValues(response.data["Next7Days"]);
        setYValues(response.data["Forecasts"]);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <LineChart
        xAxis={[{ scaleType: "point", data: xValues }]}
        series={[
          {
            data: yValues,
          },
        ]}
        width={500}
        height={300}
        grid={{ vertical: true, horizontal: true }}
      />
    </div>
  );
}

export default App;
