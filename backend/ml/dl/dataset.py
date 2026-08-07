import os

import numpy as np
import pandas as pd

import torch
from torch.utils.data import Dataset


class LapSequenceDataset(Dataset):

    def __init__(
        self,
        sequence_dir,
        labels_csv,
    ):

        self.sequence_dir = sequence_dir

        self.labels = pd.read_csv(labels_csv)

        # remove obviously broken laps
        self.labels = self.labels[
            self.labels["lap_duration"] < 200
        ].reset_index(drop=True)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):

        row = self.labels.iloc[idx]

        sequence = np.load(
            os.path.join(
                self.sequence_dir,
                row["file"],
            )
        )

        sequence = sequence.astype(np.float32)

        target = np.float32(
            row["lap_duration"]
        )

        return (
            torch.tensor(sequence),
            torch.tensor(target),
        )