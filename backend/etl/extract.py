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

