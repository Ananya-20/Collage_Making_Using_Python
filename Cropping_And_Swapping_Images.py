import cv2
import numpy
In [2]:
photo1 = cv2.imread('redhat.png')
photo2 = cv2.imread('linux.jpg')
In [3]:
cv2.imshow('photo1', photo1)
cv2.imshow('photo2', photo2)
cv2.waitKey()
cv2.destroyAllWindows()
In [4]:
cphoto1 = photo1 [:,:150]
cphoto2 = photo2 [:,:160]
cv2.imshow('cphoto1', cphoto1)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('cphoto2', cphoto2)
cv2.waitKey()
cv2.destroyAllWindows()
photo1 [0:109,0:150] = cphoto2 [0:109,0:150]
cv2.imshow('swapped photo 1', photo1)
cv2.waitKey()
cv2.destroyAllWindows()
photo3 = cv2.imread('redhat.png')
photo4 = cv2.imread('linux.jpg')
cphoto3 = photo3 [:,:150]
cphoto4 = photo4 [:,:160]
cv2.imshow('cphoto3', cphoto3)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('cphoto4', cphoto4)
cv2.waitKey()
cv2.destroyAllWindows()
photo4 [0:109,0:150] = cphoto3 [0:,0:]
cv2.imshow('swapped photo 1', photo4)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('swapped photo 4',  cphoto4)
cv2.waitKey()
cv2.destroyAllWindows()