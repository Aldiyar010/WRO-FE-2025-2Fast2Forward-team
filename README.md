# WRO-FE-2025-2Fast2Forward-team
Welcome to the official repository of **Team 2Fast2Forward** from Kazakhstan, participants of the **World Robot Olympiad (WRO) Future Engineers 2025**.This repository contains all engineering documentation, source code, and media related to the development of our autonomous EV3-based vehicle. 
## Team members: Malikuly Aldiyar, Nurlanov Dzhalil

![preview2](https://github.com/user-attachments/assets/a29509b0-afce-4198-8052-537fa538f86d)

## Project Overview

Our mission is to design and build a compact, fast, and intelligent autonomous vehicle capable of:

- Following a marked path
- Avoiding obstacles using real-time computer vision
- Autonomously driving using sensor and control algorithms

**Core Technologies:**
- LEGO MINDSTORMS EV3 brick & motors
- Pixy2 Camera (connected directly to EV3 via cable)
- Color, ultrasonic, and gyro sensors
- PID-controlled movement

## Technical Summary

### Drive & Chassis

- Chassis dimensions: **230 × 190 × 200 mm**
- 1 × Medium motors for drive, 1 × Medium motor for steering
- Rear large wheels for better speed and tight turns
- Lightweight front wheel steering system
  ## Why medium motors?
- EV3 Medium Motor
![m motor](https://github.com/user-attachments/assets/19fe0448-3ddf-4de9-929a-c16c0d89444e)

Power (Torque): ~8 N·cm (Newton centimeters). 
Speed: ~240 RPM (rotations per minute). 
Size/Weight: Smaller and lighter. 

- EV3 Large Motor
![l motor](https://github.com/user-attachments/assets/d86e9a87-0c56-4965-ab5f-10c92d2f1292)

Power (Torque): ~20 N·cm. 
Speed: ~160 RPM. 
Size/Weight: Larger and heavier.

- Summary:

Medium Motor: Faster but less powerful
Large Motor: More powerful but slower
Each motor is better for different purposes however we use Medium Motor for speed and precision that is vital characteristics for steering mechanism and avoiding obstacles.
![Compare](https://github.com/user-attachments/assets/f507339e-7dce-4c3c-ac42-29122630327d)

## Power management

In our robot we use EV3 lithium battery which is:
1. Rechargeable – Can be recharged hundreds of times, saving money and reducing waste compared to disposable AA batteries.
2. Stable voltage – Provides a consistent 7.4V output, which ensures stable performance of motors and sensors.

3. High capacity (2200mAh) – Offers longer operating time than 6 AA batteries, especially under heavy load.

4. Lighter weight – Weighs less than 6 AA batteries with a battery holder, reducing the robot’s total weight and improving mobility.

5. No need to remove – Charges directly in the EV3 brick via the AC charger, no need to take the battery out.

6. Better for competitions – Provides reliable and predictable performance, which is important during long runs or matches.

7. Environmentally friendly – Reduces the use of disposable batteries.
- Thus, the EV3 lithium-ion battery is a more efficient, lighter, and cost-effective power source for serious robot projects.
![Akkum](https://github.com/user-attachments/assets/00a34278-78ce-4b32-a8b1-bfac66677113)

### Sensor System

- **Color sensor** – detects path direction (orange/blue)
- **Ultrasonic sensor** – wall distance
- **Gyro sensor** – ensures straight-line movement with PID controller
- **Pixy2 camera** – recognizes red and green objects during the obstacle round

### Photos of robot
![photo1](https://github.com/user-attachments/assets/88275ad2-432f-4e03-a3fd-e1ecc41c92a8)
![photo3](https://github.com/user-attachments/assets/c06869b0-6ebe-4701-b5a8-91e420653d27)
![photo2](https://github.com/user-attachments/assets/53c9a823-8810-4864-bd32-61579632f31f)
![photo4](https://github.com/user-attachments/assets/8ff3bd48-07a2-4f93-8a78-e4a726ca3f4b)
![photo5](https://github.com/user-attachments/assets/488bd7d0-920f-470d-a573-8f7b915256e4)
![photo6](https://github.com/user-attachments/assets/41b5eede-4352-4352-9438-da3a8381cb4e)

## Open Challenge
![{25555357-B112-4AEB-A130-E63DFD27DE6F}](https://github.com/user-attachments/assets/1131fb5d-a43f-4af9-b7d4-89e1067f62b9)
1. The robot moves forward and uses an ultrasonic sensor to follow the wall at a distance of 61 cm (with proportional steering).

2. A color sensor checks for black — if black is detected:
- Wait 2 seconds
- Play a sound
- Set variable line = line + 1

3. The screen shows the current value of line every second.

4. If line == 12, the robot:
- Drives for 1 second and stops
Plays the "Kung Fu" sound
## Link to YouTube: https://youtu.be/lYeoIkNUopo?si=VNAsNOlTND-y97Hu
## Pseudo code: https://github.com/Aldiyar010/WRO-FE-2025-2Fast2Forward-team/blob/main/Pseudo%20code.py
## Obstacle Avoidance Logic

- Pixy2 camera detects red (right) and green (left) obstacle markers
- Detected positions are logged
- Programm decides where to turn and robot turns in correct direction.

## Team photo
![Team photo](https://github.com/user-attachments/assets/e525b1ea-c73b-4389-8844-296973a7db4d)
