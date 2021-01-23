import torch
import torch.nn as nn
import torch.nn.functional as F


class ModelCifar(nn.Module):
    def __init__(self):
        super(ModelCifar, self).__init__()

        self.conv_lyr1 = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding= 2, padding_mode= 'replicate'), #3, 32
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(0.03),

            nn.Conv2d(32, 64, 3, padding= 2 , padding_mode= 'replicate'), # 5, 32
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.03),
            nn.MaxPool2d(2, 2) #10, 16
        )

        self.dpthwse_sprbl_lyr1 = nn.Sequential(
            nn.Conv2d(64, 64, 3, padding= 2, padding_mode= 'replicate', groups= 64), #12, 16
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.03),

            nn.Conv2d(64, 64, 3, padding= 2, padding_mode= 'replicate', groups= 64), #14, 16
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.03),
            
            nn.Conv2d(64, 128, 1),
            nn.MaxPool2d(2, 2) #28, 8
        )

        self.dpthwse_sprbl_lyr2 = nn.Sequential(
            nn.Conv2d(128, 128, 3, padding= 2, padding_mode= 'replicate', groups= 128), #30, 8
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(0.03),

            nn.Conv2d(128, 128, 3, padding= 2, padding_mode= 'replicate', groups= 128), #32, 8
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(0.03),
            
            nn.Conv2d(128, 256, 1), #32, 8
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Dropout(0.03)
        )

        self.dil_lyr1 = nn.Sequential(
            nn.Conv2d(256, 256, 3, dilation=2), #36, 8
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Dropout(0.03),

            nn.Conv2d(256, 256, 3, dilation=2), #40, 6
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Dropout(0.03)
        )

        self.fnl_lyr = nn.Sequential(
            nn.Conv2d(256, 64, 1), #4
            nn.Conv2d(64, 10, 1),
            nn.AvgPool2d(kernel_size=4)
        )

    def forward(self, x):
        x = self.conv_lyr1(x)
        x = self.dpthwse_sprbl_lyr1(x)
        x = self.dpthwse_sprbl_lyr2(x)
        x = self.dil_lyr1(x)
        x = self.fnl_lyr(x)
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=1)





