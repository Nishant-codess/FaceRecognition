import face_recognition
import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import Label, Button, ttk
from PIL import Image, ImageTk

def load_known_faces():
    known_face_encodings = []
    known_face_names = []
    image_folder = "images/"
    
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(filename.split('.')[0])
    
    return known_face_encodings, known_face_names

known_face_encodings, known_face_names = load_known_faces()
video_capture = None
selected_camera = 0
running = False

def open_camera():
    global video_capture, selected_camera, running
    video_capture = cv2.VideoCapture(selected_camera)
    running = True
    scan_face()

def close_camera():
    global video_capture, running
    running = False
    if video_capture:
        video_capture.release()
        video_capture = None
        access_label.config(text="Camera Closed")
        person_name_label.config(text="Name: None")

def scan_face():
    global access_label, person_name_label, canvas, video_capture, running
    if not video_capture or not running:
        return
    
    ret, frame = video_capture.read()
    if not ret:
        access_label.config(text="Camera Error")
        return
    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    recognized = "No"
    recognized_name = "Unknown"
    
    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        
        if True in matches:
            recognized = "Yes"
            match_index = matches.index(True)
            recognized_name = known_face_names[match_index]
            
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, recognized_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            break
        else:
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
    access_label.config(text=f"Recognized: {recognized}", fg="green" if recognized == "Yes" else "red")
    person_name_label.config(text=f"Name: {recognized_name}", fg="cyan" if recognized == "Yes" else "yellow")
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
    canvas.image = imgtk
    
    if running:
        canvas.after(10, scan_face)

def select_camera(event):
    global selected_camera
    selected_camera = int(camera_selection.get())

app = tk.Tk()
app.title("Face Detection using OpenCV")
app.geometry("900x600")
app.configure(bg="#121212")

title_label = Label(app, text="FaceDetection", font=("Arial", 18, "bold"), fg="cyan", bg="#121212")
title_label.pack(pady=10)

status_frame = tk.Frame(app, bg="#121212")
status_frame.pack(pady=5)

access_label = Label(status_frame, text="Access: Waiting...", font=("Arial", 16, "bold"), fg="white", bg="#121212")
access_label.grid(row=0, column=0, padx=10)

person_name_label = Label(status_frame, text="Name: None", font=("Arial", 16, "bold"), fg="white", bg="#121212")
person_name_label.grid(row=0, column=1, padx=10)

canvas = tk.Canvas(app, width=640, height=360, bg="black", highlightthickness=2, highlightbackground="white")
canvas.pack(pady=10)

camera_selection_label = Label(app, text="Select Camera:", font=("Arial", 12), fg="white", bg="#121212")
camera_selection_label.pack()

camera_selection = ttk.Combobox(app, values=["0 (Main Camera)", "1 (External Camera)"], state="readonly")
camera_selection.current(0)
camera_selection.pack()
camera_selection.bind("<<ComboboxSelected>>", select_camera)

button_frame = tk.Frame(app, bg="#121212")
button_frame.pack(pady=10)

open_camera_button = Button(button_frame, text="Open Camera", font=("Arial", 12), bg="#00cc66", fg="white", width=15, command=open_camera)
open_camera_button.grid(row=0, column=0, padx=5)

close_camera_button = Button(button_frame, text="Close Camera", font=("Arial", 12), bg="#ff4444", fg="white", width=15, command=close_camera)
close_camera_button.grid(row=0, column=1, padx=5)

scan_button = Button(button_frame, text="Scan Again", font=("Arial", 12), bg="#0099ff", fg="white", width=15, command=scan_face)
scan_button.grid(row=0, column=2, padx=5)

footer_label = Label(app, text="Made with ❤️ by Nishant Ranjan & Nidhi Nayana", font=("Arial", 12), fg="orange", bg="#121212")
footer_label.pack(side=tk.BOTTOM, pady=10)

app.mainloop()