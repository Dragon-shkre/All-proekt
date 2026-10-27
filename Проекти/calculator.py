import tkinter as tk


# ==========================================
# ФУНКЦИИ
# ==========================================

# Эта функция добавляет символ на экран калькулятора
def button_click(symbol):
    display.insert(tk.END, symbol)


# Эта функция очищает экран
def clear():
    display.delete(0, tk.END)


# Эта функция вычисляет результат
def calculate():
    try:
        # Получаем текст с экрана
        expression = display.get()

        # Вычисляем математическое выражение
        result = eval(expression)

        # Очищаем старое выражение
        display.delete(0, tk.END)

        # Выводим результат
        display.insert(tk.END, result)

    except:
        # Если произошла ошибка
        display.delete(0, tk.END)
        display.insert(tk.END, "Ошибка")


# ==========================================
# СОЗДАНИЕ ОКНА
# ==========================================

# Создаём главное окно
window = tk.Tk()

# Название окна
window.title("Калькулятор")

# Размер окна
window.geometry("300x400")


# ==========================================
# ЭКРАН КАЛЬКУЛЯТОРА
# ==========================================

# Entry — поле, где будет показываться
# введённое выражение и результат
display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)

# Размещаем экран
display.pack(
    padx=10,
    pady=10,
    fill="x"
)


# ==========================================
# КНОПКИ
# ==========================================

# Создаём отдельный контейнер для кнопок
buttons_frame = tk.Frame(window)

buttons_frame.pack()


# Список кнопок
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]


# Создаём кнопки автоматически
for i, symbol in enumerate(buttons):

    # Если это "=",
    # при нажатии вызываем calculate()
    if symbol == "=":

        button = tk.Button(
            buttons_frame,
            text=symbol,
            font=("Arial", 18),
            width=5,
            height=2,
            command=calculate
        )

    # Для остальных кнопок
    # вызываем button_click()
    else:

        button = tk.Button(
            buttons_frame,
            text=symbol,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda s=symbol: button_click(s)
        )

    # Размещаем кнопку в сетке
    button.grid(
        row=i // 4,
        column=i % 4,
        padx=2,
        pady=2
    )


# ==========================================
# КНОПКА CLEAR
# ==========================================

clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 16),
    command=clear
)

clear_button.pack(
    pady=10
)


# ==========================================
# ЗАПУСК ПРОГРАММЫ
# ==========================================

# Запускаем окно
window.mainloop()