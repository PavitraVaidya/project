# 🚗 Self-Driving Car Simulation
A 2D self-driving car simulation using Python and Pygame.
The car follows a predefined path smoothly while rotating towards its target points.

---

## ✨ Features
#### 🚗 Smooth car movement along a predefined path
#### 🔄 Car rotates naturally towards the target
#### 🎨 Visualized path and real-time car motion
#### 💻 Interactive simulation with Pygame
#### 🖼 Easy to replace car image with your own

---

## 📁 Project Structure
```bash
.
├── main.py                 # Main simulation code
├── car-removebg-preview.png # Car image
├── README.md               # Project documentation

```
---

## ⚙ Requirements
- Python 3.8+
- Pygame
- Math (built-in)


## Install dependencies:
```bash
pip install pygame
```
---

## 🏃 Usage
1. Make sure the car image (car-removebg-preview.png) is in the same folder as main.py.
2. Run the simulation:
```bash
python main.py
```
3. A window will open showing the car moving along the path.
4. Close the window or press X to exit.

---

## 🖼 How It Works
1. Car Image: Loaded and scaled using Pygame.
2. Path Points: A predefined list of (x, y) coordinates.
3. Car Rotation: The car rotates to face the next target using atan2.
4. Movement: Car moves towards the next target until reaching the end of the path.

---

## 🎨 Customization
- Replace car-removebg-preview.png with your own car image.
- Adjust path points in path = [(x1, y1), (x2, y2), ...].
- Change car speed with car_speed = 2.

---

## 📝 License
MIT License © 2025
You are free to use, modify, and distribute this project
