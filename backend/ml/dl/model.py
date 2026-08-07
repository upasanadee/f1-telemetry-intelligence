import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence


class LapTimeLSTM(nn.Module):

    def __init__(
        self,
        input_size=7,
        hidden_size=128,
        num_layers=2,
        dropout=0.3,
    ):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout,
            bidirectional=True,
        )

        self.regressor = nn.Sequential(
            nn.Linear(hidden_size * 2, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 1),
        )

    def forward(
        self,
        x,
        lengths,
    ):

        packed = pack_padded_sequence(
            x,
            lengths.cpu(),
            batch_first=True,
            enforce_sorted=False,
        )

        _, (hidden, _) = self.lstm(packed)

        # forward + backward
        embedding = torch.cat(
            (
                hidden[-2],
                hidden[-1],
            ),
            dim=1,
        )

        prediction = self.regressor(
            embedding
        )

        return prediction.squeeze(1)