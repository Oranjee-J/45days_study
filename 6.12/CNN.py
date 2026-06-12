from torchvision.datasets import MNIST
import torchvision.transforms  as transforms
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.optim as optim

transform = transforms.ToTensor()
train_dataset = MNIST(
    root='./data',
    train=True,
    transform=transform,
    download=True
)
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True)

image, label = train_dataset[0]


X, y = next(iter(train_loader))

class FirstNet(nn.Module):
    def __init__(self):
        super(FirstNet, self).__init__()
        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            padding=1)
        self.relu1 = nn.ReLU()
        self.pooling1 = nn.MaxPool2d(
            kernel_size=2,
            stride=2)
        self.conv2 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            padding=1)
        self.relu2 = nn.ReLU()
        self.pooling2 = nn.MaxPool2d(
            kernel_size=2,
            stride=2)
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(
            in_features=1568,
            out_features=10)
        

    def forward(self,x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pooling1(x)
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pooling2(x)
        x = self.flatten(x)
        x = self.linear(x)

        return x

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)
model = FirstNet().to(device)

output = model(X)

criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 5

for epoch in range(epochs):

    model.train()

    running_loss = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        running_loss += loss.item()


    print(
        f"Epoch {epoch+1}, "
        f"Loss: {running_loss/len(train_loader):.4f}"
    )


torch.save(
    model.state_dict(),
    "mnist_cnn.pth"
)

print("Successfully saved!!")