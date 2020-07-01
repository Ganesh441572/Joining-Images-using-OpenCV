import numpy as np
import cv2
from stackImagesFunction import stackImages
# reading the images
img = cv2.imread('Images to join/ronaldo.jpg')
img2 = cv2.imread('Images to join/ronaldoBrazil.jpg')
img3 = cv2.imread('Images to join/ronaldinho.jpg')
img4 = cv2.imread('Images to join/messi.jpg')
img5 = cv2.imread('Images to join/zidan.jpg')
img6 = cv2.imread('Images to join/henry.png')

#resizing the images
Img = cv2.resize(img , (500,500))
Img2 = cv2.resize(img2 , (500,500))
Img3 = cv2.resize(img3 , (500,500))
Img4 = cv2.resize(img4 , (500,500))
Img5 = cv2.resize(img5 , (500,500))
Img6 = cv2.resize(img6 , (500,500))
# method that stacks images in horizontal way
imgStack = stackImages(0.5, ([Img, Img2, Img3], [Img4, Img5, Img6])) # the array dimensions should be equal
cv2.imshow("ImageStack", imgStack)
cv2.waitKey(0)
