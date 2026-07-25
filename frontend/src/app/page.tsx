"use client";

import { useEffect, useState } from "react";
import { fetchPerformanceScores } from "@/services/api";
import { PerformanceScore } from "@/types/analytics";

export default function Home() {
  const [drivers, setDrivers] = useState<PerformanceScore[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const data = await fetchPerformanceScores(9462);
        setDrivers(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">
        <h1 className="text-3xl font-bold">
          Loading F1 Telemetry Dashboard...
        </h1>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <div className="max-w-7xl mx-auto px-8 py-10">
        <h1 className="text-5xl font-bold text-red-600">
          F1 Telemetry Intelligence Platform
        </h1>

        <p className="text-zinc-400 mt-2">
          AI-Powered Formula 1 Analytics Dashboard
        </p>

        <div className="mt-12">
          <h2 className="text-3xl font-semibold mb-6">
            Driver Performance Leaderboard
          </h2>

          <div className="overflow-hidden rounded-2xl border border-zinc-800">
            <table className="w-full">
              <thead className="bg-zinc-900">
                <tr>
                  <th className="p-4 text-left">Rank</th>
                  <th className="p-4 text-left">Driver</th>
                  <th className="p-4 text-left">Team</th>
                  <th className="p-4 text-right">Score</th>
                </tr>
              </thead>

              <tbody>
                {drivers.map((driver) => (
                  <tr
                    key={driver.driver_number}
                    className="border-t border-zinc-800 hover:bg-zinc-900 transition"
                  >
                    <td className="p-4">{driver.rank}</td>

                    <td className="p-4 font-medium">
                      {driver.driver_name}
                    </td>

                    <td className="p-4 text-zinc-400">
                      {driver.team_name}
                    </td>

                    <td className="p-4 text-right font-bold text-red-500">
                      {driver.performance_score}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </main>
  );
}