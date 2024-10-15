import cv2
import numpy as np

cap = cv2.VideoCapture(2)

while True:
    _, frame = cap.read()
    
    # Convert the BGR color space of the image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Threshold of yellow in HSV space
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Prepare the mask to overlay
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Apply bitwise-and operation to keep yellow regions
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Apply Canny edge detection
    edges = cv2.Canny(mask, 100, 200)
    
    # Hough line detection parameters
    threshold = 100
    minLineLength = 50
    maxLineGap = 20
    lines = cv2.HoughLinesP(mask, 1, np.pi / 360, threshold, minLineLength, maxLineGap)
    
    # Draw lines
    linear = np.zeros_like(mask)
    if lines is not None:
        for [line] in lines:
            x1, y1, x2, y2 = line
            cv2.line(linear, (x1, y1), (x2, y2), 255, 1)
        
        # Get bounds of white pixels
        white = np.where(linear == 255)
        
        # Ensure that white pixels were detected
        if white[0].size > 0:
            xmin, ymin, xmax, ymax = np.min(white[1]), np.min(white[0]), np.max(white[1]), np.max(white[0])
            
            # Check if more than one object is detected by ensuring bounds are reasonable
            if (xmax - xmin > 5) and (ymax - ymin > 5):
                # Crop the image within bounds
                crop = frame[ymin:ymax, xmin:xmax]
                
                # Resize the crop to 7x7
                resized_crop = cv2.resize(crop, (7, 7))
                
                # Show the upscaled image to visualize the resized crop
                upscaled_image = cv2.resize(resized_crop, (200, 200), interpolation=cv2.INTER_NEAREST)
                
                # Display the upscaled image
                cv2.imshow("Upscaled Image", upscaled_image)
        else:
            # No object detected; clear the window if open
            cv2.imshow("Upscaled Image", np.zeros((200, 200, 3), dtype=np.uint8))
    else:
        # No lines detected; clear the window if open
        cv2.imshow("Upscaled Image", np.zeros((200, 200, 3), dtype=np.uint8))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
