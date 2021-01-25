import cv2

img = cv2.imread('left06.jpg', -1)
print(img)

# read image
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('left06_copy.png', img)
    cv2.destroyAllWindows()
else:
    print('not esc')

