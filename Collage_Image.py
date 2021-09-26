import cv2
import numpy
image1 = cv2.imread('elonmusk.jpg')
image2 = cv2.imread('doge.jpg')
image1 = image1 [:, 0:262]
cv2.imshow('image1', image1)
cv2.waitKey()
cv2.destroyAllWindows()
image2 = image2 [0:180,:]
cv2.imshow('image2', image2)
cv2.waitKey()
cv2.destroyAllWindows()
image = cv2.hconcat([image1,image2])
cv2.imshow('collage', image)
cv2.waitKey()
cv2.destroyAllWindows()
