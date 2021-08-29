import os
import re
import cv2
import numpy as np
from tqdm import tqdm_notebook
import matplotlib.pyplot as plt


col_frames = os.listdir('D:/Machine Learning/laneTracking/test_videos/challenge.mp4')
col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

idx = 457

# plot frame
plt.figure(figsize=(10,10))
# plt.imshow(col_images[idx][:,:,0], cmap= 'gray')
plt.show()



'''
code by anEngineer-py
instagram.com/sbariskoksal
twitter.com/sbariskoksal
github.com/anengineer-py
'''