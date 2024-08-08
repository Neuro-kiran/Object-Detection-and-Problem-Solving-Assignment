#!/usr/bin/env python
# coding: utf-8

# # Task 2: Object Shape Analysis

# Enhance your existing code from Task 1 to include object shape
# analysis. Your program should be able to:
# ● Detect objects based on color as in Task 1.
# ● Apply appropriate image processing techniques to isolate individual objects.
# ● Analyze the shape of each object and classify it into one of the following categories:
# ○ Circle, Square, Triangle, or Irregular shape.
# ● Display the detected objects with their respective shape classifications.

# In[ ]:


import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
cv2.namedWindow('Frame')

# Create trackbars for color change
cv2.createTrackbar('LH', 'Frame', 0, 179, nothing)
cv2.createTrackbar('LS', 'Frame', 0, 255, nothing)
cv2.createTrackbar('LV', 'Frame', 0, 255, nothing)
cv2.createTrackbar('UH', 'Frame', 179, 179, nothing)
cv2.createTrackbar('US', 'Frame', 255, 255, nothing)
cv2.createTrackbar('UV', 'Frame', 255, 255, nothing)

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get current positions of the trackbars
    l_h = cv2.getTrackbarPos('LH', 'Frame')
    l_s = cv2.getTrackbarPos('LS', 'Frame')
    l_v = cv2.getTrackbarPos('LV', 'Frame')
    u_h = cv2.getTrackbarPos('UH', 'Frame')
    u_s = cv2.getTrackbarPos('US', 'Frame')
    u_v = cv2.getTrackbarPos('UV', 'Frame')
    
    # Define the HSV range for color detection
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])
    
    # Create a mask
    mask = cv2.inRange(hsv, lower_range, upper_range)
    
    # Reduce noise in the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter out small contours
            # Get the bounding box
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw the bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Shape analysis
            approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
            shape_name = "Irregular"
            if len(approx) == 3:
                shape_name = "Triangle"
            elif len(approx) == 4:
                # Use aspect ratio to distinguish between square and rectangle
                aspect_ratio = float(w) / h
                if 0.95 <= aspect_ratio <= 1.05:
                    shape_name = "Square"
                else:
                    shape_name = "Rectangle"
            elif len(approx) > 4:
                shape_name = "Circle"
            
            # Display shape name
            cv2.putText(frame, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()


# Thanks for visiting

# In[ ]:




