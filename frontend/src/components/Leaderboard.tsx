import { PerformanceScore } from "@/types/analytics";

interface LeaderboardProps {
  drivers: PerformanceScore[];
}

export default function Leaderboard({
  drivers,
}: LeaderboardProps) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 overflow-hidden">
      <div className="px-6 py-5 border-b border-zinc-800">
        <h2 className="text-2xl font-bold text-white">
          Driver Performance Leaderboard
        </h2>
      </div>

      <table className="w-full">
        <thead className="bg-zinc-950">
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
              className="border-t border-zinc-800 hover:bg-zinc-800 transition"
            >
              <td className="p-4 font-semibold">
                {driver.rank === 1 && "🥇"}
                {driver.rank === 2 && "🥈"}
                {driver.rank === 3 && "🥉"}
                {driver.rank > 3 && driver.rank}
              </td>

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
  );
}