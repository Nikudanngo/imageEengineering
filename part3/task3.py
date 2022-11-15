# from google.colab.patches import cv2_imshow
import cv2
import numpy as np

img_src = cv2.imread('kadai-3/sampleimage_6.jpg')
h = img_src.shape[0] 
w = img_src.shape[1]

halfW = int(w/2)
halfH = int(h/2)

arr1Func = (288-32)*(10.97/23.77)/2
arr2Func = (280*(10.97/23.77))/2

arr1 = [[halfW - int(arr1Func), 20], 
        [halfW + int(arr1Func), 20],
        [halfW - int(arr1Func), 240], 
        [halfW + int(arr1Func), 240]]

arr2 = [[halfW + 150, int(halfH) - int(arr2Func)], 
        [halfW + 150, int(halfH) + int(arr2Func)], 
        [halfW - 140, int(halfH) - int(arr2Func)], 
        [halfW - 140, int(halfH) + int(arr2Func)]]


def toProjective(arr):
    cornerPoint = np.float32([[108, 31], [292, 31], [14, 228], [385, 228]])
    transformPoint = np.float32(arr)
    transformedMatrix = cv2.getPerspectiveTransform(cornerPoint, transformPoint)
    img_dst = cv2.warpPerspective(img_src, transformedMatrix, (w, h), flags=cv2.INTER_CUBIC)
    return img_dst


cv2.imwrite('kadai-3/projective1.jpg', toProjective(arr1))
cv2.imwrite('kadai-3/projective2.jpg', toProjective(arr2))
# cv2_imshow(toProjective(arr1))
# cv2_imshow(toProjective(arr2))
