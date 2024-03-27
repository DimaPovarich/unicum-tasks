import tkinter as tk
import random

root = tk.Tk()
root.title("Рисование круга по щелчку мышью")
root.geometry("500x500")

def create_circle(event):
    x = random.randint(30, 470)
    y = random.randint(30, 470)
    radius = 20
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")



canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.bind("<Button-1>", create_circle)


root.mainloop()
