import cv2

bite = cv2.imread("bite.jpg")
cv2.imshow("origin", bite)

lowThreshold = 50
edge_bite = cv2.Canny(bite, lowThreshold, 3 * lowThreshold)
print(edge_bite)

cv2.waitKey(0)
cv2.destroyAllWindows()


def isBite(image):
    edge_test = cv2.Canny(image, lowThreshold, 3 * lowThreshold)

    if 2 > 1:
        return True
    else:
        return False
