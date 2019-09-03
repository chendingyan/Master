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
![enter image description here](https://picasaweb.google.com/109592484409092847965/6732498200469472481#6732498205487171938)
![enter image description here](https://picasaweb.google.com/109592484409092847965/6732498322966803601#6732498323156758306)
![enter image description here](https://picasaweb.google.com/109592484409092847965/6732498466542821969#6732498472290306418)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0NTg5NjUzM119
-->