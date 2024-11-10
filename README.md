# Obstacle Detection using Pushbroom Algorithm in Python

This project demonstrates a basic obstacle detection system implemented in Python using OpenCV. The code utilizes a pushbroom-inspired algorithm to classify obstacles based on distance thresholds, identifying them as either "Highly Dangerous," "Less Dangerous," or "Safe."

## Features

- Detects obstacles within the camera's field of view.
- Estimates the distance of obstacles using a contour-based method.
- Classifies and labels obstacles based on their estimated distance.
- Real-time video display with labeled obstacles.

## Prerequisites

To run this project, you need:

- Python 3.x
- OpenCV library
- Numpy library

You can install the required libraries with:

 ```bash
pip install opencv-python numpy
```

## Code Explanation

### Parameters
- `DANGER_DISTANCE_THRESHOLD`: Threshold for marking an obstacle as highly dangerous.
- `SAFE_DISTANCE_THRESHOLD`: Maximum distance threshold for marking an obstacle as safe.

### Functions
- **estimate_distance**: A simple function that calculates a proxy distance based on the area of the detected contour. Adjust this method for more accurate distance calculations based on the camera's calibration.

### Main Code
1. **Camera Initialization**: Opens the default camera (usually webcam) for capturing video frames.
2. **Grayscale and Blurring**: Converts each frame to grayscale and applies Gaussian blurring to reduce noise.
3. **Edge Detection**: Detects edges in the frame using the Canny edge detection method.
4. **Contour Detection**: Finds contours in the edge-detected frame.
5. **Distance Calculation and Labeling**: For each contour, estimates distance and classifies the obstacle:
    - **Highly Dangerous**: Close distance; displayed in red.
    - **Less Dangerous**: Moderate distance; displayed in yellow.
    - **Safe**: Safe distance; displayed in green.
6. **Display**: Annotates and displays the labeled frame in real time.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/obstacle-detection-pushbroom.git
    ```
2. Run the script:
    ```bash
    python obstacle_detection.py
    ```

3. Press **q** to quit the display window.

