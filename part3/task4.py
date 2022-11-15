# from google.colab.patches import cv2_imshow
import cv2
import numpy as np

imgBlue = cv2.imread("kadai-3/chroma_blue.jpg")
imgBackground = cv2.imread("kadai-3/chroma_back2.jpg")
hsv = cv2.cvtColor(imgBlue, cv2.COLOR_BGR2HSV)
imgBinary = ~cv2.inRange(hsv, (10, 120, 0), (255, 255, 255))

element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
imgErode = cv2.erode(imgBinary, element, iterations=1)
imgDilate = cv2.dilate(imgErode, element, iterations=1)
contours, _ = cv2.findContours(imgDilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = max(contours, key=lambda x: cv2.contourArea(x))
mask = np.zeros_like(imgDilate)
cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
w = min(imgBlue.shape[1], imgBackground.shape[1])
h = min(imgBlue.shape[0], imgBackground.shape[0])

fgRoi = imgBlue[:h, :w]
bgRoi = imgBackground[:h, :w]

dst = np.where(mask[:h, :w, np.newaxis] == 0, bgRoi, fgRoi)

cv2.imwrite("kadai-3/chroma_back3.jpg", dst)

# cv2_imshow(img_1)
# cv2_imshow(img_2)
# cv2_imshow(dst)