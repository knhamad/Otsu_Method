import cv2          
import matplotlib.pyplot as plt

def Otsu(file):
    image = cv2.imread(file)
    Grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, Segmented_img = cv2.threshold(Grey_img, 1, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    Segmented_img[Segmented_img==255]=1     
    plt.imshow(Segmented_img)
    plt.show()
    return Segmented_img
