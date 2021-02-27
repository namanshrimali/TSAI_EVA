#  Assignment 11 - SuperConvergence

> Submitted by Naman Shrimali

## Target

* Write a code that draws this curve (without the arrows). In submission, you'll upload your drawn curve and code for that
![ZigZagQuestion](/assets/images/11s6-1.png)
* Write a code which
uses this new ResNet Architecture for Cifar10:
    - PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
    - Layer1 -
    - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
    - R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
    - Add(X, R1)
    - Layer 2 -Conv 3x3 [256k]
    - MaxPooling2D
    - BN
    - ReLU
    - Layer 3 -
    - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
    - R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
    - Add(X, R2)
    - MaxPooling with Kernel Size 4
    - FC Layer 
    - SoftMax
* Uses One Cycle Policy such that:
    - Total Epochs = 24
    - Max at Epoch = 5
    - LRMIN = FIND
    - LRMAX = FIND
    - NO Annihilation
* Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
* Batch size = 512
* Target Accuracy: 90%. 


## Submission
I have trained model, summary and observationsd details can be found below.

**I wasn't able to achieve 90% accuracy while training on colab with batch size of 512, but I did able to achieve the same with a batch size of 128 in my local machine. As of now, I'm looking for some way that I can achieve the same through bigger batch sizes** 

---

### Results
* No of parameters: 6,573,120
* Batch Size: 128
* No of epochs: 24
* Optimal Learning Rate: 7.05E-02
* Dropout: 0%
* First training accuracy: 52.5120%
* First testing accuracy: 62.24%
* Highest training accuracy: 98.8720%
* Highest testing accuracy: 90.70%

---
### Model


```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 64, 32, 32]           1,728
       BatchNorm2d-2           [-1, 64, 32, 32]             128
              ReLU-3           [-1, 64, 32, 32]               0
            Conv2d-4          [-1, 128, 32, 32]          73,728
         MaxPool2d-5          [-1, 128, 16, 16]               0
       BatchNorm2d-6          [-1, 128, 16, 16]             256
              ReLU-7          [-1, 128, 16, 16]               0
            Conv2d-8          [-1, 128, 16, 16]         147,456
       BatchNorm2d-9          [-1, 128, 16, 16]             256
          Dropout-10          [-1, 128, 16, 16]               0
           Conv2d-11          [-1, 128, 16, 16]         147,456
      BatchNorm2d-12          [-1, 128, 16, 16]             256
          Dropout-13          [-1, 128, 16, 16]               0
       BasicBlock-14          [-1, 128, 16, 16]               0
           Conv2d-15          [-1, 256, 14, 14]         294,912
        MaxPool2d-16            [-1, 256, 7, 7]               0
      BatchNorm2d-17            [-1, 256, 7, 7]             512
             ReLU-18            [-1, 256, 7, 7]               0
           Conv2d-19            [-1, 512, 7, 7]       1,179,648
      BatchNorm2d-20            [-1, 512, 7, 7]           1,024
             ReLU-21            [-1, 512, 7, 7]               0
           Conv2d-22            [-1, 512, 7, 7]       2,359,296
      BatchNorm2d-23            [-1, 512, 7, 7]           1,024
          Dropout-24            [-1, 512, 7, 7]               0
           Conv2d-25            [-1, 512, 7, 7]       2,359,296
      BatchNorm2d-26            [-1, 512, 7, 7]           1,024
          Dropout-27            [-1, 512, 7, 7]               0
       BasicBlock-28            [-1, 512, 7, 7]               0
          Flatten-29                  [-1, 512]               0
           Linear-30                   [-1, 10]           5,120
================================================================
Total params: 6,573,120
Trainable params: 6,573,120
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 7.59
Params size (MB): 25.07
Estimated Total Size (MB): 32.67
-------------------------------------------------------------------
```
---
### Observations
* Model is overfitting (obvioisly, augumentations are far lesser than what we did last time)
* The maximum learning rate was determined by optimal lr finder, which ran for _1000 iterations_ and returned a optimal lr of _7.05E-02_. Note that this learning rate is for  batch size of 128. For batch size of 512, optimal lr was found to be _1.46E-02_, but it didn't really gave me the results I was hoping for :(
![Steepest LR](/assets/images/SteepestLR.png)

* Implemented OneCycleLR with following parameters:
    - Epochs: _24_
    - Max at epoch: _5_
    - Steps per Epochs: len(trainloader) = _98_
    - Total steps : Epochs * Steps per epoch  = _2352_
    - pct_start: max_at_epoch/total_epochs = _5/24_
    - Division factor: 8
    - Final division factor: 1 (No annihlation)

    ![Learning rates vs epochs](/assets/images/LearningDistribution.png)
* Ran the model for 24 epochs. There were huge variations in training accuracy while the model was being trained
    ![Train test losses](/assets/images/train_test_val.png)
* At last, the ZigZag curve (Cyclic triangle plot)!

![Zig Zag Curve](/assets/images/Cyclic_Triangle_Plot.png)


---
## Future aspirations
* That 90% accuracy barrier with batch size as 512 !
* My gradcam is somehow not working for this model and gives me a weired error unrelated to real cause (that's what I think, I'm gonna correct that)
* I need to optimize the code I wrote for the model ! I could've coded it infinitely better, but couldn't :(
