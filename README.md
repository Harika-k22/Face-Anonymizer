Face Blur System (Image, Video & Webcam):A simple computer vision project using OpenCV that detects
and blurs human faces in:Images,Videos,Live Webcam

---

##Features

* Detects faces using Haar Cascade Classifier
* Applies Gaussian blur to hide identities
* Works on image, video, and real-time webcam
* Saves processed video output
* Easy menu-based interface

---

## Technologies Used

* Python
* OpenCV

---

## Project Structure

```
project-folder/
│
├── main.py
├── haarcascade_frontalface_default.xml
├── harika_pic.jpg
├── input.mp4
└── output.mp4 (generated)
```

---


## How It Works

1. Converts input frame to grayscale
2. Uses Haar Cascade XML model to detect faces
3. Extracts face regions
4. Applies Gaussian blur
5. Replaces original face with blurred version

---

## Key Components

### Haar Cascade XML File

* Pre-trained face detection model
* Contains patterns of facial features
* Enables detection without deep learning

### blur_faces() Function

* Core processing function
* Works on a single frame
* Reused for image, video, and webcam

---

## Output

* Image: Displays blurred result
* Video: Saves as `output.mp4`
* Webcam: Real-time blurred feed

