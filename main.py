import cv2 as cv
from cvzone import HandTrackingModule
import ctypes

# Initialize the webcam
cap = cv.VideoCapture(0)

# Initialize the hand detector
detector = HandTrackingModule.HandDetector()

while True:
    # Read a frame from the webcam
    ret, img = cap.read()

    # Detect hands in the frame
    hands, img = detector.findHands(img)

    # Display the frame with detected hands
    cv.imshow("Hands Detected", img)

    # Check each detected hand
    for hand in hands:
        # If all fingers are down
        if detector.fingersUp(hand) == [0, 0, 0, 0, 0]:
            # Lock the workstation
            ctypes.windll.user32.LockWorkStation()

    # Break the loop if 'x' is pressed
    if cv.waitKey(1) == ord('x'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
