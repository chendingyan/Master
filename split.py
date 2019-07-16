import os
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import ToTensor, Resize, Compose
from PIL import Image
from sklearn.model_selection import train_test_split
import random, shutil

class ImageFolderSplitter:
    # images should be placed in folders like:
    # --root
    # ----root\dogs
    # ----root\dogs\image1.png
    # ----root\dogs\image2.png
    # ----root\cats
    # ----root\cats\image1.png
    # ----root\cats\image2.png
    # path: the root of the image folder
    def __init__(self, path, train_size=0.8):
        self.path = path
        self.train_size = train_size
        self.data_x_path = []
        self.x_train = []
        self.x_valid = []
        for root, dirs, files in os.walk(path):
            print(len(files))
            if len(files) > 1 and len(dirs) == 0:
                for file1 in files:
                    self.data_x_path.append(file1)
            else:
                raise RuntimeError("please check the folder structure!")
        self.x_train, self.x_valid = train_test_split(self.data_x_path,shuffle=True,train_size=self.train_size, test_size= 0.2)

    def getTrainingDataset(self):
        return self.x_train

    def getValidationDataset(self):
        return self.x_valid


class DatasetFromFilename(Dataset):
    # x: a list of image file full path
    def __init__(self, x, y, transforms=None):
        super(DatasetFromFilename, self).__init__()
        self.x = x
        self.y = y
        if transforms == None:
            self.transforms = ToTensor()
        else:
            self.transforms = transforms

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        img = Image.open(self.x[idx])
        img = img.convert("RGB")
        return self.transforms(img), torch.tensor([[self.y[idx]]])

# test code
old_dir = '/Users/mikechen/bitmoji'
splitter = ImageFolderSplitter(old_dir)
transforms = Compose([ToTensor()])
x_train = splitter.getTrainingDataset()
print(len(x_train))
print(x_train[0])
x_test = splitter.getValidationDataset()
print(len(x_test))
# shutil.copyfile
new_dir = '/Users/mikechen/moji/trainB'
for pic in x_train:
    old = old_dir+'/'+pic
    new = new_dir+'/'+pic
    shutil.copyfile(old,new)

new_dir = '/Users/mikechen/moji/testB'
for pic in x_test:
    old = old_dir+'/'+pic
    new = new_dir+'/'+pic
    shutil.copyfile(old,new)

