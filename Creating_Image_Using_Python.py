import cv2
import numpy as np
photo=np.zeros([500,1000,3],dtype=np.uint8)
photo2=cv2.circle(photo,(350,150), 50,[255,0,0],3 )

photo2=cv2.circle(photo,(450,150), 50,[255,0,0],3 )
photo2=cv2.circle(photo,(550,150), 50,[255,0,0],3 )

photo2=cv2.circle(photo,(400,240), 50,[0,0,255],3 )
photo2=cv2.circle(photo,(500,240), 50,[0,0,255],3 )

photo2=cv2.circle(photo,(450,333), 50,[0,255,0],2 )

cv2.imshow("image",photo2)
cv2.waitKey()
cv2.destroyAllWindows()

