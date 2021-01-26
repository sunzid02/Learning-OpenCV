import numpy as np
import cv2

# img = cv2.imread('left06.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line( img, (0, 0), (255, 255), (255, 0, 0), 5 )
img = cv2.arrowedLine(img, (0,255), (255, 255), (255, 0, 0), 10 )

# draw rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

# draw circle
img = cv2.circle(img, (447, 63), 63, (0,255,0), -1 )

# put text
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img, 'OpenCv', (10, 400), font, 4, (0, 255, 255), 10, cv2.LINE_AA )

# output
cv2.imshow('image', img)

# wait for the closing event
cv2.waitKey(0)
cv2.destroyAllWindows()