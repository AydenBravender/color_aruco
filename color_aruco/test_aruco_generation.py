import unittest
import numpy as np
from aruco_marker_generator import GenerateArucoMarker

class TestGenerateArucoMarker(unittest.TestCase):

    def test_create_aruco_valid(self):
        marker = GenerateArucoMarker(num=10, pixel_size=10)
        output_image = marker.create_aruco()
        # Check if the output image is the correct shape
        self.assertEqual(output_image.shape, (70, 70, 3))  # 7x7 mini_array * pixel_size

    def test_create_aruco_invalid_number(self):
        with self.assertRaises(ValueError):
            marker = GenerateArucoMarker(num=1099511627775, pixel_size=10)
            marker.create_aruco()

    def test_create_aruco_invalid_number(self):
        with self.assertRaises(ValueError):
            marker = GenerateArucoMarker(num=-1, pixel_size=10)
            marker.create_aruco()

    def test_create_aruco_zero(self):
        marker = GenerateArucoMarker(num=0, pixel_size=1)
        output_image = marker.create_aruco()

        # Check if the borders are yellow
        top_border = output_image[0, :]
        bottom_border = output_image[-1, :]
        left_border = output_image[:, 0]
        right_border = output_image[:, -1]

        self.assertTrue(np.all(top_border == [0, 255, 255]), "Top border is not yellow.")
        self.assertTrue(np.all(bottom_border == [0, 255, 255]), "Bottom border is not yellow.")
        self.assertTrue(np.all(left_border == [0, 255, 255]), "Left border is not yellow.")
        self.assertTrue(np.all(right_border == [0, 255, 255]), "Right border is not yellow.")

    def test_aruco_2312(self):
        marker = GenerateArucoMarker(num=2312, pixel_size=1)
        output_image = marker.create_aruco()
        print(output_image.size)
        print(list(output_image))
        # self.assertEqual(output_image, 

# If running this file directly, run the tests
if __name__ == '__main__':
    unittest.main()
