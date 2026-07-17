"use client";

import { Brain, Gauge, Fuel, BatteryCharging } from "lucide-react";
import { motion } from "framer-motion";

interface Props {
  insights: string[];
}

const icons = [
  Gauge,
  Brain,
  Fuel,
  BatteryCharging,
];

const colors = [
  "text-purple-400",
  "text-green-400",
  "text-yellow-400",
  "text-blue-400",
];

export default function AIInsights({ insights }: Props) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="bg-zinc-900 rounded-3xl p-8 border border-zinc-800"
    >
      <div className="flex items-center gap-3 mb-8">
        <Brain size={30} className="text-red-500" />

        <h2 className="text-3xl font-bold">
          AI Race Engineer
        </h2>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        {insights.map((insight, i) => {
          const Icon = icons[i % icons.length];

          return (
            <motion.div
              key={i}
              whileHover={{ scale: 1.02 }}
              className="bg-zinc-800 rounded-2xl p-6 border border-zinc-700"
            >
              <div className="flex items-center gap-3 mb-4">
                <Icon
                  size={28}
                  className={colors[i % colors.length]}
                />

                <h3 className="font-semibold text-lg">
                  Insight {i + 1}
                </h3>
              </div>

              <p className="text-zinc-300 leading-7">
                {insight}
              </p>

              <div className="mt-5 text-green-400 text-sm font-semibold">
                Confidence: {95 - i}%
              </div>
            </motion.div>
          );
        })}
      </div>
    </motion.div>
  );
}