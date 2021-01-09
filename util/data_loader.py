import torch
from torchvision import datasets, transforms

class DataLoader():
    def __init__(self, batch_size, shuffle, kwargs):
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.kwargs = kwargs

    def load_train_data(self):
        return torch.utils.data.DataLoader(
            datasets.MNIST('../data', train=True, download=True,
                    transform=transforms.Compose([
                        transforms.RandomRotation((-7.0, 7.0), fill=(1,)),
                        transforms.ToTensor(),
                        transforms.Normalize((0.1307,), (0.3081,))
                    ])),
                    batch_size=self.batch_size, shuffle=self.shuffle, **self.kwargs)
    
    def load_test_data(self):
        return torch.utils.data.DataLoader(
            datasets.MNIST('../data', train=False, transform=transforms.Compose([
                        transforms.ToTensor(),
                        transforms.Normalize((0.1307,), (0.3081,))
                    ])),
                    batch_size=self.batch_size, shuffle=self.shuffle, **self.kwargs)
