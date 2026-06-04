import torch.nn as nn
class SimpleFCN(nn.Module):
    def __init__(self, input_size, num_class):
        super(SimpleFCN,self).__init__()
        self.fc1 = nn.Linear(input_size,128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128,64)
        self.fc3 = nn.Linear(64,num_class)

    def forward(self,x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x
    

model = SimpleFCN(input_size=100,num_class=10)