import os

import shutil

path = '/Users/mikechen/Downloads/cartoonset100k/0'
new_path = '/Users/mikechen/bitmoji'
count = 0
for root, dirs, files in os.walk(path):
    if len(dirs) == 0:
        for file in files:
            if file.endswith('.png'):
                print file
                count +=1
                old = path +'/'+file
                new = new_path + '/' + str(count) +'.png'
                print (old, new)
                shutil.copyfile(old, new)

