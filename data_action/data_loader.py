from data_action.transformations import *

class Data_Loader:
    def __init__(self, device, batch_size):
        self.device = device
        self.batch_size = batch_size
        self.kwargs = {'num_workers': 2, 'pin_memory': True} if device=="cuda" else {}
    
    def load_training_data(self):
        print('Loading training data. Dataset: CIFAR10')
        trainloader = torch.utils.data.DataLoader(
            torchvision.datasets.CIFAR10(root='data', train=True, download=True, transform=get_train_transforms()), 
            self.batch_size,
            shuffle=True,
            **self.kwargs)
        print('Training data loaded\n')
        return trainloader

    def load_testing_data(self):
        print('Loading testing data.')
        testloader = torch.utils.data.DataLoader(
            torchvision.datasets.CIFAR10(root='data', train=False, download=True, transform=get_test_transforms()),
            self.batch_size,
            shuffle=False, 
            **self.kwargs)
        print('Test data loaded\n')
        return testloader
