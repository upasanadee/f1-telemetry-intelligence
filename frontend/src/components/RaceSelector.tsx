"use client";

import { Meeting } from "@/types/f1";

interface RaceSelectorProps {
  meetings: Meeting[];
  selectedMeeting: number;
  onMeetingChange: (meetingKey: number) => void;
}

export default function RaceSelector({
  meetings,
  selectedMeeting,
  onMeetingChange,
}: RaceSelectorProps) {
  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 mb-8">

      <h2 className="text-xl font-semibold text-white mb-4">
        🏁 Race Selection
      </h2>

      <div className="grid md:grid-cols-2 gap-6">

        {/* Season */}

        <div>
          <label className="block text-zinc-400 mb-2">
            Season
          </label>

          <input
            value="2024"
            disabled
            className="w-full rounded-xl bg-zinc-950 border border-zinc-800 p-3"
          />
        </div>

        {/* Grand Prix */}

        <div>
          <label className="block text-zinc-400 mb-2">
            Grand Prix
          </label>

          <select
            value={selectedMeeting}
            onChange={(e) =>
              onMeetingChange(Number(e.target.value))
            }
            className="w-full rounded-xl bg-zinc-950 border border-zinc-800 p-3"
          >
            {meetings.map((meeting) => (
              <option
                key={meeting.meeting_key}
                value={meeting.meeting_key}
              >
                {meeting.meeting_name}
              </option>
            ))}
          </select>
        </div>

      </div>

    </div>
  );
}