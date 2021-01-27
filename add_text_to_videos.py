import cv2
import datetime

# select video from default camera
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

# show video on frame
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height: '+ str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
