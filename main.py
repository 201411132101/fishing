import cv2.cv2
import uiautomator2 as u2
import cv2

d = u2.connect()  # connect to device

image = d.screenshot(format='opencv')
cv2.imwrite("test.jpg", image)

cv2.waitKey(0)