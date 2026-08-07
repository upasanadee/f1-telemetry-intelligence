import numpy as np
import pandas as pd

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv("ml/dataset.csv")

# ==========================================================
# Remove Invalid Samples
# ==========================================================

# Remove drivers with no valid timed lap
df = df.dropna(
    subset=[
        "fastest_lap",
        "lap_std",
    ]
)

# Remove impossible fastest laps
# (No 2024 F1 circuit has a competitive lap > 200 sec)
df = df[df.fastest_lap < 200]

# Driver should have completed at least 3 laps
df = df[df.total_laps >= 3]

# Remove telemetry errors
df = df[df.max_speed > 150]

# Reset index
df.reset_index(drop=True, inplace=True)

print(f"Clean dataset shape: {df.shape}")

# ==========================================================
# Create ML Target
# ==========================================================

df["target"] = np.nan

for session in df["session_key"].unique():

    session_mask = df["session_key"] == session

    ranked = (
        df.loc[session_mask]
        .sort_values("fastest_lap")
    )

    num_drivers = len(ranked)

    # Skip empty sessions
    if num_drivers == 0:
        continue

    # Best driver = 100
    # Worst driver = 0
    scores = np.linspace(
        100,
        0,
        num_drivers,
    )

    df.loc[
        ranked.index,
        "target",
    ] = scores

# ==========================================================
# Save Dataset
# ==========================================================

df.to_csv(
    "ml/dataset_clean.csv",
    index=False,
)

print("\nDataset cleaned successfully!")

print("\nFirst 5 rows:")
print(df.head())

print("\nDrivers per session:")
print(df.groupby("session_key").size().describe())