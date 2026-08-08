"use client";

import Navbar from "@/components/Navbar";

export default function ComparePage() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <Navbar />

      <div className="max-w-7xl mx-auto px-8 py-10">
        <h1 className="text-4xl font-bold">
          Driver Comparison
        </h1>

        <p className="text-zinc-400 mt-2">
          Compare telemetry, AI Performance Index, lap pace, speed,
          throttle, braking and DRS usage between two drivers.
        </p>

        <div className="mt-10 rounded-2xl border border-zinc-800 bg-zinc-900 p-8">
          <p className="text-zinc-400">
            🚧 Driver comparison coming next...
          </p>
        </div>
      </div>
    </main>
  );
}