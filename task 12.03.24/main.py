from tkinter import *from tkinter import ttk
data_str = None
def factorial(n):
    if n <= 1:        return 1
    else:        return n * factorial(n-1)
def permutations_yes():
    if data_str:        num = data_str.get()
        label["text"] = f"Перестановки с повторениями: {factorial(len(num))}"
def permutations_no():    if data_str:
        num = data_str.get()        n = len(num)
        k = len(num)        label["text"] = f"Сочетания: {factorial(n) / factorial(n-k)}"
def change_combinations():
    popup = Toplevel(root)    popup.title("Ваш выбор в сочетаниях")
    popup.configure(bg="#333333")
    data_str_popup = StringVar(popup)    entry_popup = Entry(popup, textvariable=data_str_popup, bg="#555555", fg="white")
    style = ttk.Style()
    style.configure('TButton', padding=6, relief="flat", background="#02b4fa", foreground="black", font=('Helvetica', '12', 'bold'))    style.map('TButton', background=[('active', '#02b4fa')])
    button1 = ttk.Button(popup, text="С повторениями", command=combinations_yes, style='TButton')
    button2 = ttk.Button(popup, text="Без повторений", command=combinations_no, style='TButton')
    entry_popup.pack(pady=10)    button1.pack(pady=10)
    button2.pack(pady=10)
def combinations_yes():    if data_str:
        num = data_str.get()        n = len(num)
        k = len(num)        label["text"] = f"Сочетания с повторениями: {factorial(n+k-1) // (factorial(k) * factorial(n-1))}"
def combinations_no():
    if data_str:        num = data_str.get()
        n = len(num)        k = len(num)
        label["text"] = f"Сочетания без повторений: {factorial(n) // (factorial(k) * factorial(n-k))}"
def change_placement():    popup = Toplevel(root)
    popup.title("Ваш выбор в размещениях")    popup.configure(bg="#333333")
    data_str_popup = StringVar(popup)
    entry_popup = Entry(popup, textvariable=data_str_popup, bg="#555555", fg="white")
    style = ttk.Style()    style.configure('TButton', padding=6, relief="flat", background="#02b4fa", foreground="black", font=('Helvetica', '12', 'bold'))
    style.map('TButton', background=[('active', '#02b4fa')])
    button1 = ttk.Button(popup, text="С повторениями", command=placement_yes, style='TButton')    button2 = ttk.Button(popup, text="Без повторений", command=placement_no, style='TButton')
    entry_popup.pack(pady=10)
    button1.pack(pady=10)    button2.pack(pady=10)
def placement_yes():
    if data_str:        num = data_str.get()
        n = len(num)        k = len(num)
        label["text"] = f"Размещения с повторениями: {n**k}"
def placement_no():    if data_str:
        num = data_str.get()        n = len(num)
        k = len(num)        label["text"] = f"Размещения без повторений: {factorial(n) // factorial(n-k)}"
def change():
    global data_str    popup = Toplevel(root)
    popup.title("Ваш выбор")    popup.configure(bg="#333333")
    data_str = StringVar(popup)
    entry_popup = Entry(popup, textvariable=data_str, bg="#555555", fg="white")
    style = ttk.Style()    style.configure('TButton', padding=6, relief="flat", background="#02b4fa", foreground="black", font=('Helvetica', '12', 'bold'))
    style.map('TButton', background=[('active', '#02b4fa')])
    button1 = ttk.Button(popup, text="Подсчитать перестановки", command=permutations_yes, style='TButton')    button2 = ttk.Button(popup, text="Подсчитать сочетания", command=change_combinations, style='TButton')
    button3 = ttk.Button(popup, text="Подсчитать размещения", command=change_placement, style='TButton')
    entry_popup.pack(pady=10)    button1.pack(pady=10)
    button2.pack(pady=10)    button3.pack(pady=10)
root = Tk()
root.geometry("400x300")root.title("Комбинаторный калькулятор")
root.configure(bg="#333333")
style = ttk.Style()style.configure('TButton', padding=6, relief="flat", background="#00BFFF", foreground="black", font=('Helvetica', '12', 'bold'), borderwidth=0)
style.map('TButton', background=[('active', '#00BFFF')])
but1 = ttk.Button(root, text='Подсчитать перестановки', command=change, style='TButton')but2 = ttk.Button(root, text='Подсчитать сочетания',
command=change_combinations, style='TButton')
but3 = ttk.Button(root, text='Подсчитать размещения', command=change_placement, style='TButton')
label = Label(root, bg="#333333", fg="white")
but1.pack(pady=5)but2.pack(pady=5)
but3.pack(pady=5)label.pack(pady=10)
root.mainloop()
