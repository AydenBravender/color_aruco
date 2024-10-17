import unittest
import cv2
import numpy as np
from color_aruco.aruco_marker_detect import MarkerDetector
from color_aruco.aruco_marker_generator import GenerateArucoMarker

class TestDetectArucoMarker(unittest.TestCase):

    def setUp(self):
        self.detector = MarkerDetector()

    def test_count_even_numbers(self):
        test_list = [1, 4, 2, 5, 8, 3]
        result = self.detector.count_even_numbers(test_list)
        self.assertEqual(result, 3)

    def test_detect_marker(self):
        marker = GenerateArucoMarker(num=0, pixel_size=1)
        output_image = marker.create_aruco()

        result = self.detector.detect_marker(output_image)
        self.assertEqual(result[0][0], 0)

if __name__ == '__main__':
    unittest.main()
    