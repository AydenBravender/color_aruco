import numpy as np
import cv2
class GenerateArucoMarker:
    """
    A class to generate ArUco markers based on a given number.

    Attributes:
        num (int): The number to convert to a marker.
        pixel_size (int): The size of each pixel in the output image.

    Methods:
        create_aruco(): Generates the ArUco marker and returns it as an image array.
    """

    def __init__(self, num, pixel_size):
        """
        Initializes the GenerateArucoMarker with the given number and pixel size.

        Parameters:
            num (int): The number to convert to a marker.
            pixel_size (int): The size of each pixel in the output image.
        """
        self.num = num
        self.pixel_size = pixel_size

    def create_aruco(self):
        """
        Generates the ArUco marker based on the initialized number and pixel size.

        Returns:
            np.ndarray: An image array of the generated ArUco marker.
        """

        base5 = 0
        if self.num == 0:
            base5 = 0

        if self.num < 95367431640624 and self.num >= 0:
            base5_digits = []
            
            # Convert number to base 5
            while self.num > 0:
                remainder = self.num % 5
                base5_digits.append(remainder)  # Store as integer
                self.num = self.num // 5
            
            base5_digits.reverse()
            
            # Pad the list to 20 digits with 0s
            while len(base5_digits) < 20:
                base5_digits.insert(0, 0)

        else:
            raise ValueError("Number is too large for base 5 conversion within the allowed range")
        
        # Split the list into 4 lists of 5 elements each
        split_lists = [base5_digits[i:i+5] for i in range(0, len(base5_digits), 5)]

        # Count the number of even elements in each list
        even_counts = [sum(1 for num1 in sublist if num1 % 2 == 0) for sublist in split_lists]

        for i in range(len(even_counts) - 1, -1, -1):
            if even_counts[i] % 2 == 0:
                base5_digits.insert(i * 5 + 5, 0)
            elif even_counts[i] % 2 == 1:
                base5_digits.insert(i * 5 + 5, 1)

        base5_digits.insert(0, 5)

        # Create a 7x7 array with zeros (for a border)
        mini_array = np.zeros((7, 7), dtype=int)

        for row in range(1, 6):  # Rows 1 to 5
            for col in range(1, 6):  # Columns 1 to 5
                mini_array[row, col] = base5_digits[(row - 1) * 5 + (col - 1)]  # Calculate the index for flat list

        # Create an output image with specified pixel size
        output_image = np.zeros((mini_array.shape[0] * self.pixel_size, mini_array.shape[1] * self.pixel_size, 3), dtype=np.uint8)

        # Assign colors based on the mini_array values
        color_map = {
            0: (0, 0, 0),       # black
            1: (255, 255, 255), # white
            2: (0, 255, 0),     # red
            3: (0, 0, 255),     # green
            4: (255, 0, 0),     # blue
            5: (0, 255, 255)    # yellow
        }

        for r in range(mini_array.shape[0]):
            for c in range(mini_array.shape[1]):
                color_value = color_map[mini_array[r, c]]
                output_image[r * self.pixel_size:(r + 1) * self.pixel_size, c * self.pixel_size:(c + 1) * self.pixel_size] = color_value
        
        return output_image

# Example usage:
if __name__ == "__main__":
    marker_id = 0  # Example marker ID
    pixel_size = 1  # Example pixel size for saving the image
    marker = GenerateArucoMarker(marker_id, pixel_size)
    # cv2.imwrite(f'aruco_marker_0.png', marker.create_aruco())
    print(marker.create_aruco())

    
