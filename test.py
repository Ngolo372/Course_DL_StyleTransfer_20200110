import os
from PIL import Image

img_fold = 'contents/test2017'

dir_list = os.listdir(img_fold)

print len(dir_list)

print dir_list[0:30]

dir_list.sort(key=lambda x: x)

num_list = []

print dir_list[4]

for idx in range(len(dir_list)):
    openPath = os.path.join(img_fold, dir_list[idx])
    try:
        img = Image.open(openPath)
    except:
        print 'failed'
        num_list.append(idx)

for item in num_list:
    openPath = os.path.join(img_fold, dir_list[item])
    os.remove(openPath)
