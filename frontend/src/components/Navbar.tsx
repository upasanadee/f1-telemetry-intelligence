export default function Navbar() {
  return (
    <nav className="w-full border-b border-zinc-800 bg-zinc-950">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-8 py-5">
        <div>
          <h1 className="text-3xl font-bold text-red-600">
            F1 Telemetry Intelligence
          </h1>

          <p className="text-zinc-400 text-sm">
            AI-Powered Formula 1 Analytics Platform
          </p>
        </div>

        <div className="flex gap-8 text-zinc-300">
          <button className="hover:text-red-500 transition">
            Dashboard
          </button>

          <button className="hover:text-red-500 transition">
            Drivers
          </button>

          <button className="hover:text-red-500 transition">
            Compare
          </button>

          <button className="hover:text-red-500 transition">
            Race Summary
          </button>
        </div>
      </div>
    </nav>
  );
}