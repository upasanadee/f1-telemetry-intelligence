from etl.client import OpenF1Client

client = OpenF1Client()

SESSION_KEY = 9462

for driver in [1, 2, 3, 4]:
    data = client.get_car_data(SESSION_KEY, driver)

    print(f"\nDriver {driver}")
    print(f"Rows: {len(data)}")

    unique_drivers = {row["driver_number"] for row in data}

    print(f"Unique driver numbers: {unique_drivers}")

    if data:
        print("First record:")
        print(data[0])