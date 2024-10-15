import cv2 
import numpy as np 

cap = cv2.VideoCapture(0) 

while True: 
   _, frame = cap.read() 
   # It converts the BGR color space of image to HSV color space 
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

   # Threshold of blue in HSV space 
   lower_yellow = np.array([20, 100, 100]) 
   upper_yellow = np.array([30, 255, 255]) 

   # preparing the mask to overlay 
   mask = cv2.inRange(hsv, lower_yellow, upper_yellow) 

   # The black region in the mask has the value of 0, 
   # so when multiplied with original image removes all non-blue regions 
   result = cv2.bitwise_and(frame, frame, mask = mask) 

   cv2.imshow('frame', frame) 
   cv2.imshow('mask', mask)  	

   # apply canny edge detection
   edges = cv2.Canny(mask, 100, 200)

   # get hough line segments
   threshold = 100
   minLineLength = 50
   maxLineGap = 20
   lines = cv2.HoughLinesP(mask, 1, np.pi/360, threshold, minLineLength, maxLineGap)
   # draw lines
   linear = np.zeros_like(mask)
   if lines is not None:
      for [line] in lines:
         #print(line)
         x1 = line[0]
         y1 = line[1]
         x2 = line[2]
         y2 = line[3]
         cv2.line(linear, (x1,y1), (x2,y2), (255), 1)
   
      # get bounds of white pixels
      white = np.where(linear==255)
      xmin, ymin, xmax, ymax = np.min(white[1]), np.min(white[0]), np.max(white[1]), np.max(white[0])
      #print(xmin,xmax,ymin,ymax)

      # draw bounding box on input
      bounds = frame.copy()
      cv2.rectangle(bounds, (xmin,ymin), (xmax,ymax), (0,0,255))

      crop = frame[ymin:ymax, xmin:xmax]

      cv2.imshow("edges", edges)
      cv2.imshow("lines", linear)
      cv2.imshow("bounds", bounds)
   
      print(crop)
      a = crop
      a = np.arange(crop.size)
      b_size = 7
      print('a =', a)
      # bl = a.size // b_size
      # l + r = b_size
      # l * (bl + 1) + r * bl = a_size
      # l = a_size - b_size * bl
      bl = a.size // b_size
      l = a.size - b_size * bl
      r = b_size - l
      print('a_size =', a.size, 'b_size =', b_size, 'left =', l,
         'right =', r, 'block_left =', bl + 1, 'block_right =', bl)
      assert l * (bl + 1) + r * bl == a.size
      al, ar = a[:l * (bl + 1)], a[l * (bl + 1):]
      al = al.reshape(l, bl + 1)
      ar = ar.reshape(r, bl)
      b = np.concatenate((al.mean(axis = 1), ar.mean(axis = 1)))
      print('b =', b)

   cv2.waitKey(0) 


   cv2.destroyAllWindows() 
   cap.release() 
