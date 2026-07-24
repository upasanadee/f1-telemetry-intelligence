from etl.client import OpenF1Client

client = OpenF1Client()


def extract_meetings(year):
    return client.get_meetings(year)


def extract_sessions(meeting_key):
    return client.get_sessions(meeting_key)


def extract_drivers(session_key):
    return client.get_drivers(session_key)


def extract_laps(session_key, driver_number):
    return client.get_laps(session_key, driver_number)


def extract_car_data(session_key, driver_number):
    return client.get_car_data(session_key, driver_number)

def extract_positions(session_key):

    return client.get_positions(session_key)


def extract_weather(session_key):

    return client.get_weather(session_key)


def extract_race_control(session_key):

    return client.get_race_control(session_key)


def extract_team_radio(session_key, driver_number):

    return client.get_team_radio(
        session_key,
        driver_number,
    )