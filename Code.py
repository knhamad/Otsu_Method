import numpy as np
import matplotlib.pyplot as plt
import glob
import cv2          
from Model import Otsu
#Simply put your RGB images in the Data file and run the code. The segmented images will be saved as .npy in the Segmented_images folder.
for path in glob.glob(r'./Data/'+"*.png"):
    Segmented_img=Otsu.Otsu(path)
    np.save(r'./Segmented_images/'+str(path[7:-4]),Segmented_img)
