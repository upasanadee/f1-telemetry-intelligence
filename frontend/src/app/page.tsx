"use client";

import { useEffect, useState } from "react";

import AIInsights from "../components/AIInsights";
import MetricCard from "../components/MetricCard";
import TelemetryChart from "../components/TelemetryChart";

export default function Home() {
  const [data, setData] = useState<any>(null);
  const [activeChart, setActiveChart] = useState("speed");

  useEffect(() => {
    async function loadTelemetry() {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/api/telemetry"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch telemetry");
        }

        const json = await response.json();
        setData(json);
      } catch (error) {
        console.error(error);
      }
    }

    loadTelemetry();
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

          <button className="bg-red-600 hover:bg-red-700 transition px-6 py-3 rounded-xl font-semibold">
            Live Telemetry
          </button>
        </div>
      </header>

      {/* ===================================================== */}
      {/* SELECTORS */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-zinc-900 rounded-3xl p-6">
            <h3 className="text-zinc-400 mb-3">Grand Prix</h3>

            <select className="w-full bg-black rounded-xl p-4">
              <option>Monaco GP</option>
            </select>
          </div>

          <div className="bg-zinc-900 rounded-3xl p-6">
            <h3 className="text-zinc-400 mb-3">Driver</h3>

            <select className="w-full bg-black rounded-xl p-4">
              <option>{data.driver1}</option>
            </select>
          </div>

          <div className="bg-zinc-900 rounded-3xl p-6">
            <h3 className="text-zinc-400 mb-3">Compare With</h3>

            <select className="w-full bg-black rounded-xl p-4">
              <option>{data.driver2}</option>
            </select>
          </div>
        </div>
      </section>

      {/* ===================================================== */}
      {/* METRIC CARDS */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10">
        <div className="grid grid-cols-2 lg:grid-cols-4 xl:grid-cols-6 gap-6">
          <MetricCard
            title="Average Speed"
            value={data.avg_speed}
            unit="km/h"
            color="#ef4444"
          />

          <MetricCard
            title="Top Speed"
            value={data.top_speed}
            unit="km/h"
            color="#3b82f6"
          />

          <MetricCard
            title="Average RPM"
            value={data.avg_rpm}
            unit="RPM"
            color="#22c55e"
          />

          <MetricCard
            title="Throttle"
            value={data.avg_throttle}
            unit="%"
            color="#facc15"
          />

          <MetricCard
            title="Tire Wear"
            value={data.avg_tire_deg}
            unit="%"
            color="#a855f7"
          />

          <MetricCard
            title="Engine Stress"
            value={data.avg_engine_stress}
            unit="%"
            color="#f97316"
          />
        </div>
      </section>

      {/* ===================================================== */}
      {/* AI INSIGHTS */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10">
        <AIInsights insights={data.insights} />
      </section>

      {/* ===================================================== */}
      {/* TELEMETRY TABS */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-10">
        <div className="flex flex-wrap gap-3 mb-6">
          {[
            { id: "speed", label: "Speed" },
            { id: "throttle", label: "Throttle" },
            { id: "brake", label: "Brake" },
            { id: "tyre", label: "Tyre" },
          ].map((chart) => (
            <button
              key={chart.id}
              onClick={() => setActiveChart(chart.id)}
              className={`px-5 py-2 rounded-xl transition font-medium ${
                activeChart === chart.id
                  ? "bg-red-600 text-white"
                  : "bg-zinc-800 text-zinc-300 hover:bg-zinc-700"
              }`}
            >
              {chart.label}
            </button>
          ))}
        </div>
      </section>

      {/* ===================================================== */}
      {/* SELECTED TELEMETRY CHART */}
      {/* ===================================================== */}

      <section className="max-w-7xl mx-auto px-8 mt-4 mb-16">
        {activeChart === "speed" && (
          <TelemetryChart
            title="Speed Telemetry"
            distance={data.distance}
            values={data.speed_trace}
            color="#ef4444"
          />
        )}

        {activeChart === "throttle" && (
          <TelemetryChart
            title="Throttle Telemetry"
            distance={data.distance}
            values={data.throttle_trace}
            color="#00F5D4"
          />
        )}

        {activeChart === "brake" && (
          <TelemetryChart
            title="Brake Telemetry"
            distance={data.distance}
            values={data.brake_trace}
            color="#FFD60A"
          />
        )}

        {activeChart === "tyre" && (
          <TelemetryChart
            title="AI Tire Degradation"
            distance={data.distance}
            values={data.tire_trace}
            color="#FF00FF"
          />
        )}
      </section>
    </main>
  );
}