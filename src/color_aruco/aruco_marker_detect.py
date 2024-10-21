import cv2
import numpy as np

class MarkerDetector:
    def __init__(self):
        """ A class to detct colored ArUco markers."""
        # Define color mappings
        self.colors = {
            0: (0, 0, 0),       # black
            1: (255, 255, 255), # white
            2: (255, 0, 0),     # blue
            3: (0, 0, 255),     # red
            4: (0, 255, 255)    # yellow
        }

    def count_even_numbers(self, lst):
        """counts even numbers in a list

        Args:
            lst (List): input list to parse through

        Returns:
           int: int number for number of even numbers
        """
        return len([num for num in lst if num % 2 == 0])


    def detect_marker(self, frame):
        """Detects color_aruco markers.

        Args:
            frame (array): Array of an image.

        Returns:
            list: List of IDs and bounding boxes of detected markers.
        """
        # Convert the BGR color space of the image to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold for detecting yellow in HSV
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        # Create mask for yellow areas
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Find contours of all yellow areas
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        detected_markers = []  # List to hold detected markers' IDs and bounding boxes

        # Iterate over each detected contour
        for contour in contours:
            # Approximate the contour to a polygon
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # Check if the polygon has four vertices (indicating a rectangle/square)
            if len(approx) == 4:
                # Get bounding box for the contour
                x, y, w, h = cv2.boundingRect(approx)

                # Only process if the bounding box is large enough
                if w > 5 and h > 5:
                    crop = frame[y:y+h, x:x+w]
                    resized_crop = cv2.resize(crop, (7, 7))
                    output = self.process_marker(resized_crop)

                    # If the marker is valid, calculate and store the marker ID and coordinates
                    if output:
                        base10_number = self.calculate_marker_id(output)
                        if base10_number is not None:
                            detected_markers.append((base10_number, (x, y, x+w, y+h)))

        return detected_markers


    def process_marker(self, resized_crop):
        """Process the 7x7 grid of pixels and return the marker's binary output."""
        output = []
        for i in range(7):
            row = []
            for j in range(7):
                r1, g1, b1 = map(float, resized_crop[i][j])

                # Calculate distances to predefined colors
                distance = []
                for k in range(5):
                    r2, g2, b2 = self.colors[k]
                    dist = (((r2 - r1) * 0.3) ** 2 + ((g2 - g1) * 0.59) ** 2 + ((b2 - b1) * 0.11) ** 2) ** 0.5
                    distance.append(dist)

                closest_color_index = distance.index(min(distance))
                row.append(closest_color_index)
            output.append(row)

        # Flatten the output and process it
        flattened_output = [color for row in output for color in row]
        while 4 in flattened_output:
            flattened_output.remove(4)

        if len(flattened_output) == 25:
            return flattened_output[1:]  # Remove top-left corner (yellow)
        return None

    def calculate_marker_id(self, results):
        """Calculate the marker ID based on the processed binary results."""
        parity = []

        for i in range(5, len(results), 6):
            parity.append(results[i])

        results = [item for i, item in enumerate(results) if (i + 1) % 6 != 0]

        x = 0
        list_1, list_2, list_3, list_4 = results[:5], results[5:10], results[10:15], results[15:20]

        # Apply the parity check function to each sublist
        result_parity = [self.count_even_numbers(lst) for lst in [list_1, list_2, list_3, list_4]]

        # Sum parity with the removed sixth items
        for a, b in zip(result_parity, parity):
            if (a + b) % 2 == 0:
                x += 1

        if x == 4:
            base4_number = ''.join(map(str, results))
            return int(base4_number, 4)  # Convert base 4 number to base 10
        return None
