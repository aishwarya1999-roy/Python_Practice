import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog

class PenTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Canvas")

        # Set up canvas
        self.canvas = tk.Canvas(root, bg='black', width=800, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Set up initial pen settings
        self.pen_color = '#00FF00'
        self.pen_thickness = 2
        self.eraser_mode = False
        self.eraser_thickness = 20  # Thickness of the eraser tool

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.paint_or_erase)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Set up toolbar
        self.toolbar = tk.Frame(root, bg='gray')
        self.toolbar.pack(fill=tk.X)

        # Add color button
        self.color_button = tk.Button(self.toolbar, text="Color", command=self.change_color)
        self.color_button.pack(side=tk.LEFT)

        # Add thickness slider
        self.thickness_slider = tk.Scale(self.toolbar, from_=1, to=10, orient=tk.HORIZONTAL, label="Thickness")
        self.thickness_slider.set(self.pen_thickness)
        self.thickness_slider.pack(side=tk.LEFT)

        # Add erase button
        self.erase_button = tk.Button(self.toolbar, text="Eraser", command=self.toggle_eraser)
        self.erase_button.pack(side=tk.LEFT)

        # Add save button
        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save)
        self.save_button.pack(side=tk.LEFT)

        self.previous_x = None
        self.previous_y = None

    def paint_or_erase(self, event):
        if self.eraser_mode:
            self.erase_area(event)
        else:
            self.paint(event)

    def paint(self, event):
        pen_thickness = self.thickness_slider.get()
        if self.previous_x and self.previous_y:
            self.canvas.create_line(self.previous_x, self.previous_y, event.x, event.y, 
                                    width=pen_thickness, fill=self.pen_color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.previous_x = event.x
        self.previous_y = event.y

    def erase_area(self, event):
        x1, y1 = event.x - self.eraser_thickness, event.y - self.eraser_thickness
        x2, y2 = event.x + self.eraser_thickness, event.y + self.eraser_thickness
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='black', outline='black')

    def reset(self, event):
        self.previous_x, self.previous_y = None, None

    def change_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.erase_button.config(relief=tk.SUNKEN)
        else:
            self.erase_button.config(relief=tk.RAISED)

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.canvas.postscript(file=file_path + ".eps")
            try:
                from PIL import Image
                img = Image.open(file_path + ".eps")
                img.save(file_path, "png")
            except ImportError:
                print("Pillow module is not installed, install it by running 'pip install pillow'.")

if __name__ == "__main__":
    root = tk.Tk()
    pen_tool = PenTool(root)
    root.mainloop()
