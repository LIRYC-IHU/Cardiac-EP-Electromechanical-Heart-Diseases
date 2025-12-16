# Lecture 1 : 2D signal processing

Title : TODO

Schedule : November 25, 2024 | 14:00-16:15 

Speaker: Valéry Ozenne

## Summary

- [Lecture 1 : 2D signal processing](#lecture-1--2d-signal-processing)
  - [Summary](#summary)
  - [Objectives](#objectives)
  - [Ressources](#ressources)
  - [PRe-requisites:](#pre-requisites)
  - [Exercice 1: apply a threshold](#exercice-1-apply-a-threshold)
  - [Exercice 2: make the convolution filter](#exercice-2-make-the-convolution-filter)
  - [Exercice 3: apply mulitple convolution filters](#exercice-3-apply-mulitple-convolution-filters)
  - [Exercice 4: apply again convolution filter](#exercice-4-apply-again-convolution-filter)
    - [To go further](#to-go-further)

## Objectives

* Being familiar with 2D convolution in image processing 
* Understanding the purposes and potential applications in computer vision such feature detection

## Ressources

## PRe-requisites:

* open this page [SAM](https://aidemos.meta.com/segment-anything/gallery), then read the relevant documentation [SAM documentation](https://docs.ultralytics.com/models/sam/)
  
## Exercice 1: apply a threshold

* open 3D Slicer then go to the download sample dataset tab and download the CTChest dataset
* go to the Save tool then save the volume in nifti format ('nii.gz')
  
```

import numpy as np
import nibabel as nib

# load the nifti
nifti=nib.load('/home/vozenne/Documents/CTChest.nii.gz')
# get the 3D volume in a multi-dimensional matrix
volume=nifti.get_fdata()

print(np.shape(volume))
# extract one slice
slice=volume[:,:,65]
slice_for_threshold=slice
```

then display the image with matplotlib


```
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(121)
plt.imshow(slice, cmap='gray')
```

extract min and max value and apply the threshold

```
print(np.min(slice_for_threshold.flatten()))
print(np.max(slice_for_threshold.flatten()))

Valeur seuil
seuil = -500

% Remplacer les éléments inférieurs à 5 par 99
slice_for_threshold[slice_for_threshold < seuil] = 0
plt.subplot(122)
plt.imshow(slice_for_threshold, cmap='gray')
```

## Exercice 2: make the convolution filter

Compute the convolution of the following image `I` with the following kernel `K`

```
import numpy as np

I=np.matrix([[3, 3, 2, 1, 0],[0,0,1,3,1],[3,1,2,2,3],[2,0,0,2,2], [2,0,0,0,1]])
K=np.matrix([[2,1,0],[0,2,2],[2,1,0]])
print("A =", A)
print("K =", K)

```

1) extract the dimension of I and K and name it
2) start with one position in I and apply K
3) then move the kernel in I
   


## Exercice 3: apply mulitple convolution filters

Compute the convolution of the following image `I` with the following kernels `H` for detecting edge, or corner.

```
import numpy as np
import matplotlib.pyplot as plt
B=np.zeros((12,12))
B[0,:]=1
B[1,:]=1
B[:,0]=1
B[:,1]=1
B[11,:]=1
B[11-1,:]=1
B[:,11]=1
B[:,11-1]=1
B[6,6]=1

# au choix
H=np.matrix([[1,1],[1,1]])*0.25  # identity
H=np.matrix([[1,-1],[1,-1]])*0.25 #??
H=np.matrix([[1,1],[-1,-1]])*0.25  #??
H=np.matrix([[1,0],[1,0]])*0.25  #??
H=np.matrix([[0,1],[0,1]])*0.25  #??

plt.figure(1)
plt.subplot(131)
plt.imshow(B)
plt.subplot(131)
plt.imshow(H)
```

## Exercice 4: apply again convolution filter

Load the astronaut image and apply a convolution filter with the fonction convolve2d to detect the edge.

```
import matplotlib.pyplot as plt
from skimage import data
import numpy as np
image = data.astronaut()
grey=image = data.astronaut().mean(-1) * 100 + 100
plt.figure(1)
plt.subplot(121)
plt.imshow(grey, cmap='gray')
print(np.shape(image))
```

### To go further

* [nice explanation](https://www.youtube.com/watch?v=2KMwRUd3hcM)
* [interactive website 1](https://bjbodner.github.io/dataScienceProjects/src/visualizations/interactive_conv2d.html)
* * [interactive website 2](https://poloclub.github.io/cnn-explainer/)
* https://wandb.ai/ayush-thakur/dl-question-bank/reports/Intuitive-understanding-of-1D-2D-and-3D-convolutions-in-convolutional-neural-networks---VmlldzoxOTk2MDA
