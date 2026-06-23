# FaceSnap

A simple Python OpenCV project that detects faces in real-time using a webcam and automatically captures and saves the detected face.

## Features

- Real-time face detection
- Face counting
- Automatic face image saving
- Cropped face preview window
- Haar Cascade Classifier based detection

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier

## Requirements

- Python 3.x
- OpenCV

Install OpenCV:


Files Required:
* haarcascade_frontalface_default.xml
* main.py
How It Works:
* Opens the webcam.
* Detects faces in each frame.
* Draws a rectangle around detected faces.
* Crops and saves the detected face as face.jpg.
* Displays the live video feed and captured face image.
Controls:
* Press Q to quit the application.
Output:
* Live webcam feed with face detection.
* Saved face image (face.jpg).
* Face count displayed on the screen.

```bash
pip install opencv-python
