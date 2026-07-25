const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

console.log("API URL:", API_BASE_URL);

export async function fetchPerformanceScores(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/performance-score/${sessionKey}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch performance scores");
  }

  return response.json();
}

export async function fetchRaceSummary(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/race-summary/${sessionKey}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch race summary");
  }

  return response.json();
}

export async function fetchTopSpeeds(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/top-speeds/${sessionKey}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch top speeds");
  }

  return response.json();
}

export async function fetchFastestLaps(sessionKey: number) {
  const response = await fetch(
    `${API_BASE_URL}/analytics/fastest-laps/${sessionKey}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch fastest laps");
  }

  return response.json();
}