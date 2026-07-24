import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class OpenF1Client:

    BASE_URL = "https://api.openf1.org/v1"

    def __init__(self):

        self.session = requests.Session()

        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        adapter = HTTPAdapter(max_retries=retries)

        self.session.mount("https://", adapter)

    def get(self, endpoint, params=None):

        response = self.session.get(
            f"{self.BASE_URL}/{endpoint}",
            params=params,
            timeout=30,
        )

        if response.status_code == 404:
            return []

        response.raise_for_status()

        return response.json()

    # -----------------------------
    # Convenience methods
    # -----------------------------

    def get_meetings(self, year):

        return self.get(
            "meetings",
            {"year": year},
        )

    def get_sessions(self, meeting_key):

        return self.get(
            "sessions",
            {"meeting_key": meeting_key},
        )

    def get_drivers(self, session_key):

        return self.get(
            "drivers",
            {"session_key": session_key},
        )

    def get_laps(self, session_key, driver_number):

        return self.get(
            "laps",
            {
                "session_key": session_key,
                "driver_number": driver_number,
            },
        )

    def get_car_data(self, session_key, driver_number):

        return self.get(
            "car_data",
            {
                "session_key": session_key,
                "driver_number": driver_number,
            },
        )
    def get_positions(self, session_key):

        return self.get(
            "position",
            {
                "session_key": session_key,
            },
        )


    def get_weather(self, session_key):

        return self.get(
            "weather",
            {
                "session_key": session_key,
            },
        )


    def get_race_control(self, session_key):

        return self.get(
            "race_control",
            {
                "session_key": session_key,
            },
        )


    def get_team_radio(self, session_key, driver_number):

        return self.get(
            "team_radio",
            {
                "session_key": session_key,
                "driver_number": driver_number,
            },
        )

