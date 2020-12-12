# Assignment 3x - EMNIST Dataset
> Submitted by - Naman Shrimali

## Network has
   * 6 Convolution layers with these kernels (10, 10, 20, 20, 30)
   * no fully connected layer (have Global Average Pooling layer)
   * uses EMNIST as the dataset
   * uses a maximum of 2 max-pooling layers
   * Used Relu activation function for effective and easier decision making we into the model
   
## Network Summary

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 10, 28, 28]             100
            Conv2d-2           [-1, 10, 28, 28]             910
         MaxPool2d-3           [-1, 10, 14, 14]               0
            Conv2d-4           [-1, 20, 14, 14]           1,820
            Conv2d-5           [-1, 20, 14, 14]           3,620
         MaxPool2d-6             [-1, 20, 7, 7]               0
            Conv2d-7             [-1, 30, 5, 5]           5,430
            Conv2d-8             [-1, 26, 3, 3]           7,046
================================================================
Total params: 18,926
Trainable params: 18,926
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.21
Params size (MB): 0.07
Estimated Total Size (MB): 0.28
----------------------------------------------------------------
Device used : cuda
