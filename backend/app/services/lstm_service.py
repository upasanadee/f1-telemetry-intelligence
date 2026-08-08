import numpy as np

from ml.dl.predictor import predict_lap_time


def predict_from_sequence(sequence):

    sequence = np.asarray(
        sequence,
        dtype=np.float32,
    )

    prediction = predict_lap_time(sequence)

    return {
        "predicted_lap_time": round(
            prediction,
            3,
        )
    }