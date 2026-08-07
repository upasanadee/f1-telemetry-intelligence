import torch
from torch.nn.utils.rnn import pad_sequence


def collate_fn(batch):

    sequences = [x[0] for x in batch]

    targets = torch.stack(
        [x[1] for x in batch]
    )

    lengths = torch.tensor(
        [len(s) for s in sequences]
    )

    padded = pad_sequence(
        sequences,
        batch_first=True,
    )

    return (
        padded,
        lengths,
        targets,
    )