import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('c3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#灰度图像
#open to see how to use: cv2.Canny
#http://blog.csdn.net/on2way/article/details/46851451
edges = cv2.Canny(gray, 200, 300)
plt.subplot(121), plt.imshow(edges, 'gray')
plt.xticks([]), plt.yticks([])
#hough transform
#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, minLineLength=150, maxLineGap=20)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, minLineLength=300, maxLineGap=150)
#img = cv2.imread('c3.jpg')
lines1 = lines[:, 0, :]#提取为二维
for x1, y1, x2, y2 in lines1[:]:
    if (abs(x2-x1) > 0):
        if ((abs(y2-y1)/abs(x2-x1)) > 0.5):
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)
            cv2.putText(img, str((y2-y1)/(x2-x1))[0:5], (x2, y2), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 0), 2)
            print((abs(y2-y1)/abs(x2-x1)))

plt.subplot(122), plt.imshow(img,)
plt.xticks([]), plt.yticks([])
#plt.show()
cv2.namedWindow("lane", 0)
cv2.imshow("lane", img)
cv2.imwrite("c3_post.jpg", img)
cv2.waitKey()
