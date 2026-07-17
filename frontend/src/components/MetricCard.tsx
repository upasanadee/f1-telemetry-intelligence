"use client";

import CountUp from "react-countup";
import { motion } from "framer-motion";

interface MetricCardProps {
  title: string;
  value: number;
  unit?: string;
  color?: string;
}

export default function MetricCard({
  title,
  value,
  unit = "",
  color = "#ffffff",
}: MetricCardProps) {
  return (
    <motion.div
      whileHover={{ scale: 1.03 }}
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className="bg-zinc-900 rounded-2xl p-6 shadow-lg border border-zinc-800"
    >
      <p className="text-sm text-zinc-400">{title}</p>

      <h2
        className="text-4xl font-bold mt-3"
        style={{ color }}
      >
        <CountUp
          end={value}
          decimals={1}
          duration={1.5}
        />
        <span className="text-lg ml-1">{unit}</span>
      </h2>
    </motion.div>
  );
}