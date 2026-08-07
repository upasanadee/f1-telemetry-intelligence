import torch
import torch.nn as nn

from torch.utils.data import DataLoader
from torch.utils.data import random_split

from ml.dl.dataset import LapSequenceDataset
from ml.dl.utils import collate_fn
from ml.dl.model import LapTimeLSTM

# ==========================================
# Device
# ==========================================

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print(f"\nUsing device: {device}")

# ==========================================
# Dataset
# ==========================================

dataset = LapSequenceDataset(
    sequence_dir="ml/dl/sequences",
    labels_csv="ml/dl/labels.csv",
)

print(f"Total samples : {len(dataset)}")

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size],
)

print(f"Train samples : {len(train_dataset)}")
print(f"Val samples   : {len(val_dataset)}")

train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True,
    collate_fn=collate_fn,
    num_workers=2,
    pin_memory=False,
)

val_loader = DataLoader(
    val_dataset,
    batch_size=16,
    shuffle=False,
    collate_fn=collate_fn,
    num_workers=2,
    pin_memory=False,
)

print("DataLoaders ready.\n")

# ==========================================
# Model
# ==========================================

model = LapTimeLSTM().to(device)

criterion = nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=1e-3,
)

best_val = float("inf")

# ==========================================
# Training
# ==========================================

EPOCHS = 1

for epoch in range(EPOCHS):

    print(f"\n========== Epoch {epoch+1}/{EPOCHS} ==========")

    model.train()

    train_loss = 0.0

    for batch_idx, (x, lengths, y) in enumerate(train_loader):

        if batch_idx == 0:
            print("Loading first batch...")

        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()

        prediction = model(
            x,
            lengths,
        )

        loss = criterion(
            prediction,
            y,
        )

        loss.backward()

        optimizer.step()

        train_loss += loss.item()

        if (batch_idx + 1) % 200 == 0:
            print(
                f"Batch {batch_idx+1}/{len(train_loader)} | "
                f"Loss {loss.item():.4f}"
            )

    train_loss /= len(train_loader)

    # ==========================================
    # Validation
    # ==========================================

    model.eval()

    val_loss = 0.0

    with torch.no_grad():

        for x, lengths, y in val_loader:

            x = x.to(device)
            y = y.to(device)

            prediction = model(
                x,
                lengths,
            )

            loss = criterion(
                prediction,
                y,
            )

            val_loss += loss.item()

    val_loss /= len(val_loader)

    print(
        f"\nEpoch {epoch+1:02d}"
        f" | Train Loss: {train_loss:.4f}"
        f" | Val Loss: {val_loss:.4f}"
    )

    if val_loss < best_val:

        best_val = val_loss

        torch.save(
            model.state_dict(),
            "ml/models/lstm.pt",
        )

        print("✓ Best model saved.")

print("\nTraining Complete.")