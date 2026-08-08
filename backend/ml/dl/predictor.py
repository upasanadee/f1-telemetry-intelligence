import numpy as np
import torch

from ml.dl.model import LapTimeLSTM

# ==========================================
# Device
# ==========================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================================
# Load Model
# ==========================================

model = LapTimeLSTM().to(device)

model.load_state_dict(
    torch.load(
        "ml/models/lstm_best.pt",
        map_location=device,
    )
)

model.eval()

# ==========================================
# Load Normalization Parameters
# ==========================================

feature_mean = np.load(
    "ml/dl/feature_mean.npy"
).astype(np.float32)

feature_std = np.load(
    "ml/dl/feature_std.npy"
).astype(np.float32)

target_mean, target_std = np.load(
    "ml/dl/target_stats.npy"
).astype(np.float32)

# ==========================================
# Prediction Function
# ==========================================

def predict_lap_time(sequence):

    # Ensure float32
    sequence = sequence.astype(np.float32)

    # Normalize
    sequence = (
        (sequence - feature_mean)
        / feature_std
    ).astype(np.float32)

    # Convert to tensor
    x = (
        torch.from_numpy(sequence)
        .unsqueeze(0)
        .float()
        .to(device)
    )

    lengths = torch.tensor(
        [len(sequence)],
        dtype=torch.long,
    )

    # Inference
    with torch.no_grad():

        prediction = model(
            x,
            lengths,
        ).item()

    # Convert back to seconds
    prediction = (
        prediction * target_std
        + target_mean
    )

    return float(prediction)