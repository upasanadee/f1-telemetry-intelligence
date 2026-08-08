"use client";

import { useEffect, useState } from "react";

import Navbar from "@/components/Navbar";
import { useSession } from "@/context/SessionContext";

import {
  fetchDrivers,
  fetchPerformanceScores,
} from "@/services/api";

import { Driver } from "@/types/f1";
import { PerformanceScore } from "@/types/analytics";

export default function DriversPage() {
  const { selectedSession } = useSession();

  const [drivers, setDrivers] = useState<Driver[]>([]);
  const [scores, setScores] = useState<PerformanceScore[]>([]);

  useEffect(() => {
    if (!selectedSession) return;

    async function loadData() {
      try {
        const [driverData, scoreData] = await Promise.all([
          fetchDrivers(selectedSession),
          fetchPerformanceScores(selectedSession),
        ]);

        setDrivers(driverData);
        setScores(scoreData);
      } catch (err) {
        console.error(err);
      }
    }

    loadData();
  }, [selectedSession]);

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <Navbar />

      <div className="max-w-7xl mx-auto px-8 py-10">
        <h1 className="text-4xl font-bold">
          Drivers
        </h1>

        <p className="text-zinc-400 mt-2">
          Driver information and AI performance analysis.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 mt-10">
          {drivers.map((driver) => {
            const score = scores.find(
              (d) => d.driver_number === driver.driver_number
            );

            return (
              <div
                key={driver.driver_number}
                className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6 hover:border-red-500 transition"
              >
                <div className="flex items-center justify-between">
                  <div>
                    <h2 className="text-2xl font-bold">
                      {driver.name_acronym}
                    </h2>

                    <p className="text-zinc-300">
                      {driver.full_name}
                    </p>
                  </div>

                  <div
                    className="w-5 h-12 rounded"
                    style={{
                      backgroundColor: `#${driver.team_colour}`,
                    }}
                  />
                </div>

                <div className="mt-5">
                  <p className="text-zinc-400">
                    Team
                  </p>

                  <p className="font-medium">
                    {driver.team_name}
                  </p>
                </div>

                <div className="mt-5">
                  <p className="text-zinc-400">
                    AI Performance Index
                  </p>

                  <p className="text-3xl font-bold text-red-500">
                    {score
                      ? score.performance_score.toFixed(2)
                      : "--"}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </main>
  );
}