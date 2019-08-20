import cv2 as cv
import os
path = '/Users/mikechen/bitmoji'
files= os.listdir(path) #得到文件夹下的所有文件名称
path_save = "/Users/mikechen/bitmoji_1/"
for f in files:
    im = cv.imread(path + '/' + f)
    if im is not None:
        rgbImage = cv.cvtColor(im, cv.COLOR_RGBA2RGB)
        print(im.shape)
        cv.imwrite(path_save + f[:-4] + ".jpg", rgbImage)
