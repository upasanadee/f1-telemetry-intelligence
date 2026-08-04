interface StatCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
}

export default function StatCard({
  title,
  value,
  subtitle,
}: StatCardProps) {
  return (
    <div className="rounded-2xl border border-zinc-800 bg-zinc-900 p-6 shadow-lg">
      <p className="text-sm text-zinc-400">{title}</p>

      <h2 className="mt-3 text-4xl font-bold text-white">
        {value}
      </h2>

      {subtitle && (
        <p className="mt-2 text-zinc-500">
          {subtitle}
        </p>
      )}
    </div>
  );
}