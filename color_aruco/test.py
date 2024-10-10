import numpy as np
import cv2
# from tensorflow.keras.preprocessing import image

image = cv2.imread('20241009_091818.png')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 0], dtype="uint8")
upper = np.array([90, 90, 90], dtype="uint8")
mask = cv2.inRange(image, lower, upper)

cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cv2.fillPoly(mask, cnts, (255,255,255))
result = cv2.bitwise_and(original,original,mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()


img = mask
cv2.imwrite('savedimage.png', img)
img = cv2.imread('savedimage.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img = cv2.medianBlur(img,5)
l, w = img.shape
img_area = l*w

thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours detected:", len(contours))

for cnt in contours:
   area = cv2.contourArea(cnt)
   if area > 1000 and (area+5000 < img_area or area-5000 > img_area):     
      print(area)
      x1,y1 = cnt[0][0]
      approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
      if len(approx) == 4:
         x, y, w, h = cv2.boundingRect(cnt)
         ratio = float(w)/h
         if ratio >= 0.9 and ratio <= 1.1:
            img = cv2.drawContours(image, [cnt], -1, (0,255,255), 3)
            cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()