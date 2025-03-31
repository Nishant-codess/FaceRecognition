# FaceLock - Face Recognition Door Lock System

A Python application that uses facial recognition to control access, simulating a door lock system. The application detects faces through a camera and matches them against a database of known faces to grant or deny access.

## Features

- Real-time face detection and recognition
- User-friendly GUI built with Tkinter
- Support for multiple cameras
- Visual feedback with face highlighting
- Display of recognized person's name
- Configurable recognition tolerance

## Prerequisites

- Python 3.9+ (recommended, may have compatibility issues with Python 3.12)
- Webcam or camera device

## Installation

1. Clone this repository or download the files:
```
git clone <repository-url>
```

2. Install the required dependencies:
```
pip install opencv-python
pip install numpy
pip install face_recognition
pip install pillow
```

Note: The `face_recognition` library depends on `dlib`, which may require additional setup on some systems. If you encounter issues, consider using a Python virtual environment with Python 3.9.

## Setup

1. Create an "images" folder in the same directory as the main.py file
2. Add reference face images to the "images" folder:
   - Use PNG format for all images
   - Name each file with the person's name (e.g., "John.png")
   - Ensure each image contains only one clear face
   - For best results, use well-lit, front-facing photos

## Usage

1. Run the application:
```
python main.py
```

2. Select your camera from the dropdown menu (default is the main camera)

3. Click "Open Camera" to start the face recognition system

4. The system will:
   - Display "Access: Yes" and the person's name in green when a recognized face is detected
   - Display "Access: No" in red for unrecognized faces
   - Highlight recognized faces in green with their name
   - Highlight unrecognized faces in red

5. Click "Close Camera" to stop the camera feed

6. Click "Scan Again" to manually trigger a new scan

## Customization

- Adjust the recognition tolerance in the `scan_face()` function:
  ```python
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
  ```
  Lower values (e.g., 0.4) make recognition more strict, higher values (e.g., 0.6) make it more lenient.

- Modify the UI colors and layout in the Tkinter setup section

## Troubleshooting

- **Camera not working**: Verify your camera is properly connected and not being used by another application
- **No faces detected**: Ensure proper lighting and camera positioning
- **False recognitions**: Adjust the tolerance value or provide better reference images
- **Installation issues**: Try using Python 3.9 or 3.10 instead of newer versions

## Authors

Made with ❤️ by Nishant Ranjan & Nidhi Nayana

## License

This project is licensed under the MIT License - see the LICENSE file for details
