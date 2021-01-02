# GENESIS
The begining of the assignment 5.
Previous model had too many parameters (6.3 million parameters !). We need to achieve similar/greater accuracy with way lesser parameters and lesser time.

> Submitted By Naman Shrimali

## Model

The model
- Has 18,578 parameters
- Trained for 30 epochs (I wanted to study the behaviour better), with a learning rate of 0.01
- No fully connected layer
- Works on MNIST dataset
- Uses Relu activation function for effective and easier decision making we into the model

Checkout the model summary below

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 16, 28, 28]             160
              ReLU-2           [-1, 16, 28, 28]               0
            Conv2d-3           [-1, 32, 28, 28]           4,640
              ReLU-4           [-1, 32, 28, 28]               0
            Conv2d-5            [-1, 8, 28, 28]             264
         MaxPool2d-6            [-1, 8, 14, 14]               0
            Conv2d-7           [-1, 16, 14, 14]           1,168
              ReLU-8           [-1, 16, 14, 14]               0
            Conv2d-9           [-1, 32, 14, 14]           4,640
             ReLU-10           [-1, 32, 14, 14]               0
           Conv2d-11            [-1, 8, 14, 14]             264
        MaxPool2d-12              [-1, 8, 7, 7]               0
           Conv2d-13             [-1, 16, 7, 7]           1,168
             ReLU-14             [-1, 16, 7, 7]               0
      BatchNorm2d-15             [-1, 16, 7, 7]              32
           Conv2d-16             [-1, 32, 7, 7]           4,640
             ReLU-17             [-1, 32, 7, 7]               0
           Conv2d-18              [-1, 8, 7, 7]             264
        MaxPool2d-19              [-1, 8, 3, 3]               0
           Conv2d-20             [-1, 16, 1, 1]           1,168
           Conv2d-21             [-1, 10, 1, 1]             170
================================================================
Total params: 18,578
Trainable params: 18,578
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.84
Params size (MB): 0.07
Estimated Total Size (MB): 0.91
----------------------------------------------------------------
```
## Expectations
- Faster training time
- Decrease in accuracy (as we significantly reduced number of parameters by a very very large margin)
- Decrease in training times (both for training and validation)
- Less overfitting ? (Lesser parameters for dataset of this size)

## Results
- Starting training accuracy - 77.08%`
- Starting validation accuracy - 97.46%
- Max training accuracy - 100% (at epoch 30)
- Max validation accuracy - 99.26% (also at epoch 30)

## Takeaways
- The model started at low accuracy, 77.08%
- Model, even with significantly low number of parameters (~18.7k), overtrained and reached maximum testing accuracy of 100% (I'm not an expert in AI/ML, but even I believe something went wrong)
- There are huge ups and downs for the validation accuracy (sometimes more than 10%, `guess what resembles my mental health in 2020`)
- I make self deprecating jokes when I'm nervous go according to plan

## What's Next ?
- Decreasing parameters furthermore
- Adding Batch Normalization to sharpen the features of model for better accuracy
- Adding a regularization to decrease the difference between training and the testing accuracy

