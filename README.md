[![License CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC4.0-blue.svg)](https://raw.githubusercontent.com/NVIDIA/FastPhotoStyle/master/LICENSE.md)
![Python 2.7](https://img.shields.io/badge/python-2.7-green.svg)
![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)
## Japanese cartoon character generation using neural style transfer

### License

Copyright (C) 2019 NVIDIA Corporation.  All rights reserved.
Licensed under the CC BY-NC-SA 4.0 license (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). 



### Introduction
Anime-Comic-Game (ACG) subculture sustains a billion-pound industry and has mil- lions of fans around the world[1]. However, making of animations and cartoons is a tedious process that requires excessive amount of dedication and talent. In recent years, with the accelerating development of deep learninig techinique, convolutional neural network, generative adversarial network have achieved significant success in style transfer, which refers to the process of translate a natural image into artistic paintings. This image to image tranlation has been applied in a number of fields, in- cluding image segmentation, comic colourisation, text analysis. Nonetheless, there is still a great deal of untapped potential for deep learning in the ACG industry. The objective of this project is to develop a method for automatic ACG character creation using deep learning technique.

### GAN loss
[![nAztN6.md.jpg](https://s2.ax1x.com/2019/09/04/nAztN6.md.jpg)](https://imgchr.com/i/nAztN6)
[![nAzYAx.md.jpg](https://s2.ax1x.com/2019/09/04/nAzYAx.md.jpg)](https://imgchr.com/i/nAzYAx)


### Dataset
Anime faces: [https://www.thiswaifudoesnotexist.net/](https://www.thiswaifudoesnotexist.net/)

BitMoji: [https://google.github.io/cartoonset/index.html](https://google.github.io/cartoonset/index.html)

Manga: Manga109

### Pre-requisite

-   Python version : Python 3.5.2
    
-   Image processing library(read,write,save,crop) : Scikit-Image, OpenCV2, Pil-
    
    low, which mainly used in data preparation process
    
-   Module for webcrawl images : urllib.request, beautifulsoup4
    
-   Module for compressing/save/extract files : pickle
    
-   scientific computations : Numpy
    
-   Data visualization : matplotlib.pyplot
    
-   Face detection and facial landmark detection : Dlib
    
-   Machine learning libraries : Scikit-learn, scipy
    
-   Process the model’s configuration : yaml
    
-   Deep Learning library : Pytorch

All algorithms have been trained on imperial department of computing remote machine, which is Ubuntu 16.04 with graphicial processing unit supported. I trained on available NVIDIA GeForce GTX 1080 Ti graphics card on dc1218@ladybug.doc.ic.ac.uk.

### Code Usage
In my dissertation...


### Result preview

[![nAza9O.md.png](https://s2.ax1x.com/2019/09/04/nAza9O.md.png)](https://imgchr.com/i/nAza9O)
[![nAzN4K.md.png](https://s2.ax1x.com/2019/09/04/nAzN4K.md.png)](https://imgchr.com/i/nAzN4K)
[![nAzd3D.md.png](https://s2.ax1x.com/2019/09/04/nAzd3D.md.png)](https://imgchr.com/i/nAzd3D)

### Model Trained 
Best Model can be downloaded at : https://drive.google.com/open?id=1bPvwsrasF8vHfhTbRizJbeQei9j7nGne

Inception Model can be downloaded at: https://drive.google.com/open?id=1q_Wgs86e5ClsCYVJNVgagsGwAU2Xfd9B
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjI2NDIyMjM4LDYxNDEyMTQyMywzMTE3ND
YwNjQsMzc1MzI1ODQwXX0=
-->