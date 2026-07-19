const API = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export async function getTelemetry() {
  const res = await fetch(`${API}/api/telemetry`);

  if (!res.ok) {
    throw new Error("Failed to fetch telemetry");
  }

  return res.json();
}
