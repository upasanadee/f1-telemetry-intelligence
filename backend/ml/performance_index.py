import pandas as pd

df = pd.read_csv("ml/dataset_clean.csv")

# Fastest lap in each session
session_fastest = (
    df.groupby("session_key")["fastest_lap"]
    .transform("min")
)

# Relative pace (100 = fastest)
df["performance_index"] = (
    session_fastest
    / df["fastest_lap"]
) * 100

df.to_csv(
    "ml/dataset_clean.csv",
    index=False,
)

print(df[[
    "driver_name",
    "fastest_lap",
    "performance_index",
]].head())

print()

print(df["performance_index"].describe())

print("\nPerformance Index updated!")