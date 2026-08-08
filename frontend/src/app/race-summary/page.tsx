"use client";

import Navbar from "@/components/Navbar";

export default function RaceSummaryPage() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <Navbar />

      <div className="max-w-7xl mx-auto px-8 py-10">
        <h1 className="text-4xl font-bold">
          Race Summary
        </h1>

        <p className="text-zinc-400 mt-2">
          Session overview, weather, race statistics,
          telemetry insights and AI lap time prediction.
        </p>

        <div className="mt-10 rounded-2xl border border-zinc-800 bg-zinc-900 p-8">
          <p className="text-zinc-400">
            🚧 Race summary coming next...
          </p>
        </div>
      </div>
    </main>
  );
}