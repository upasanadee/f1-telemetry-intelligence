"use client";

import {
  LineChart,
  Line,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
  CartesianGrid,
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
    <div className="bg-zinc-900 rounded-3xl p-8 mt-8">

      <h2 className="text-3xl font-bold mb-6">

        {title}

      </h2>

      <div className="h-[420px]">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={chartData}>

            <CartesianGrid stroke="#333" />

            <XAxis
              dataKey="distance"
              stroke="#777"
            />

            <YAxis stroke="#777" />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="value"
              stroke={color}
              strokeWidth={3}
              dot={false}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}