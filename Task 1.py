#!/usr/bin/env python
# coding: utf-8

# # Task 1: Color-Based Object Detection

# Write a Python script using OpenCV to perform
# color-based object detection. Your program should be able to:
# ● Capture frames from a video or webcam.
# ● Allow the user to select a specific color range (e.g., red, blue, green).
# ● Detect objects in the specified color range using image processing techniques.
# ● Display the detected objects in real-time using bounding boxes or other appropriate
# visualizations.

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




