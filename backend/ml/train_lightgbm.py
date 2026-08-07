import joblib
import lightgbm as lgb
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("ml/dataset_clean.csv")

# ==========================================
# Features
# ==========================================

FEATURES = [

    # Lap statistics
    "average_lap",
    "lap_std",
    "total_laps",

    # Telemetry
    "average_speed",
    "max_speed",
    "average_rpm",
    "average_gear",
    "average_throttle",
    "average_brake",
    "drs_usage",

    # Weather
    "track_temp",
    "air_temp",
    "humidity",
    "wind_speed",
]

TARGET = "performance_index"

X = df[FEATURES]
y = df[TARGET]

# ==========================================
# Train/Test Split
# ==========================================

from sklearn.model_selection import GroupShuffleSplit

groups = df["session_key"]

splitter = GroupShuffleSplit(
    test_size=0.2,
    n_splits=1,
    random_state=42,
)

train_idx, test_idx = next(
    splitter.split(
        X,
        y,
        groups,
    )
)

X_train = X.iloc[train_idx]
X_test = X.iloc[test_idx]

y_train = y.iloc[train_idx]
y_test = y.iloc[test_idx]

# ==========================================
# LightGBM Model
# ==========================================

model = lgb.LGBMRegressor(

    objective="regression",

    n_estimators=1500,

    learning_rate=0.02,

    num_leaves=31,

    max_depth=6,

    min_child_samples=15,

    feature_fraction=0.8,

    bagging_fraction=0.8,

    bagging_freq=5,

    reg_alpha=0.3,

    reg_lambda=0.5,

    random_state=42,
)

model.fit(X_train, y_train)

# ==========================================
# Predictions
# ==========================================

predictions = model.predict(X_test)
results = X_test.copy()

results["Actual"] = y_test.values
results["Predicted"] = predictions

results.to_csv(
    "ml/predictions.csv",
    index=False,
)

print("\nSaved predictions to ml/predictions.csv")

print("\nModel Performance\n")

print(
    "MAE :",
    round(mean_absolute_error(y_test, predictions), 3),
)

print(
    "RMSE:",
    round(
        mean_squared_error(
            y_test,
            predictions,
        ) ** 0.5,
        3,
    ),
)

print(
    "R²  :",
    round(r2_score(y_test, predictions), 3),
)

# ==========================================
# Feature Importance
# ==========================================

importance = (
    pd.DataFrame(
        {
            "Feature": FEATURES,
            "Importance": model.feature_importances_,
        }
    )
    .sort_values(
        "Importance",
        ascending=False,
    )
)

print("\nFeature Importance\n")
print(importance)

# ==========================================
# Save Model
# ==========================================

joblib.dump(
    model,
    "ml/models/lightgbm_model.pkl",
)

print("\nModel saved successfully!")