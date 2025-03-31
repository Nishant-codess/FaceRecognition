# FaceRecognition

## Description
FaceRecognition is a face detection and recognition system implemented using Python, OpenCV, and face_recognition library. This project is designed as a face recognition-based door lock system with a GUI built using Tkinter.

## Features
- Recognizes faces stored in the `images/` directory.
- Opens and closes the camera for face scanning.
- Displays detected faces with labels.
- UI built with Tkinter for ease of use.
- Supports multiple camera selections.

## Installation

### Prerequisites
Ensure you have Python installed on your system.

### Install Required Packages
Run the following command to install the necessary dependencies:
```bash
pip install face-recognition opencv-python numpy pillow tkinter
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/nishant-codess/FaceRecognition.git
cd FaceRecognition
```

2. Create an `images/` directory and add PNG images of faces you want to recognize.

3. Run the script:
```bash
python main.py
```

4. Use the GUI to open the camera and start recognizing faces.

## File Structure
```
FaceRecognition/
│-- images/                 # Folder to store known faces
│-- main.py # Main script
│-- README.md               # Project documentation
```

## Contributing
Feel free to fork this repository and improve upon it. Contributions are welcome!

## License
This project is open-source and available under the MIT License.

## Credits
Developed by **Nishant Ranjan & Nidhi Nayana**.
