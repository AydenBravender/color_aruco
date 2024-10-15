import unittest
import numpy as np
from color_aruco.aruco_marker_generator import GenerateArucoMarker

class TestGenerateArucoMarker(unittest.TestCase):

    def test_create_aruco_valid(self):
        marker = GenerateArucoMarker(num=10, pixel_size=10)
        output_image = marker.create_aruco()
        # Check if the output image is the correct shape
        self.assertEqual(output_image.shape, (70, 70, 3))  # 7x7 mini_array * pixel_size

    def test_create_aruco_invalid_number(self):
        with self.assertRaises(ValueError):
            marker = GenerateArucoMarker(num=95367431640625, pixel_size=10)
            marker.create_aruco()

    def test_create_aruco_invalid_number(self):
        with self.assertRaises(ValueError):
            marker = GenerateArucoMarker(num=-1, pixel_size=10)
            marker.create_aruco()

    def test_create_aruco_zero(self):
        marker = GenerateArucoMarker(num=0, pixel_size=1)
        output_image = marker.create_aruco()

        # Check if the borders are white
        top_border = output_image[0, :]
        bottom_border = output_image[-1, :]
        left_border = output_image[:, 0]
        right_border = output_image[:, -1]

        self.assertTrue(np.all(top_border == [0, 255, 255]), "Top border is not black.")
        self.assertTrue(np.all(bottom_border == [0, 255, 255]), "Bottom border is not black.")
        self.assertTrue(np.all(left_border == [0, 255, 255]), "Left border is not black.")
        self.assertTrue(np.all(right_border == [0, 255, 255]), "Right border is not black.")

# If running this file directly, run the tests
if __name__ == '__main__':
    unittest.main()
