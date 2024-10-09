import numpy as np
import cv2

class DetectArucoMarkers:
    """
    A class to detct colored ArUco markers.

    Attributes:
        image: 

    Methods:
        detect_aruco(): detects the ArUco marker and returns an array.
    """
    def __init__(self, image):
        self.image = image

    def detect_aruco(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


     
