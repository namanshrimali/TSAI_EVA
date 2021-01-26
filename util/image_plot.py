import matplotlib.pyplot as plt
import torchvision
import numpy as np


def plot_images(images, classes, labels, total= 5):
    images = images/2 + 0.5 #un-normalize
    plt.figure(figsize=(30, 30))

    for image_num in range(total):
        plt.subplot(15, 15, image_num+1)
        plt.imshow(np.transpose(images[image_num], (1, 2, 0)))
        plt.title(classes[labels[image_num]])