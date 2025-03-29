import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

GRAVITY = 9.81

class MyCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.my_fig, self.my_ax = plt.subplots(figsize=(6, 4), dpi=100)
        super().__init__(self.my_fig)
        self.setParent(parent)

        self.my_ax.set_xlabel("X")
        self.my_ax.set_ylabel("Y")
        self.my_ax.grid(True)

    def draw_trajectory(self, speed, angle_deg):
        self.my_ax.clear()
        self.my_ax.set_xlabel("X")
        self.my_ax.set_ylabel("Y")
        self.my_ax.grid(True)

        angle_rad = np.deg2rad(angle_deg)
        flight_time = 2 * speed * np.sin(angle_rad) / GRAVITY
        t = np.linspace(0, flight_time, 100)
        x = speed * np.cos(angle_rad) * t
        y = speed * np.sin(angle_rad) * t - 0.5 * GRAVITY * t**2

        self.my_ax.plot(x, y, label="траектория")
        self.my_ax.legend()
        self.draw()
