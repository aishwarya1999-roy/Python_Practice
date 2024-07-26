import tkinter as tk
from tkinter import colorchooser, filedialog
import pyautogui
import threading
import time
import win32api
import win32con
import win32gui

class PenTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Pen Tool Settings")
        self.pen_color = 'black'
        self.pen_thickness = 5
        self.drawing = False
        self.eraser_mode = False

        # Create UI components
        self.color_button = tk.Button(root, text="Select Color", command=self.select_color)
        self.color_button.pack(pady=10)

        self.thickness_slider = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, label="Pen Thickness")
        self.thickness_slider.set(self.pen_thickness)
        self.thickness_slider.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Drawing", command=self.start_drawing)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Drawing", command=self.stop_drawing)
        self.stop_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Drawing", command=self.save_drawing)
        self.save_button.pack(pady=10)

        self.eraser_button = tk.Button(root, text="Toggle Eraser", command=self.toggle_eraser)
        self.eraser_button.pack(pady=10)

        self.screenshot = None

    def select_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_button.config(text="Eraser On")
        else:
            self.eraser_button.config(text="Toggle Eraser")

    def start_drawing(self):
        self.drawing = True
        self.screenshot = pyautogui.screenshot()
        self.drawing_thread = threading.Thread(target=self.draw)
        self.drawing_thread.start()

    def stop_drawing(self):
        self.drawing = False
        if self.drawing_thread.is_alive():
            self.drawing_thread.join()

    def draw(self):
        previous_x = None
        previous_y = None
        hdc = win32gui.GetDC(0)
        
        pen_color = 'white' if self.eraser_mode else self.pen_color
        pen = win32gui.CreatePen(win32con.PS_SOLID, self.pen_thickness, win32api.RGB(
            int(pen_color[1:3], 16), 
            int(pen_color[3:5], 16), 
            int(pen_color[5:7], 16)
        ))
        win32gui.SelectObject(hdc, pen)

        while self.drawing:
            if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:  # Left mouse button is pressed
                x, y = pyautogui.position()
                if previous_x is not None and previous_y is not None:
                    win32gui.MoveToEx(hdc, previous_x, previous_y)
                    win32gui.LineTo(hdc, x, y)
                previous_x = x
                previous_y = y
            else:
                previous_x = None
                previous_y = None
            time.sleep(0.01)

        win32gui.ReleaseDC(0, hdc)

    def save_drawing(self):
        if self.screenshot:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.screenshot.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = PenTool(root)
    root.mainloop()
