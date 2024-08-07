# Object Detection and Problem Solving Assignment

## Introduction
This assignment demonstrates object detection using OpenCV, focusing on color-based object detection, shape analysis, and angle calculation. The project is divided into three tasks:

1. **Color-Based Object Detection**
2. **Object Shape Analysis**
3. **Object Angle Calculation**

## Tasks

### Task 1: Color-Based Object Detection
This task involves detecting objects based on a specified color range. The program:
- Captures frames from a video or webcam.
- Allows the user to select a color range using trackbars.
- Detects objects in the specified color range.
- Displays the detected objects in real-time using bounding boxes.

### Task 2: Object Shape Analysis
This task extends Task 1 by adding shape analysis. The program:
- Detects objects based on color.
- Isolates individual objects using image processing techniques.
- Analyzes the shape of each object and classifies it into one of the following categories: Circle, Square, Rectangle, Triangle, or Irregular shape.
- Displays the detected objects with their respective shape classifications.

### Task 3: Object Angle Calculation
This task further extends Task 2 by including angle calculation. The program:
- Detects objects based on color.
- Isolates individual objects and analyzes their shapes.
- Calculates the angle of each detected object with respect to a reference axis (horizontal).
- Displays the detected objects with their shape classifications and angles.

## Approach
### Color-Based Object Detection
1. **Capture Frames**: Use OpenCV to capture frames from the webcam.
2. **Color Range Selection**: Use trackbars to dynamically select the HSV color range.
3. **Color Detection**: Convert frames to HSV, create a mask based on the selected range, and find contours in the mask.
4. **Bounding Boxes**: Draw bounding boxes around detected objects.

### Object Shape Analysis
1. **Contour Detection**: Detect contours in the mask.
2. **Shape Approximation**: Approximate the contour shape using `cv2.approxPolyDP`.
3. **Shape Classification**: Classify shapes based on the number of vertices and aspect ratio.
4. **Display Shapes**: Label each object with its shape classification.

### Object Angle Calculation
1. **Min Area Rectangle**: Calculate the minimum area rectangle for each contour using `cv2.minAreaRect`.
2. **Angle Calculation**: Extract the angle of the rectangle.
3. **Display Angles**: Label each object with its shape classification and angle.

## Challenges Faced
1. **Real-Time Processing**: Ensuring real-time detection and display without significant lag.
2. **Shape Classification**: Accurate classification of shapes, especially distinguishing between squares and rectangles.
3. **Angle Calculation**: Calculating and displaying angles correctly in real-time.

## Assumptions
1. The input will be from a live webcam feed.
2. The user will manually select the color range using the provided trackbars.

## How to Run the Code
1. Install the required dependencies:
    ```bash
    pip install opencv-python
    ```
2. Run the Python script:
    ```bash
    python object_detection.py
    ```
3. Adjust the HSV trackbars to select the desired color range.

## Demonstration
- **Screenshots**: Include screenshots of the application detecting and classifying objects.
- **Video**: Provide a short video demonstrating the functionality.

## Directory Structure
