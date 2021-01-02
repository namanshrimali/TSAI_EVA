# Reconnaissance
Second step of assignment 5.
The model in the previous step, even after reducing parameters from 18k to ~10k, had too many parameters. We need to achieve similar/greater accuracy with way lesser parameters and lesser time.

> Submitted By Naman Shrimali

## Model

On the top of previous model, this one have
- Has 9,954 parameters
- Trained for various epochs (I wanted to study the behaviour better). I have divided everything I did in `experiments`.
- Have massive `dropouts` of 30% after every two convolution layers.
- Have `BatchNormalization` after every convolution ( for better accuracy).
- Mostly involved playing with Learning Rate (To see how it affects the training of the model)

Checkout the model summary below

```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              80
              ReLU-2            [-1, 8, 26, 26]               0
       BatchNorm2d-3            [-1, 8, 26, 26]              16
            Conv2d-4           [-1, 16, 24, 24]           1,168
              ReLU-5           [-1, 16, 24, 24]               0
       BatchNorm2d-6           [-1, 16, 24, 24]              32
            Conv2d-7            [-1, 8, 24, 24]             136
         MaxPool2d-8            [-1, 8, 12, 12]               0
           Dropout-9            [-1, 8, 12, 12]               0
           Conv2d-10           [-1, 16, 10, 10]           1,168
             ReLU-11           [-1, 16, 10, 10]               0
      BatchNorm2d-12           [-1, 16, 10, 10]              32
           Conv2d-13             [-1, 16, 8, 8]           2,320
             ReLU-14             [-1, 16, 8, 8]               0
      BatchNorm2d-15             [-1, 16, 8, 8]              32
        MaxPool2d-16             [-1, 16, 4, 4]               0
          Dropout-17             [-1, 16, 4, 4]               0
           Conv2d-18             [-1, 32, 2, 2]           4,640
           Conv2d-19             [-1, 10, 2, 2]             330
================================================================
Total params: 9,954
Trainable params: 9,954
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.45
Params size (MB): 0.04
Estimated Total Size (MB): 0.49
----------------------------------------------------------------
```
## Expectations
- Decrease in training times (both for training and validation)
- Less overfitting ? (Lesser parameters for dataset of this size, and massive dropouts)

## Results
- ### Expirement One

    Ran the model for 50 epochs, with a learning rate of 0.05, the training started with 87.19% of training accuracy. The model eventually reached the accuracy of > 99.40%, highest being 99.49% (At 44th epoch). This means that the model is capable of achieveing higher accuracy given the learning rate is increased.
- ### Expirement Two

    Increased the learning rate to 0.01, added image augumentation of 7% tilt and trained the model for 30 epochs. The model started the training with training accuracy of 89.86%. The model managed to achieve >99.40% accuracy on several epochs, started the trend at 19th epochs. The highest the model got the validation accuracy was 99.50% (30th epoch), with training accuracy of 98.78%.
- ### Expirement Three
    Increased the learning rate to 0.02, trained the model for 30 epochs. The model started with 91.6367% as the training accuracy. The model first achieved the > 99% validation accuracy at 4th epoch, and continued the upward trend till 8th epoch (This happened before also in the 0.01 learning rate). The model achieved the highest validation accuracy of 99.45% several times (first at 25th epoch)
- ### Expirement Four

    Increased the learning rate to 0.04, the model started with 91% of training accuracy and first achieved the validation accuracy of > 99.4% (99.44%) at the 15th epoch. It then continued to overshoot the accuracy multiple times, and come up with the accuracy of > 99.4% again and again. It managed to get the highest validation accuracy of 99.45%.
- ### Expirement Five
    Increased the learning rate to 0.08, the model started with 93.3367% of training accuracy. It constantly over-shot the parameters, and was never able achieve the required > 99.4% accuracy. The model continued the forward trend till the 6th epoch, for which it achieved the validation accuracy of 99.17%, and then continued the pattern of rising-falling, and reached highest validation accuracy of 99.25%


## Takeaways
- Model, never overtrained and the maximum testing accuracy did not go beyond 99.0% (and that is expected, since I added a massive 30% of dropout while training)
- With smaller number of parameters, the model achieved validation accuracy of as high as 99.50% (in some cases, might not appear in logs)
- Both BatchNormalization and Dropouts worked fabulously, BatchNorm helped achieved desired accuracy in lesser number of parameters, while dropouts completly eliminated the problem of over-training of the model

## What's Next ?
- Decreasing parameters furthermore
- Playing with the learning rates, introducing schedulers
- Decrease the difference between training and the testing accuracy

