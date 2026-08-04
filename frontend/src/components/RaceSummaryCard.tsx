interface RaceSummaryProps {
  fastestLap: number;
  fastestDriver: string;
  topSpeed: number;
  topSpeedDriver: string;
  trackTemp: number;
  yellowFlags: number;
}

export default function RaceSummaryCard({
  fastestLap,
  fastestDriver,
  topSpeed,
  topSpeedDriver,
  trackTemp,
  yellowFlags,
}: RaceSummaryProps) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6">
      <h2 className="text-2xl font-bold mb-6">
        Race Summary
      </h2>

      <div className="space-y-4">

        <div className="flex justify-between">
          <span className="text-zinc-400">
            Fastest Lap
          </span>

          <span>
            {fastestDriver} ({fastestLap}s)
          </span>
        </div>

        <div className="flex justify-between">
          <span className="text-zinc-400">
            Highest Speed
          </span>

          <span>
            {topSpeedDriver} ({topSpeed} km/h)
          </span>
        </div>

        <div className="flex justify-between">
          <span className="text-zinc-400">
            Track Temperature
          </span>

          <span>{trackTemp}°C</span>
        </div>

        <div className="flex justify-between">
          <span className="text-zinc-400">
            Yellow Flags
          </span>

          <span>{yellowFlags}</span>
        </div>

      </div>
    </div>
  );
}