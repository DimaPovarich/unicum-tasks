import tkinter as tk


def move_circle(event):
    target_x = event.x
    target_y = event.y

    # Определяем текущие координаты круга
    current_x, current_y = canvas.coords(circle)[0], canvas.coords(circle)[1]

    # Вычисляем вектор сдвига для движения круга к целевой точке
    dx = (target_x - current_x) / 10
    dy = (target_y - current_y) / 10

    # Анимированное движение круга к точке клика
    for _ in range(10):
        canvas.move(circle, dx, dy)
        canvas.update()  # Обновление холста для визуализации движения
        canvas.after(50)  # Задержка времени между каждым шагом


# Создаем графическое окно
root = tk.Tk()
root.title("Движение круга по клику мышью")

# Создаем холст
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Создаем круг и помещаем его в случайное место на холсте
circle = canvas.create_oval(50, 50, 100, 100, fill="red")

# Привязываем событие клика мыши к функции движения круга
canvas.bind("<Button-1>", move_circle)

# Запускаем основной цикл обработки событий
root.mainloop()
