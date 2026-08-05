"use client";

import { useEffect, useState } from "react";

interface ProgressBarProps {
  value: number;
  color: string;
}

export default function ProgressBar({
  value,
  color,
}: ProgressBarProps) {

  const [width, setWidth] = useState(0);

  useEffect(() => {
    setTimeout(() => {
      setWidth(value);
    }, 150);
  }, [value]);

  return (
    <div className="w-36 h-3 rounded-full bg-zinc-800 overflow-hidden">

      <div
        className={`h-full rounded-full ${color} transition-all duration-1000`}
        style={{ width: `${width}%` }}
      />

    </div>
  );
}