from tkinter import *

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

root = Tk()
root.geometry("400x300")
root.title("Комбинаторный калькулятор")

def permutations_yes():
    num = data_str.get()
    label["text"] = f"Перестановки с повторениями: {factorial(len(num))}"

def permutations_no():
    num = data_str.get()
    n = len(num)
    k = len(num)
    label["text"] = f"Перестановки без повторений: {factorial(n) // factorial(n-k)}"

def change_permutations():
    root1 = Tk()
    root1.title("Ваш выбор в перестановках")
    button1 = Button(root1, text="С повторениями", command=permutations_yes)
    button2 = Button(root1, text="Без повторений", command=permutations_no)
    button1.pack()
    button2.pack()


def change_combinations():
    root1 = Tk()
    root1.title("Ваш выбор в сочетаниях")
    button1 = Button(root1, text="С повторениями", command=combinations_yes)
    button2 = Button(root1, text="Без повторений", command=combinations_no)
    button1.pack()
    button2.pack()

def combinations_yes():
    num = data_str.get()
    n = len(num)
    k = len(num)
    label["text"] = f"Сочетания с повторениями: {factorial(n+k-1) // factorial(k) * factorial(n-1)}"

def combinations_no():
    num = data_str.get()
    n = len(num)
    k = len(num)
    label["text"] = f"Сочетания без повторений: {factorial(n) // (factorial(k) * factorial(n-k))}"

def change_placement():
    root1 = Tk()
    root1.title("Ваш выбор в размещениях")
    button1 = Button(root1, text="С повторениями", command=placement_yes)
    button2 = Button(root1, text="Без повторений", command=placement_no)
    button1.pack()
    button2.pack()

def placement_yes():
    num = data_str.get()
    n = len(num)
    k = len(num)
    label["text"] = f"размещения с повторениями: {n**k}"

def placement_no():
    num = data_str.get()
    n = len(num)
    k = len(num)
    label["text"] = f"размещения без повторений: {factorial(n) // factorial(n-k)}"

data_str = StringVar(root)
entry = Entry(textvariable=data_str)
but1 = Button(root, text='Подсчитать перестановки', command=change_permutations)
but2 = Button(root, text='Подсчитать сочетания', command=change_combinations)
but3 = Button(root, text='Подсчитать размещения', command=change_placement)
label = Label(root)

entry.pack()
but1.pack()
but2.pack()
but3.pack()
label.pack()

root.mainloop()
