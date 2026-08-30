import cv2
capture = cv2.VideoCapture("test_vid_deltarune.mp4")

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    newRes = (width, height)
    newImg = cv2.resize(frame, newRes, interpolation=cv2.INTER_AREA) # add interpolation to smooth out the edges between pixels
    return newImg

while True:
    isTrue, frame = capture.read()
    frameResized = rescaleFrame(frame, 0.75)

    cv2.imshow("Video", frame)
    cv2.imshow("Video", frameResized)

    if cv2.waitKey(20) & 0xFF == ord('d'): # press d to exit the simulation
        break

capture.release()
cv2.destroyAllWindows()
