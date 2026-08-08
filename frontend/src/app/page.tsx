"use client";

import { useEffect, useState } from "react";

import Navbar from "@/components/Navbar";
import RaceSelector from "@/components/RaceSelector";
import StatCard from "@/components/StatCard";
import Leaderboard from "@/components/Leaderboard";
import RaceSummaryCard from "@/components/RaceSummaryCard";

import {
  fetchMeetings,
  fetchSessions,
  fetchPerformanceScores,
  fetchRaceSummary,
} from "@/services/api";

import { Meeting, Session } from "@/types/f1";
import { PerformanceScore } from "@/types/analytics";

export default function Home() {
  // ===========================================
  // Dashboard Data
  // ===========================================

  const [drivers, setDrivers] = useState<PerformanceScore[]>([]);
  const [summary, setSummary] = useState<any>(null);

  // ===========================================
  // Race Selection Data
  // ===========================================

  const [meetings, setMeetings] = useState<Meeting[]>([]);
  const [sessions, setSessions] = useState<Session[]>([]);

  // Default Bahrain GP
  const [selectedMeeting, setSelectedMeeting] = useState<number>(1229);

  // Default Bahrain Race
  const [selectedSession, setSelectedSession] = useState<number>(9472);

  const [loading, setLoading] = useState(true);

  // ===========================================
  // Load meetings & sessions
  // ===========================================

  useEffect(() => {
    async function loadInitialData() {
      try {
        const [meetingsData, sessionsData] = await Promise.all([
          fetchMeetings(),
          fetchSessions(),
        ]);

        setMeetings(meetingsData);
        setSessions(sessionsData);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadInitialData();
  }, []);

  // ===========================================
  // Auto-select Race session whenever GP changes
  // ===========================================

  useEffect(() => {
    if (sessions.length === 0) return;

    const meetingSessions = sessions.filter(
      (session) => session.meeting_key === selectedMeeting
    );

    const raceSession =
      meetingSessions.find(
        (session) => session.session_type === "Race"
      ) ?? meetingSessions[0];

    if (raceSession) {
      setSelectedSession(raceSession.session_key);
    }
  }, [selectedMeeting, sessions]);

  // ===========================================
  // Load analytics whenever session changes
  // ===========================================

  useEffect(() => {
    if (!selectedSession) return;

    async function loadAnalytics() {
      try {
        const [leaderboard, raceSummary] =
          await Promise.all([
            fetchPerformanceScores(selectedSession),
            fetchRaceSummary(selectedSession),
          ]);

        setDrivers(leaderboard);
        setSummary(raceSummary);
      } catch (error) {
        console.error(error);
      }
    }

    loadAnalytics();
  }, [selectedSession]);

  // ===========================================
  // Loading Screen
  // ===========================================

  if (loading || !summary) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-zinc-950 text-white">
        <h1 className="text-3xl font-bold">
          Loading Dashboard...
        </h1>
      </main>
    );
  }

  // ===========================================
  // UI
  // ===========================================

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <Navbar />

      <div className="max-w-7xl mx-auto px-8 py-10">
        <RaceSelector
          meetings={meetings}
          sessions={sessions}
          selectedMeeting={selectedMeeting}
          selectedSession={selectedSession}
          onMeetingChange={setSelectedMeeting}
          onSessionChange={setSelectedSession}
        />

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-5 gap-6 mt-8">
          <StatCard
            title="Fastest Lap"
            value={`${summary.fastest_lap}s`}
            subtitle={summary.fastest_lap_driver}
          />

          <StatCard
            title="Highest Speed"
            value={`${summary.highest_top_speed} km/h`}
            subtitle={summary.highest_top_speed_driver}
          />

          <StatCard
            title="Track Temperature"
            value={`${summary.average_track_temperature}°C`}
            subtitle="Average"
          />
          <StatCard
            title="Predicted Lap Time"
            value={
              summary.predicted_lap_time !== null &&
              summary.predicted_lap_time !== undefined
                ? `${summary.predicted_lap_time.toFixed(3)} s`
                : "--"
            }
            subtitle="AI Prediction"
          />

          <StatCard
            title="Safety Cars"
            value={summary.safety_car_events}
            subtitle="Race Control"
          />
        </div>

        <div className="mt-10">
          <Leaderboard drivers={drivers} />
        </div>

        <div className="mt-10">
          <RaceSummaryCard
            fastestLap={summary.fastest_lap}
            fastestDriver={summary.fastest_lap_driver}
            topSpeed={summary.highest_top_speed}
            topSpeedDriver={summary.highest_top_speed_driver}
            trackTemp={summary.average_track_temperature}
            yellowFlags={summary.yellow_flags}
          />
        </div>
      </div>
    </main>
  );
}