

import tkinter as tk

root = tk.Tk()
root.title("Press Enter to Display 'Hello World!'")
def on_key_press(event):
    if event.keysym == "Return":
        label.config(text="Hello World!")

label = tk.Label(root, text="")
label.pack()

root.bind("<Key>", on_key_press)


root.mainloop()
