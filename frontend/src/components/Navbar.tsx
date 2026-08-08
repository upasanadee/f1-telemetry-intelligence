"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full border-b border-zinc-800 bg-zinc-950">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-8 py-5">
        {/* Logo / Title */}
        <div>
          <h1 className="text-3xl font-bold text-red-600">
            F1 Telemetry Intelligence
          </h1>

          <p className="text-zinc-400 text-sm">
            AI-Powered Formula 1 Analytics Platform
          </p>
        </div>

        {/* Navigation */}
        <div className="flex gap-8 text-zinc-300 font-medium">
          <Link
            href="/"
            className="hover:text-red-500 transition-colors duration-200"
          >
            Dashboard
          </Link>

          <Link
            href="/drivers"
            className="hover:text-red-500 transition-colors duration-200"
          >
            Drivers
          </Link>

          <Link
            href="/compare"
            className="hover:text-red-500 transition-colors duration-200"
          >
            Compare
          </Link>

          <Link
            href="/race-summary"
            className="hover:text-red-500 transition-colors duration-200"
          >
            Race Summary
          </Link>
        </div>
      </div>
    </nav>
  );
}