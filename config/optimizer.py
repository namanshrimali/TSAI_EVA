import torch
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR, ReduceLROnPlateau

class Optimizer:
    @staticmethod
    def getOptimizer(mode, parameters, learning_rate):
        if mode is 'l2_bn' or 'l1_l2_bn' or 'l1_l2_gbn':
            return torch.optim.SGD(parameters, learning_rate, momentum=0, dampening=0, weight_decay=0.00001, nesterov=False)
        elif mode is 'l1_bn' or 'gbn':
            return torch.optim.SGD(parameters, learning_rate, momentum=0.9)

