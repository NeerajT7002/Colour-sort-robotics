# HSV–Based Visual Grasp Quality Estimation and Pick Verification Using a 4-DOF Robotic Arm

## Project Overview

This project presents a vision-guided robotic manipulation system that detects colored objects using computer vision and automatically picks them using a 4-DOF robotic arm. The system integrates real-time image processing with robotic control to demonstrate autonomous object detection, alignment, grasping, and lifting.

A smartphone camera is used as a live video stream through DroidCam, and the robotic arm is controlled using an Arduino Uno with servo motors. The project demonstrates how computer vision and robotics can work together to perform automated pick-and-place tasks.

Project Website:  
https://neerajt7002.github.io/Colour-sort-robotics/

---

## Features

- Real-time object detection using computer vision
- Autonomous robotic arm alignment toward detected objects
- Controlled grasping using a servo-based gripper
- Smooth servo motion for stable arm movement
- Automatic pick, lift, and release cycle
- Integration of Python, OpenCV, and Arduino control

---

## System Architecture

The system consists of three major components:

1. Vision System  
   Detects colored objects in real-time using OpenCV and HSV color segmentation.

2. Control System  
   Processes the detected object's position and calculates the required servo angles for alignment.

3. Robotic Manipulation System  
   Executes the movement of the robotic arm and performs object grasping using servo motors.

---

## Hardware Requirements

- Arduino Uno
- 4-DOF Robotic Arm with 4 Servo Motors
- USB Cable for Arduino
- Smartphone Camera (via DroidCam)
- Breadboard
- Jumper Wires
- External Webcam or Phone Camera

---

## Servo Configuration

| Servo | Pin | Function |
|------|------|------|
| Base | D3 | Horizontal rotation |
| Shoulder | D5 | Vertical arm movement |
| Elbow | D6 | Arm extension |
| Gripper | D9 | Object gripping |

---

## Software Requirements

- Python 3.x
- OpenCV
- NumPy
- PyFirmata2
- DroidCam

Install dependencies using:

```bash
pip install opencv-python numpy pyfirmata2
```

---

## Arduino Setup

1. Connect Arduino Uno to your computer.
2. Open Arduino IDE.
3. Upload **StandardFirmata** to the Arduino board.

Steps:
- Open Arduino IDE
- File → Examples → Firmata → StandardFirmata
- Upload the sketch to Arduino

This allows Python to control the servo motors directly.

---

## Camera Setup

1. Install DroidCam on your smartphone.
2. Connect the phone and computer to the same Wi-Fi network.
3. Launch DroidCam and note the IP address.
4. Update the camera URL in the Python code:

```
http://PHONE_IP:4747/video
```

Example:

```
http://10.180.42.234:4747/video
```

---

## Project Workflow

1. The camera captures real-time video of the workspace.
2. OpenCV processes the frames and detects red-colored objects.
3. The horizontal position of the object is mapped to the base servo angle.
4. When the object reaches the center of the frame, the robot initiates the grasp sequence.
5. The robotic arm lowers toward the object.
6. The gripper closes to hold the object.
7. The arm lifts the object and releases it.

---

## Key Technologies Used

- Computer Vision
- OpenCV Image Processing
- Arduino Hardware Control
- Python Robotics Integration
- HSV Color Segmentation
- Real-Time Servo Control

---

## Project Structure

```
Colour-sort-robotics
│
├── robot_control.py
├── README.md
├── documentation
│   └── project_report.pdf
└── images
    └── system_architecture.png
```

---

## Applications

- Industrial object sorting
- Warehouse automation
- Assistive robotics
- Educational robotics platforms
- Smart manufacturing systems

---

## Future Improvements

- Multi-color object sorting
- Object distance estimation
- Deep learning–based grasp detection
- Multi-object tracking
- Autonomous pick-and-place pipelines

---

## Author

Neeraj T

Project Repository  
https://neerajt7002.github.io/Colour-sort-robotics/

---

## License

This project is intended for educational and research purposes.
