from math import pi
# №1, №2
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def calculate_area(self):
        return pi * self.r * 2

    def print_circle(self):
        print(f"Circle: (x={self.x}, y={self.y}, r={self.r})")


circle1 = Circle(10, 20, 50)
circle2 = Circle(80, 90, 10)

circle1.print_circle()
circle2.print_circle()

# №3
class Rect(Circle):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, 0)
        self.w = w
        self.h = h

    def calculate_area(self):
        return self.w * self.h
rectangle = Rect(10, 20, 50, 100)
area = rectangle.calculate_area()
print(f"Площадь прямоугольника: {area}")

# №4 (дополнительно создаю два круга по заданным параметрам)
import tkinter as tk

root = tk.Tk()

circle1 = tk.Canvas(root, width=100, height=100)
circle1.create_oval(10, 10, 100, 100, fill='red')
circle1.pack()


circle2 = tk.Canvas(root, width=100, height=100)
circle2.create_oval(10, 10, 60, 60, fill='red')
circle2.pack()

root.mainloop()