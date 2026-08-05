const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

console.log("API URL:", API_BASE_URL);

// ===========================================
// Performance Score
// ===========================================

export async function fetchPerformanceScores(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/performance-score/${sessionKey}`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch performance scores");
  }

  return response.json();
}

// ===========================================
// Race Summary
// ===========================================

export async function fetchRaceSummary(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/race-summary/${sessionKey}`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch race summary");
  }

  return response.json();
}

// ===========================================
// Top Speeds
// ===========================================

export async function fetchTopSpeeds(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/top-speeds/${sessionKey}`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch top speeds");
  }

  return response.json();
}

// ===========================================
// Fastest Laps
// ===========================================

export async function fetchFastestLaps(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/fastest-laps/${sessionKey}`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch fastest laps");
  }

  return response.json();
}

// ===========================================
// Meetings
// ===========================================

export async function fetchMeetings() {
  const response = await fetch(`${API_BASE_URL}/meetings`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch meetings");
  }

  return response.json();
}

// ===========================================
// Sessions
// ===========================================

export async function fetchSessions() {
  const response = await fetch(`${API_BASE_URL}/sessions`, {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch sessions");
  }

  return response.json();
}