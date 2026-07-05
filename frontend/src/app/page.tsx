"use client";

import { useEffect, useState } from "react";

import TelemetryChart from "../components/TelemetryChart";

export default function Home() {

  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch("/data/f1_dashboard_data.json")
      .then((res) => res.json())
      .then((json) => setData(json));
  }, []);

  if (!data) {
    return (
      <main className="min-h-screen bg-black text-white flex items-center justify-center">
        <h1 className="text-3xl">Loading AI Telemetry...</h1>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-[#09090B] text-white">

      {/* ===================================================== */}
      {/* HEADER */}
      {/* ===================================================== */}

      <header className="border-b border-zinc-800">

        <div className="max-w-7xl mx-auto px-8 py-6 flex items-center justify-between">

          <div>

            <h1 className="text-4xl font-bold">
              F1 Telemetry Intelligence
            </h1>

            <p className="text-zinc-400 mt-1">
              Research-grade AI Analytics Platform
            </p>

          </div>

          <div className="flex gap-4">

            <button className="bg-red-600 hover:bg-red-700 transition px-6 py-3 rounded-xl font-semibold">
              Live Telemetry
            </button>

          </div>

        </div>

      </header>

      {/* ===================================================== */}
      {/* SELECTORS */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10">

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

          <div className="bg-zinc-900 rounded-3xl p-6">

            <h3 className="text-zinc-400 mb-3">
              Grand Prix
            </h3>

            <select className="w-full bg-black rounded-xl p-4">

              <option>Monaco GP</option>

            </select>

          </div>

          <div className="bg-zinc-900 rounded-3xl p-6">

            <h3 className="text-zinc-400 mb-3">
              Driver
            </h3>

            <select className="w-full bg-black rounded-xl p-4">

              <option>Max Verstappen</option>

            </select>

          </div>

          <div className="bg-zinc-900 rounded-3xl p-6">

            <h3 className="text-zinc-400 mb-3">
              Compare With
            </h3>

            <select className="w-full bg-black rounded-xl p-4">

              <option>Lewis Hamilton</option>

            </select>

          </div>

        </div>

      </section>

      {/* ===================================================== */}
      {/* METRICS */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10">

        <div className="grid grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-6">

          <MetricCard
            title="Average Speed"
            value={`${data.avg_speed.toFixed(1)} km/h`}
          />

          <MetricCard
            title="Top Speed"
            value={`${data.top_speed.toFixed(1)} km/h`}
          />

          <MetricCard
            title="Average RPM"
            value={data.avg_rpm.toFixed(0)}
          />

          <MetricCard
            title="Throttle"
            value={`${data.avg_throttle.toFixed(1)} %`}
          />

          <MetricCard
            title="Tire Wear"
            value={`${data.avg_tire_deg.toFixed(1)} %`}
          />

          <MetricCard
            title="Engine Stress"
            value={`${data.avg_engine_stress.toFixed(1)} %`}
          />

        </div>

      </section>

      {/* ===================================================== */}
      {/* EMPTY CHART AREA */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10 mb-16">

      <TelemetryChart
        title="Speed Telemetry"
        distance={data.distance}
        values={data.speed_trace}
        color="#ef4444"
      />

      <TelemetryChart
        title="Throttle Telemetry"
        distance={data.distance}
        values={data.throttle_trace}
        color="#00F5D4"
      />

      <TelemetryChart
        title="Brake Telemetry"
        distance={data.distance}
        values={data.brake_trace}
        color="#FFD60A"
      />

      <TelemetryChart
        title="AI Tire Degradation"
        distance={data.distance}
        values={data.tire_trace}
        color="#FF00FF"
      />

      </section>

    </main>
  );
}

function MetricCard({

  title,

  value,

}: {

  title: string;

  value: string;

}) {

  return (

    <div className="bg-zinc-900 rounded-3xl p-6">

      <p className="text-zinc-400">

        {title}

      </p>

      <h2 className="text-4xl font-bold mt-3">

        {value}

      </h2>

    </div>

  );

}