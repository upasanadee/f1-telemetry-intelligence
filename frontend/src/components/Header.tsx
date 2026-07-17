"use client";

export default function Header() {
  return (
    <header className="border-b border-zinc-800">
      <div className="max-w-7xl mx-auto px-8 py-6 flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold">
            F1 Telemetry Intelligence
          </h1>

          <p className="text-zinc-400 mt-2">
            Research-grade AI Analytics Platform
          </p>
        </div>

        <button className="bg-red-600 hover:bg-red-700 transition px-6 py-3 rounded-xl font-semibold">
          Live Telemetry
        </button>
      </div>
    </header>
  );
}