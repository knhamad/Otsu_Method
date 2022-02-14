import cv2          
import matplotlib.pyplot as plt
#from tensorflow.keras.preprocessing import image
# path to input image is specified and
# image is loaded with imread command
image = cv2.imread('Image_file')
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
Grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# applying Otsu thresholding
# as an extra flag in binary 
# thresholding     
ret, Segmented_img = cv2.threshold(Grey_img, 1, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)     
plt.imshow(Segmented_img)
plt.show()
