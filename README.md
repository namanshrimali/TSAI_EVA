# Assignment 4 Submission

> Submitted by Naman Shrimali

## Target
* 99.4 validation accuracy in at-least on epoch
* Less than 20k parameters
* Less than 20 epochs
* No Fully Connected Layer
* To learn how to add different things into model (eg. BatchNorm, Dropouts, etc)

## What worked
* To keep number of parameters in check, no of channels were kept 16 and below
* Every Convolution layer were added with Batch Normalization and Dropouts
  - Batchnorm normalizes the images of complete batch to ur channels hence features can be  clearly found in the images
  - Dropout is a very lazy and brutal way of removing some % age of nodes, hence has a regularization effect on the model, when some primary nodes are dropped, it forces other nodes to train to improve the accuracy
* Did not used `Fully Connected Layers`, thus keeping the number of parameters in check
* Used `Ant-Man` which helped with following:
  - Lesser computation requirement for reducing the number of channels 
  - Use of existing channels to create complex channels (instead of re-convolution)
* Used Relu activation function into model for effective and easier decision making.
* Didn't use any Flatten layer hence no spatial information was lost in code
* Used Global Average Pooling of 2x2

## What didn't worked
* Using 4 layers in the network. While the parameters were kept in check, the network was only able to achieve the highest training accuracy of `99.35%` (almost had it !)
* Expand and squeeze model in every layer (Only worked on the first layer)
* 10%, 20%, 25%, 40% of Drop-outs
* 4.7k parameters, using Expand and Squeeze in every layer, had highest training accuracy of `99.17%` (Not bad for 4.7k parameters though, right ?)
* Keeping the Learning Rate low (tried with 0.001, 0.003, 0.005, 0.008), was able to achieve highest training accuracy of `99.35%`
* Using BatchNormalization before non-linearity (as was suggested in the BatchNorm research paper), but opposite worked. If you know why this happened, please let me know too.

## Final Model
I achieved `99.4%` accuracy with ~18k, ~12k and ~10k (9,954 to be exact) parameters. I'm highlighting the model which used lowest amounts of parameter. You can find other models (failures and successes).
The model with 10k parameters was only able to achieve 99.4% accuracy once (at the 18th epoch) (It got lucky)

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
```

```
EPOCH : 18

loss=0.024853497743606567 batch_id=468: 100%|██████████| 469/469 [00:13<00:00, 35.24it/s]

\Train set: Accuracy: 59284/60000 (98.8067%)


  0%|          | 0/469 [00:00<?, ?it/s]


Test set: Average loss: 0.0198, Accuracy: 9940/10000 (99.40%)
```

## What's next
* Model with 4.7k parameters got pretty close to the required accuracy, will work on that. It's always better to get the same results from less number of parameters
* As per kaggle, the highest accuracy for the MNIST dataset is 99.6% - 99.8% (impossible to achieve beyond 99.8%). I'll try to achieve a stable accuracy beyond 99.4%


