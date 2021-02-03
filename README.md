# Assignment 8

> Submitted by Naman Shrimali
---

## Target
- Go through this repository: https://github.com/kuangliu/pytorch-cifar
- Extract the ResNet18 model from this repository and add it to your API/repo. 
- Use your data loader, model loading, train, and test code to train ResNet18 on Cifar10
- Your Target is 85% accuracy. No limit on the number of epochs. Use default ResNet18 code (so params are fixed). 
- Once done finish S8-Assignment-Solution.

## Submission
I have trained model, summary and observations and details can be found below.

## Results
- No of parameters: `11,173,962`
- No of epochs: 35
- Droupout: 10%
- First training accuracy: 24.5020%
- First validation accuracy: 37.12%
- Highest training accuracy: 99.5500% (Epoch 35)
- Highest validation accuracy: `87.65%` (Epoch 34) 
---
### Model
Resnet-18
```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 64, 32, 32]           1,728
       BatchNorm2d-2           [-1, 64, 32, 32]             128
            Conv2d-3           [-1, 64, 32, 32]          36,864
       BatchNorm2d-4           [-1, 64, 32, 32]             128
           Dropout-5           [-1, 64, 32, 32]               0
            Conv2d-6           [-1, 64, 32, 32]          36,864
       BatchNorm2d-7           [-1, 64, 32, 32]             128
           Dropout-8           [-1, 64, 32, 32]               0
        BasicBlock-9           [-1, 64, 32, 32]               0
           Conv2d-10           [-1, 64, 32, 32]          36,864
      BatchNorm2d-11           [-1, 64, 32, 32]             128
          Dropout-12           [-1, 64, 32, 32]               0
           Conv2d-13           [-1, 64, 32, 32]          36,864
      BatchNorm2d-14           [-1, 64, 32, 32]             128
          Dropout-15           [-1, 64, 32, 32]               0
       BasicBlock-16           [-1, 64, 32, 32]               0
           Conv2d-17          [-1, 128, 16, 16]          73,728
      BatchNorm2d-18          [-1, 128, 16, 16]             256
          Dropout-19          [-1, 128, 16, 16]               0
           Conv2d-20          [-1, 128, 16, 16]         147,456
      BatchNorm2d-21          [-1, 128, 16, 16]             256
          Dropout-22          [-1, 128, 16, 16]               0
           Conv2d-23          [-1, 128, 16, 16]           8,192
      BatchNorm2d-24          [-1, 128, 16, 16]             256
          Dropout-25          [-1, 128, 16, 16]               0
       BasicBlock-26          [-1, 128, 16, 16]               0
           Conv2d-27          [-1, 128, 16, 16]         147,456
      BatchNorm2d-28          [-1, 128, 16, 16]             256
          Dropout-29          [-1, 128, 16, 16]               0
           Conv2d-30          [-1, 128, 16, 16]         147,456
      BatchNorm2d-31          [-1, 128, 16, 16]             256
          Dropout-32          [-1, 128, 16, 16]               0
       BasicBlock-33          [-1, 128, 16, 16]               0
           Conv2d-34            [-1, 256, 8, 8]         294,912
      BatchNorm2d-35            [-1, 256, 8, 8]             512
          Dropout-36            [-1, 256, 8, 8]               0
           Conv2d-37            [-1, 256, 8, 8]         589,824
      BatchNorm2d-38            [-1, 256, 8, 8]             512
          Dropout-39            [-1, 256, 8, 8]               0
           Conv2d-40            [-1, 256, 8, 8]          32,768
      BatchNorm2d-41            [-1, 256, 8, 8]             512
          Dropout-42            [-1, 256, 8, 8]               0
       BasicBlock-43            [-1, 256, 8, 8]               0
           Conv2d-44            [-1, 256, 8, 8]         589,824
      BatchNorm2d-45            [-1, 256, 8, 8]             512
          Dropout-46            [-1, 256, 8, 8]               0
           Conv2d-47            [-1, 256, 8, 8]         589,824
      BatchNorm2d-48            [-1, 256, 8, 8]             512
          Dropout-49            [-1, 256, 8, 8]               0
       BasicBlock-50            [-1, 256, 8, 8]               0
           Conv2d-51            [-1, 512, 4, 4]       1,179,648
      BatchNorm2d-52            [-1, 512, 4, 4]           1,024
          Dropout-53            [-1, 512, 4, 4]               0
           Conv2d-54            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-55            [-1, 512, 4, 4]           1,024
          Dropout-56            [-1, 512, 4, 4]               0
           Conv2d-57            [-1, 512, 4, 4]         131,072
      BatchNorm2d-58            [-1, 512, 4, 4]           1,024
          Dropout-59            [-1, 512, 4, 4]               0
       BasicBlock-60            [-1, 512, 4, 4]               0
           Conv2d-61            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-62            [-1, 512, 4, 4]           1,024
          Dropout-63            [-1, 512, 4, 4]               0
           Conv2d-64            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-65            [-1, 512, 4, 4]           1,024
          Dropout-66            [-1, 512, 4, 4]               0
       BasicBlock-67            [-1, 512, 4, 4]               0
           Linear-68                   [-1, 10]           5,130
================================================================
Total params: 11,173,962
Trainable params: 11,173,962
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.01
Forward/backward pass size (MB): 15.44
Params size (MB): 42.63
Estimated Total Size (MB): 58.07
----------------------------------------------------------------
```
---
## Observations
* Model is highly overfitting (Model is too heavy !)
* Since high overfitting was observed, dropout of 10% had to be coded, which bumped up the highest validation accuracy to 87.65%, but still lead to overfitting
* The loss was negative, so had to modify the model to add log_softmax of the output as the return value
* Learning rate of 0.2, with a scheduler introduced with gamma of 0.5 and step size of 8 was introduced
---
## Future Aspirations
* More image augumentations !!!
---

