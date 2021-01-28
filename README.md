#  Assignment 7

> Submitted by Naman Shrimali

## Target
* Fix the network -change the code such that it uses GPU
* Change the architecture to C1C2C3C40 (basically 3 MPs)
* Total RF must be more than 44 one of the layers must use Depthwise Separable Convolution
* One of the layers must use Dilated Convolution
* Use GAP (compulsory):- add FC after GAP to target #of classes (optional)
* Achieve 80% accuracy, as many epochs as you want. Total Params to be - less than 1M.
* Upload to Github

## Submission
I have trained model, summary and observationsd details can be found below.

---

### Results
* No of parameters: 671,690
* No of epochs: 10
* Dropout: 15%
* First training accuracy: 50.3740%
* First testing accuracy: 64.90%
* Highest training accuracy: 86.3680%
* Highest testing accuracy: 83.17%

---
### Model


```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 32, 32, 32]             896
              ReLU-2           [-1, 32, 32, 32]               0
       BatchNorm2d-3           [-1, 32, 32, 32]              64
           Dropout-4           [-1, 32, 32, 32]               0
            Conv2d-5           [-1, 64, 32, 32]          18,496
              ReLU-6           [-1, 64, 32, 32]               0
       BatchNorm2d-7           [-1, 64, 32, 32]             128
           Dropout-8           [-1, 64, 32, 32]               0
         MaxPool2d-9           [-1, 64, 16, 16]               0
           Conv2d-10           [-1, 64, 16, 16]             640
             ReLU-11           [-1, 64, 16, 16]               0
      BatchNorm2d-12           [-1, 64, 16, 16]             128
          Dropout-13           [-1, 64, 16, 16]               0
           Conv2d-14          [-1, 128, 16, 16]           8,320
             ReLU-15          [-1, 128, 16, 16]               0
      BatchNorm2d-16          [-1, 128, 16, 16]             256
        MaxPool2d-17            [-1, 128, 8, 8]               0
           Conv2d-18            [-1, 128, 8, 8]           1,280
             ReLU-19            [-1, 128, 8, 8]               0
      BatchNorm2d-20            [-1, 128, 8, 8]             256
          Dropout-21            [-1, 128, 8, 8]               0
           Conv2d-22            [-1, 256, 8, 8]          33,024
             ReLU-23            [-1, 256, 8, 8]               0
      BatchNorm2d-24            [-1, 256, 8, 8]             512
          Dropout-25            [-1, 256, 8, 8]               0
           Conv2d-26            [-1, 256, 4, 4]         590,080
             ReLU-27            [-1, 256, 4, 4]               0
      BatchNorm2d-28            [-1, 256, 4, 4]             512
          Dropout-29            [-1, 256, 4, 4]               0
           Conv2d-30             [-1, 64, 4, 4]          16,448
             ReLU-31             [-1, 64, 4, 4]               0
           Conv2d-32             [-1, 10, 4, 4]             650
             ReLU-33             [-1, 10, 4, 4]               0
        AvgPool2d-34             [-1, 10, 1, 1]               0
================================================================
Total params: 671,690
Trainable params: 671,690
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 5.33
Params size (MB): 2.56
Estimated Total Size (MB): 7.90
----------------------------------------------------------------
```
---
### Observations
* Model is overfitting
* I have used two depthwise seperable convolution layers (64 x 64 (group size 64) followed by `AntMan` to increase channels to 128, and 128 x 128 (group of 128), followed by `Antman` to increase channel size to 256)
* A dialated convolution is used with dialation of 2 is used
* At last layer, global average pooling with kernel= 4 is used.
* This is followed by a fully connected layer to straighten out
* Learning rate is `0.2`, a scheduler is applied with gamma of 0.5 and step size of 8
---
## Future aspirations
* None :(
## Receptive field calculation
![RF_Calc](images\receptive_field.png)
