# QR Code Authentication

## Overview

The QR Code Authentication project aims to develop a secure and efficient access control system using QR codes. By leveraging computer vision techniques, the system scans, decodes, and verifies QR codes in real-time to grant or deny access based on an authorized list.

## Features

- **Object Detection**: Identifies QR code patterns within the webcam feed using computer vision algorithms.
- **QR Code Decoding**: Extracts and interprets QR code data from the detected regions.
- **Authentication Verification**: Validates the decoded QR code against an authorized list to determine access status.
- **Real-time Feedback**: Provides instant audio notifications and updates the user interface with authentication results.

## Methodology

### Object Detection

In the QR Code Authentication system, object detection is crucial for locating and isolating QR code patterns within the webcam feed. The system utilizes computer vision algorithms to scan video frames and identify potential QR code regions based on their unique square patterns.

### QR Code Decoding and Verification

After detecting the QR code regions, the system refines and processes them to extract the encoded data. This decoded data is then validated against a predefined list of authorized QR codes to determine authentication status.

## Requirements

### Hardware

- Webcam or built-in camera capable of high-resolution video capture
- Modern PC or laptop with a decent CPU and GPU for real-time processing

### Software

- Compatible with Windows 10, macOS Big Sur, or Ubuntu 20.04 LTS
- Python-supported coding environments (e.g., Visual Studio Code, Spyder)
- Key Libraries: OpenCV, NumPy, Pyzbar, Tkinter, Pygame

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/QRCodeAuthentication.git
   ```

2. Install required Python libraries:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory:

   ```
   cd QRCodeAuthentication
   ```

2. Run the main.py file:

   ```
   python main.py
   ```

3. Follow the on-screen instructions to interact with the QR Code Authentication system.

