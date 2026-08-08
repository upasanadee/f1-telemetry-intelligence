import { PerformanceScore } from "@/types/analytics";
import ProgressBar from "./ProgressBar";

interface LeaderboardProps {
  drivers: PerformanceScore[];
}

function teamColor(team: string) {
  if (team.includes("Red Bull")) return "bg-blue-500";
  if (team.includes("Ferrari")) return "bg-red-600";
  if (team.includes("Mercedes")) return "bg-emerald-400";
  if (team.includes("McLaren")) return "bg-orange-500";
  if (team.includes("Aston")) return "bg-green-600";
  if (team.includes("Williams")) return "bg-cyan-400";
  if (team.includes("Alpine")) return "bg-pink-500";
  if (team.includes("RB")) return "bg-indigo-500";
  if (team.includes("Sauber")) return "bg-lime-500";

  return "bg-zinc-400";
}

function getBarColor(score: number) {
  if (score >= 85) return "#22c55e"; // Green
  if (score >= 70) return "#3b82f6"; // Blue
  if (score >= 55) return "#facc15"; // Yellow
  return "#ef4444"; // Red
}

function getTextColor(score: number) {
  if (score >= 85) return "text-green-500";
  if (score >= 70) return "text-blue-500";
  if (score >= 55) return "text-yellow-400";
  return "text-red-500";
}

export default function Leaderboard({
  drivers,
}: LeaderboardProps) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 overflow-hidden shadow-xl">

      {/* Header */}
      <div className="px-6 py-5 border-b border-zinc-800">
        <h2 className="text-2xl font-bold text-white">
          AI Performance Index
        </h2>

        <p className="text-sm text-zinc-400 mt-1">
          Computed from lap pace, speed, throttle, braking and DRS telemetry.
        </p>
      </div>

      {/* Table */}
      <table className="w-full">
        <thead className="bg-zinc-950">
          <tr>
            <th className="p-4 text-left">Rank</th>
            <th className="p-4 text-left">Driver</th>
            <th className="p-4 text-left">Team</th>
            <th className="p-4 text-right">Performance Index</th>
          </tr>
        </thead>

        <tbody>
          {drivers.map((driver) => (
            <tr
              key={driver.driver_number}
              className="border-t border-zinc-800 hover:bg-zinc-800 hover:scale-[1.01] transition-all duration-300"
            >
              {/* Rank */}
              <td className="p-4 font-semibold text-lg">
                {driver.rank === 1 && "🥇"}
                {driver.rank === 2 && "🥈"}
                {driver.rank === 3 && "🥉"}
                {driver.rank > 3 && driver.rank}
              </td>

              {/* Driver */}
              <td className="p-4 font-medium text-white">
                {driver.driver_name}
              </td>

              {/* Team */}
              <td className="p-4">
                <div className="flex items-center gap-3">
                  <div
                    className={`w-2 h-8 rounded-full ${teamColor(
                      driver.team_name
                    )}`}
                  />
                  <span className="text-zinc-300">
                    {driver.team_name}
                  </span>
                </div>
              </td>

              {/* Score */}
              <td className="p-4">
                <div className="flex items-center justify-end gap-4">

                  <div className="w-40">
                    <ProgressBar
                      value={driver.performance_score}
                      color={getBarColor(driver.performance_score)}
                    />
                  </div>

                  <span
                    className={`font-bold text-lg ${getTextColor(
                      driver.performance_score
                    )}`}
                  >
                    {driver.performance_score.toFixed(2)}
                  </span>

                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}