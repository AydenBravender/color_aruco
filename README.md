# Color ArUco

**Color ArUco** is a Python package designed for detecting colored ArUco markers using OpenCV. This package includes functionality for capturing video from a webcam, detecting markers in real-time, and generating ArUco markers for various applications. Its primary purpose is to significantly increase the amount of data that can be transmitted via an ArUco marker. With the ability to encode over 1 trillion bits of data, it can transmit nearly a billion times more information compared to a standard ArUco marker.

## Features

- Detect colored ArUco markers in real-time from webcam footage.
- Draw bounding boxes around detected markers with their IDs.
- Generate ArUco markers with customizable parameters.

## Installation

To install the package via pip, you can use the following command:

```bash
pip install color_aruco
```
## Requirements
This package depends on the following libraries:

- ```numpy```
- ```opencv-python```
- ```opencv-contrib-python```

## Usage

### Detecting Markers
To use the marker detector with your webcam, you can run the following code:
```bash
import cv2
from color_aruco.aruco_marker_detect import MarkerDetector

def main():
    # Initialize marker detector
    detector = MarkerDetector()

    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Pass the frame to the marker detector
        markers = detector.detect_marker(frame)

        # Iterate over all detected markers and draw their bounding boxes and IDs
        for marker_id, bbox in markers:
            xmin, ymin, xmax, ymax = bbox
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {marker_id}", (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Show the frame
        cv2.imshow("frame", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

### Generating ArUco Markers
You can also generate ArUco markers using the ```GenerateArucoMarker``` class:
```bash
from color_aruco.aruco_marker_generator import GenerateArucoMarker
import cv2

# Example usage:
if __name__ == "__main__":
    marker_id = 1099511627774  # Example marker ID
    pixel_size = 100  # Example pixel size for saving the image
    marker = GenerateArucoMarker(marker_id, pixel_size)
    cv2.imwrite('aruco_marker_0.png', marker.create_aruco())
```

## Running Tests
To ensure everything is working correctly, you can run the unit ```tests``` provided in the tests folder:
```bash
python -m unittest discover tests
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or create an issue if you encounter any bugs or have feature requests.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/AydenBravender/color_aruco/blob/main/LICENSE) file for details.
