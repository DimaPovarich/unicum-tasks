import tkinter as tk

# Создаем графическое окно
root = tk.Tk()
root.title("Простой калькулятор")

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    if operation.get() == "+":
        result = num1 + num2
    elif operation.get() == "-":
        result = num1 - num2

    result_label.config(text="Результат: " + str(result))



entry1 = tk.Entry(root, width=10)
entry2 = tk.Entry(root, width=10)
entry1.pack(pady=10)
entry2.pack(pady=10)


operation = tk.StringVar()
operation.set("+")


plus_btn = tk.Radiobutton(root, text="+", variable=operation, value="+")
minus_btn = tk.Radiobutton(root, text="-", variable=operation, value="-")

plus_btn.pack()
minus_btn.pack()


calculate_btn = tk.Button(root, text="=", command=calculate)
result_label = tk.Label(root, text="Результат:")

calculate_btn.pack(pady=10)
result_label.pack(pady=10)


root.mainloop()
