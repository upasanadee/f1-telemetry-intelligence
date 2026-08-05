export interface Meeting {
  meeting_key: number;
  meeting_name: string;
  country_name: string;
  location: string;
  year: number;
}

export interface Session {
  session_key: number;
  meeting_key: number;
  session_name: string;
  session_type: string;
  date_start: string;
  date_end: string;
}