"use client";

import { useEffect, useState } from "react";

import Navbar from "@/components/Navbar";
import StatCard from "@/components/StatCard";
import Leaderboard from "@/components/Leaderboard";
import RaceSummaryCard from "@/components/RaceSummaryCard";

import {
  fetchPerformanceScores,
  fetchRaceSummary,
} from "@/services/api";

import { PerformanceScore } from "@/types/analytics";

export default function Home() {
  const [drivers, setDrivers] = useState<PerformanceScore[]>([]);
  const [summary, setSummary] = useState<any>(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      try {
        const [leaderboard, raceSummary] = await Promise.all([
          fetchPerformanceScores(9462),
          fetchRaceSummary(9462),
        ]);

        setDrivers(leaderboard);
        setSummary(raceSummary);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">
        <h1 className="text-3xl font-bold">
          Loading Dashboard...
        </h1>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-zinc-950 text-white">

      <Navbar />

      <div className="max-w-7xl mx-auto px-8 py-10">

        {/* ============================================ */}
        {/* KPI CARDS */}
        {/* ============================================ */}

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

          <StatCard
            title="Fastest Lap"
            value={`${summary.fastest_lap}s`}
            subtitle={summary.fastest_lap_driver}
          />

          <StatCard
            title="Highest Speed"
            value={`${summary.highest_top_speed} km/h`}
            subtitle={summary.highest_top_speed_driver}
          />

          <StatCard
            title="Track Temperature"
            value={`${summary.average_track_temperature}°C`}
            subtitle="Average"
          />

          <StatCard
            title="Safety Cars"
            value={summary.safety_car_events}
            subtitle="Race Control"
          />

        </div>

        {/* ============================================ */}
        {/* LEADERBOARD */}
        {/* ============================================ */}

        <div className="mt-10">
          <Leaderboard drivers={drivers} />
        </div>

        {/* ============================================ */}
        {/* RACE SUMMARY */}
        {/* ============================================ */}

        <div className="mt-10">

          <RaceSummaryCard
            fastestLap={summary.fastest_lap}
            fastestDriver={summary.fastest_lap_driver}
            topSpeed={summary.highest_top_speed}
            topSpeedDriver={summary.highest_top_speed_driver}
            trackTemp={summary.average_track_temperature}
            yellowFlags={summary.yellow_flags}
          />

        </div>

      </div>

    </main>
  );
}