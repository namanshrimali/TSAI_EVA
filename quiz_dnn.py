import torch
import torch.nn as nn
import torch.nn.functional as F

class QuizDnn(nn.Module):
    def __init__(self):
        super(QuizDnn, self).__init__()

        self.conv_lyr1 = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding= 1, padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(0.15),

            nn.Conv2d(32, 64, 3, padding= 1 , padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.15),
            nn.MaxPool2d(2, 2)
        )
        
        self.conv_lyr2 = nn.Sequential(
            nn.Conv2d(64, 64, 3, padding= 1, padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.15),

            nn.Conv2d(64, 64, 3, padding= 1 , padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(0.15),

            nn.Conv2d(64, 128, 3, padding= 1 , padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(0.15),

            nn.MaxPool2d(2, 2)
        )

        self.conv_lyr3 = nn.Sequential(
            nn.Conv2d(128, 256, 3, padding= 0, padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Dropout(0.15),

            nn.Conv2d(256, 256, 3, padding= 0 , padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Dropout(0.15),

            nn.Conv2d(256, 10, 1, padding= 0 , padding_mode= 'replicate'),
            nn.ReLU(),
            nn.BatchNorm2d(10),
            nn.Dropout(0.15)
        )
        
        self.fnl_lyr = nn.Sequential(
            nn.AvgPool2d(kernel_size=4)
        )


    def forward(self, x):
        x = self.conv_lyr1(x)
        x = self.conv_lyr2(x)
        x = self.conv_lyr3(x)
        x = self.fnl_lyr(x)
        x = x.view(-1, 10)
        return F.log_softmax(x)