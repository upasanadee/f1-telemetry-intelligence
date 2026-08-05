export interface PerformanceScore {
  rank: number;
  driver_number: number;
  driver_name: string;
  team_name: string;

  lap_score: number;
  speed_score: number;
  average_speed_score: number;
  throttle_score: number;
  brake_score: number;
  drs_score: number;

  performance_score: number;
}