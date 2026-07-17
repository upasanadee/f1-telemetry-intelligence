"use client";

interface Props {
  driver1: string;
  driver2: string;
}

export default function SelectorPanel({
  driver1,
  driver2,
}: Props) {
  return (
    <section className="max-w-7xl mx-auto px-8 mt-10">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <div className="bg-zinc-900 rounded-3xl p-6">
          <h3 className="text-zinc-400 mb-3">Grand Prix</h3>

          <select className="w-full bg-black rounded-xl p-4">
            <option>Bahrain GP</option>
          </select>
        </div>

        <div className="bg-zinc-900 rounded-3xl p-6">
          <h3 className="text-zinc-400 mb-3">Driver</h3>

          <select className="w-full bg-black rounded-xl p-4">
            <option>{driver1}</option>
          </select>
        </div>

        <div className="bg-zinc-900 rounded-3xl p-6">
          <h3 className="text-zinc-400 mb-3">Compare With</h3>

          <select className="w-full bg-black rounded-xl p-4">
            <option>{driver2}</option>
          </select>
        </div>

      </div>
    </section>
  );
}