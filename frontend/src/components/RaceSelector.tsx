"use client";

import { Meeting, Session } from "@/types/f1";

interface RaceSelectorProps {
  meetings: Meeting[];
  sessions: Session[];

  selectedMeeting: number;
  selectedSession: number;

  onMeetingChange: (meeting: number) => void;
  onSessionChange: (session: number) => void;
}

export default function RaceSelector({
  meetings,
  sessions,
  selectedMeeting,
  selectedSession,
  onMeetingChange,
  onSessionChange,
}: RaceSelectorProps) {

  const meetingSessions = sessions.filter(
    (session) => session.meeting_key === selectedMeeting
  );

  return (
    <div className="flex gap-6 mb-8">

      {/* Grand Prix */}

      <div>
        <label className="block text-sm mb-2 text-zinc-400">
          Grand Prix
        </label>

        <select
          value={selectedMeeting}
          onChange={(e) =>
            onMeetingChange(Number(e.target.value))
          }
          className="bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2"
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

      {/* Session */}

      <div>
        <label className="block text-sm mb-2 text-zinc-400">
          Session
        </label>

        <select
          value={selectedSession}
          onChange={(e) =>
            onSessionChange(Number(e.target.value))
          }
          className="bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2"
        >
          {meetingSessions.map((session) => (
            <option
              key={session.session_key}
              value={session.session_key}
            >
              {session.session_name}
            </option>
          ))}
        </select>
      </div>

    </div>
  );
}