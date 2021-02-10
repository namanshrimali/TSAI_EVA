# Assignment - 10
> Submitted by Naman Shrimali
---

## Target
* Pick your last code
* Make sure  to Add CutOut to your code. It should come from your transformations (albumentations)
* Use this repo: https://github.com/davidtvs/pytorch-lr-finder
    * Move LR Finder code to your modules
    * Implement LR Finder (for SGD, not for ADAM)
    * Implement ReduceLROnPlatea: https://pytorch.org/docs/stable/optim.html#torch.optim.lr_scheduler.ReduceLROnPlateau
* Find best LR to train your model
* Use SDG with Momentum
* Train for 50 Epochs. 
* Show Training and Test Accuracy curves
* Target 88% Accuracy.
* Run GradCAM on the any 25 misclassified images. Make sure you mention what is the prediction and what was the ground truth label.
* Submit

## Submission
I have trained the model for 50 epochs, with optimal leraning rate (calculated through lr finder) of **4.10E-01** and summary, graphs, gradcam reports for misclassified images, observations and details can be found below. I've made a seperate library - [simplif-ai](https://github.com/namanshrimali/simplif-ai) (pronounced simplifai, or simplify) -  for the boilerplate codes that can be used effectively everywhere !

## Results 
* No of parameters: 11,173,962
* No of epochs: `50`
* Droupout: 10%
* First training accuracy: 14.4800%
* First validation accuracy: 18.29%
* Highest training accuracy: 88.9680%
* **Highest validation accuracy: 90.42%**
* The validation accuracy settled around 90% in the final epochs
---

### Model
```
================================================================
Model: Resnet-18
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
* Added middle man augumentations (cutout + 10% dropout + ChannelDropout + GridDistortion + RandomCrop + HorizontalFlip) 
* The optimal learning rate came out to be 4.10E-01. This learning rate, with SGD optimizer and scheduler as ReduceLROnPlateu managed to train the model with slight underfitting 
* The model crossed 90% threshold (yay !)

## Visual Analysis
### Misclassified Images and their gradcam reports
![Misclassified Images](assets/images/misclassified_gradcam.png)


## Future Aspirations
* Idk ! 😭
![Noooo !](https://tenor.com/T64d.gif)