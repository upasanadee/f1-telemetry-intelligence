from torch.utils.data import DataLoader

from ml.dl.dataset import LapSequenceDataset
from ml.dl.utils import collate_fn

dataset = LapSequenceDataset(
    sequence_dir="ml/dl/sequences",
    labels_csv="ml/dl/labels.csv",
)

loader = DataLoader(
    dataset,
    batch_size=8,
    shuffle=True,
    collate_fn=collate_fn,
)

x, lengths, y = next(iter(loader))

print("Input Shape :", x.shape)
print("Lengths     :", lengths)
print("Targets     :", y.shape)