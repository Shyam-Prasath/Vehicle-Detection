# 🚗 Vehicle Detection using OpenCV

This project demonstrates real-time and static image-based vehicle detection using **OpenCV** and **Haar cascade classifiers**. It can detect **cars and buses** from both video files and image URLs.

---

## 🔍 Features

- Detect cars in video using Haar cascades.
- Detect cars and buses in static images from online URLs.
- Basic preprocessing using grayscale, blur, dilation, and morphological operations.
- Highlights detected vehicles with bounding boxes.
- Console output of total vehicles detected.

---

## 📁 Folder Structure

```bash
vehicle-detection/
├── carv.mp4                       # Sample video for car detection
├── cars.xml                       # Haar cascade for car detection
├── folder/
│   └── bus.xml                    # Haar cascade for bus detection
├── car_video_detection.py         # Detect cars from video
├── car_image_detection.py         # Detect cars from URL image
├── bus_image_detection.py         # Detect buses from URL image
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

---

## ⚙️ Requirements

Install Python packages with:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:
```text
opencv-python
pillow
numpy
requests
```

---

## 🚀 How to Run

### ▶️ Detect Cars in Video:
```bash
python car_video_detection.py
```

### 🖼️ Detect Cars in Image:
```bash
python car_image_detection.py
```

### 🚌 Detect Buses in Image:
```bash
python bus_image_detection.py
```

---

## 📸 Output

- Red rectangles on cars (video)
- Blue rectangles on cars/buses (images)
- Console prints total count of vehicles detected


