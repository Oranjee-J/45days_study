import torch.nn as nn
import torch
from torch.utils.data import Dataset, DataLoader
texts = [
    "i love this movie",
    "this film is great",
    "i hate this movie",
    "this film is terrible",
    "good movie",
    "bad movie"
]

labels = [1, 1, 0, 0, 1, 0]

vocab = {"<PAD>": 0}

for text in texts:
    for word in text.split():
        if word not in vocab:
            vocab[word] = len(vocab)

print(vocab)

MAX_LEN = 5

def encode(text):

    ids = [vocab[word] for word in text.split()]

    ids = ids[:MAX_LEN]

    ids += [0] * (MAX_LEN - len(ids))

    return ids

class TextDataset(Dataset):

    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):

        x = torch.tensor(
            encode(self.texts[idx]),
            dtype=torch.long
        )

        y = torch.tensor(
            self.labels[idx],
            dtype=torch.long
        )

        return x, y

dataset = TextDataset(texts, labels)

train_loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

class LSTMClassifier(nn.Module):

    def __init__(
        self,
        vocab_size,
        embed_dim,
        hidden_dim,
        num_classes
    ):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            embed_dim
        )

        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_dim,
            num_classes
        )

    def forward(self, x):
        x = self.embedding(x)
        _, (h_n, c_n) = self.lstm(x)
        logits = self.fc(h_n[-1])
        return logits

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)    
model = LSTMClassifier(
    vocab_size=len(vocab),
    embed_dim=100,
    hidden_dim=128,
    num_classes=2
).to(device)

X = torch.randint(
    0,
    len(vocab),
    (2, 5)
).to(device)

output = model(X)

print(output.shape)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 20
for epoch in range(epochs):
    model.train()
    running_loss = 0
    for X, y in train_loader:
        X = X.to(device)
        y = y.to(device)
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(
        f"Epoch {epoch+1}, "
        f"Loss={running_loss/len(train_loader):.4f}"
    )