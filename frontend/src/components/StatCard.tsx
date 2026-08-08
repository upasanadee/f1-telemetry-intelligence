"use client";

import CountUp from "react-countup";

interface StatCardProps {
  title: string;
  value: string | number;
  subtitle: string;
}

export default function StatCard({
  title,
  value,
  subtitle,
}: StatCardProps) {

  const numeric = Number(
    String(value).replace(/[^\d.]/g, "")
  );

  const suffix =
    String(value).replace(/[0-9.]/g, "");

  return (
    <div className="rounded-2xl bg-zinc-900 border border-zinc-800 p-7 hover:border-red-500 transition-all duration-300">

      <p className="text-zinc-400 text-lg">
        {title}
      </p>

      <h2 className="text-4xl font-bold mt-4 text-white">

        <CountUp
          end={numeric}
          duration={1.8}
          decimals={String(numeric).includes(".") ? 3 : 0}
        />

        {suffix}

      </h2>

      <p className="mt-4 text-zinc-500">
        {subtitle}
      </p>

    </div>
  );
}