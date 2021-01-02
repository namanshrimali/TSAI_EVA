# Salvation
Third step of assignment 5.
Reduced number of parameters from 9.8k to 8.7k. Needed to achieve similar/greater accuracy with lesser parameters and lesser time.

> Submitted By Naman Shrimali

## Model

On the top of previous model, this one have
- Has 8,718 parameters
- Trained for 15 epochs .
- Have massive `dropouts` of 30% after every two convolution layers.
- Have `BatchNormalization` after every convolution ( for better accuracy).
- Have `Augumentations` added in the training phase.
- Mostly involved playing with Learning Rate (To see how it affects the training of the model), and introducing `Scheduler`, finding the sweet spot where the model works phenomenally.

Checkout the model summary below

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 10, 26, 26]              90
              ReLU-2           [-1, 10, 26, 26]               0
       BatchNorm2d-3           [-1, 10, 26, 26]              20
            Conv2d-4           [-1, 16, 24, 24]           1,440
              ReLU-5           [-1, 16, 24, 24]               0
       BatchNorm2d-6           [-1, 16, 24, 24]              32
         MaxPool2d-7           [-1, 16, 12, 12]               0
           Dropout-8           [-1, 16, 12, 12]               0
            Conv2d-9           [-1, 16, 10, 10]           2,304
             ReLU-10           [-1, 16, 10, 10]               0
      BatchNorm2d-11           [-1, 16, 10, 10]              32
           Conv2d-12             [-1, 16, 8, 8]           2,304
             ReLU-13             [-1, 16, 8, 8]               0
      BatchNorm2d-14             [-1, 16, 8, 8]              32
        MaxPool2d-15             [-1, 16, 4, 4]               0
          Dropout-16             [-1, 16, 4, 4]               0
           Conv2d-17             [-1, 16, 2, 2]           2,304
           Conv2d-18             [-1, 10, 2, 2]             160
================================================================
Total params: 8,718
Trainable params: 8,718
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.47
Params size (MB): 0.03
Estimated Total Size (MB): 0.50
----------------------------------------------------------------
```
## Expectations
- Decrease in training times (both for training and validation)
- A constant validation accuracy of > 99.40% for the last few epochs.

## Results
- Starting testing accuracy : 92.17%
- Starting validation accuracy : 98.33%
- Peak testing accuracy : 98.84%
- Peak validation accuracy : 99.48%
- Number of Epochs : 15
- Learning rate, started with 0.02, with a decay of 50% for every 6 cycles


## Takeaways
- Model, never overtrained and the maximum testing accuracy did not go beyond 99.0% (and that is expected, since I added a massive 30% of dropout while training)
- With smaller number of parameters, the model achieved validation accuracy of as high as 99.48% (in some cases, might not appear in logs)
- Adding augumentations helped in getting the training accuracy of the model upto a certain level, while finding the ideal learning rate, with a scheduler that compliments the learning with a much needed decay really helped to achieve a stable validation accuracy of > 99.40%
- I did it !

## What's Next ?
- Decreasing parameters furthermore
- Decrease the difference between training and the testing accuracy
- An accuracy of 99.5% (I wish)
- Calculation of accurate receptive fields
