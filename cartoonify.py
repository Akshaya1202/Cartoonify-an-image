import cv2

img = cv2.imread("tomato.jpg")

down_width = 300
down_height = 300
down_points = (down_width, down_height)

img = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
outlines = cv2.adaptiveThreshold(gray, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 11)

color = cv2.bilateralFilter(img, 5, 255, 255)
cartoon = cv2.bitwise_and(color, color, mask=outlines)

cv2.imshow("Original Image", img)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

