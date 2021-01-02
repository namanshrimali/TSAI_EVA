# End Game
Final step of assignment 5.
Reduced number of parameters from 8.7k to 7k. Needed to achieve similar/greater accuracy with lesser parameters and lesser time.

> Submitted By Naman Shrimali

## Model

On the top of previous model, this one have
- Has 8,718 parameters
- Trained for 15 epochs .
- Have  `dropouts` of 3% after every convolution layers.
- Have `BatchNormalization` after every convolution ( for better accuracy).
- Have `Augumentations` added in the training phase.
- Mostly involved playing with Learning Rate (To see how it affects the training of the model), and introducing `Scheduler`, finding the sweet spot where the model works phenomenally.

Checkout the model summary below

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 10, 26, 26]             100
              ReLU-2           [-1, 10, 26, 26]               0
       BatchNorm2d-3           [-1, 10, 26, 26]              20
           Dropout-4           [-1, 10, 26, 26]               0
            Conv2d-5           [-1, 16, 24, 24]           1,456
              ReLU-6           [-1, 16, 24, 24]               0
       BatchNorm2d-7           [-1, 16, 24, 24]              32
           Dropout-8           [-1, 16, 24, 24]               0
         MaxPool2d-9           [-1, 16, 12, 12]               0
           Conv2d-10           [-1, 10, 10, 10]           1,450
             ReLU-11           [-1, 10, 10, 10]               0
      BatchNorm2d-12           [-1, 10, 10, 10]              20
          Dropout-13           [-1, 10, 10, 10]               0
           Conv2d-14             [-1, 16, 8, 8]           1,456
             ReLU-15             [-1, 16, 8, 8]               0
      BatchNorm2d-16             [-1, 16, 8, 8]              32
          Dropout-17             [-1, 16, 8, 8]               0
           Conv2d-18             [-1, 10, 6, 6]           1,450
             ReLU-19             [-1, 10, 6, 6]               0
      BatchNorm2d-20             [-1, 10, 6, 6]              20
          Dropout-21             [-1, 10, 6, 6]               0
           Conv2d-22             [-1, 10, 4, 4]             910
             ReLU-23             [-1, 10, 4, 4]               0
      BatchNorm2d-24             [-1, 10, 4, 4]              20
          Dropout-25             [-1, 10, 4, 4]               0
        AvgPool2d-26             [-1, 10, 1, 1]               0
           Conv2d-27             [-1, 10, 1, 1]             110
================================================================
Total params: 7,076
Trainable params: 7,076
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.58
Params size (MB): 0.03
Estimated Total Size (MB): 0.61
----------------------------------------------------------------

```
## Expectations
- Decrease in training times (both for training and validation)
- A constant validation accuracy of > 99.40% for the last few epochs.
- High marks !!

## Results
- Starting training accuracy : 87.51%
- Starting validation accuracy : 98.24%
- Peak training accuracy : 99.07%
- Peak validation accuracy : 99.55%
- Number of Epochs : 15
- Learning rate, started with 0.01, with a decay of 40% for every 10 cycles


## Takeaways
- Model, never overtrained and the maximum testing accuracy did not go beyond 99.0% (and that is expected, since I added a massive 30% of dropout while training)
- With smaller number of parameters, the model achieved validation accuracy of as high as 99.49%
- I did it !  Again !

## What's Next ?
- I forgot to remove biases, will do it later
- There are lots of variations, which I'll look at later
- I'm gonna sleep