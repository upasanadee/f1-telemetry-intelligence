"use client";

import {
  LineChart,
  Line,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
} from "recharts";

interface Props {
  title: string;
  distance: number[];
  values: number[];
  color: string;
}

export default function TelemetryChart({
  title,
  distance,
  values,
  color,
}: Props) {
  const chartData = distance.map((d, i) => ({
    distance: d,
    value: values[i],
  }));

  return (
    <div className="bg-zinc-900 rounded-3xl p-8 border border-zinc-800 shadow-lg">
      <h2 className="text-3xl font-bold mb-6">{title}</h2>

      <div className="h-[380px]">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            data={chartData}
            margin={{
              top: 10,
              right: 20,
              left: 0,
              bottom: 10,
            }}
          >
            <CartesianGrid
              stroke="#2b2b2b"
              strokeDasharray="3 3"
            />

            <XAxis
              dataKey="distance"
              stroke="#9CA3AF"
              tick={{ fontSize: 12 }}
              tickFormatter={(value) => `${Math.round(Number(value))} m`}
            />

            <YAxis
              stroke="#9CA3AF"
              tick={{ fontSize: 12 }}
              tickFormatter={(value) => Number(value).toFixed(0)}
            />

            <Tooltip
              contentStyle={{
                backgroundColor: "#18181B",
                border: "1px solid #3F3F46",
                borderRadius: "12px",
                color: "#ffffff",
              }}
              formatter={(value) => {
                const numericValue = Number(value);

                return [
                  Number.isNaN(numericValue)
                    ? String(value)
                    : numericValue.toFixed(2),
                  title,
                ];
              }}
              labelFormatter={(label) =>
                `Distance: ${Math.round(Number(label))} m`
              }
            />

            <Legend />

            <Line
              type="monotone"
              dataKey="value"
              name={title}
              stroke={color}
              strokeWidth={3}
              dot={false}
              activeDot={{ r: 5 }}
              isAnimationActive
              animationDuration={700}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}