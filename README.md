# Finger Tracker

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-orange)](https://google.github.io/mediapipe/solutions/hands)

A lightweight, real-time fingertip tracking tool built with Python, OpenCV, and MediaPipe. Detects hand landmarks and displays live `(x, y)` coordinates for each fingertip directly on your webcam feed.

##  Features
- Detects and tracks up to 2 hands simultaneously
- Renders a real-time hand skeleton with 21 landmark points
-  Shows live pixel coordinates for every fingertip
-  Optimized inference pipeline for smooth, high-FPS performance
-  Plug-and-play: works with built-in and external USB webcams

##  Requirements
- Python 3.8 or higher
- `opencv-python`
- `mediapipe`

## 🚀 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/finger-tracker.git
   cd finger-tracker
2. nstall dependencies
   ```bash
   pip install -r requirements.txt
3. Run the application
   ```bash
   python main.py
