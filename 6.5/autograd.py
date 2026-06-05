import torch

torch.manual_seed(42)
X = torch.randn(100,1)
y_true = 2*X + 1 + 0.1 * torch.randn(100,1)

w = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

lr = 0.1
epochs = 50

for epoch in range(epochs):
    y_pred = X*w + b
    loss = ((y_pred-y_true)**2).mean()
    loss.backward()

    with torch.no_grad():
        w -= lr*w.grad
        b -= lr*b.grad

    w.grad.zero_()
    b.grad.zero_()

    if (epoch+1)%10 ==0:
        print(f"Epoch {epoch+1:3d} | Loss: {loss.item():.4f} | w={w.item():.3f}, b={b.item():.3f}")
print(f"\n训练完成：w ≈ {w.item():.3f}（真实值 2.0），b ≈ {b.item():.3f}（真实值 1.0）")