import cv2
import numpy as np

def generate_aruco_marker(marker_id, marker_size=200):
    # Define the dictionary of ArUco markers
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    # Generate the marker image
    marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
    
    # Draw the marker
    marker_image = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)

    return marker_image

def save_marker_image(marker_image, marker_id):
    filename = f"aruco_marker_{marker_id}.png"
    cv2.imwrite(filename, marker_image)
    print(f"Saved marker {marker_id} as {filename}")

def main():
    num_markers = 1  # Number of markers to generate

    for marker_id in range(num_markers):
        marker_image = generate_aruco_marker(marker_id)
        save_marker_image(marker_image, marker_id)

if __name__ == "__main__":
    main()
