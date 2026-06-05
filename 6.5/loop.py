import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

dataset = TensorDataset(X, y)

train_loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

model = nn.Linear(1, 1)

criterion = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

epochs = 100

for epoch in range(epochs):
    for X_batch, y_batch in train_loader:

        pred = model(X_batch)
        loss = criterion(pred, y_batch)
        optimizer.zero_grad()

        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss={loss.item():.4f}")


print(model.weight)
print(model.bias)