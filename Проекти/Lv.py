import tkinter as tk
from tkinter import Button

import random

from PIL import Image, ImageTk, ImageSequence


def move_no(event=None):
    x = random.randint(20, 800)
    y = random.randint(150, 580)

    btn_no.place(x=x, y=y)

window = tk.Tk()


window.title("Моей любимой")


window.geometry("1000x700")

window.resizable(width=False, height=False)

canvas = tk.Canvas(
    window,
    height=700,
    width=1000,
    bg="pink",
    bd=0,
    highlightthickness=0
)
canvas.pack()


gif = Image.open("cute_cat.gif")

frames = [
    ImageTk.PhotoImage(frame.copy().convert("RGBA").resize((200, 200)))
    for frame in ImageSequence.Iterator(gif)
]

cat = canvas.create_image(500, 330, image=frames[0])


def animate_cat(index=0):
    canvas.itemconfig(cat, image=frames[index])

    delay = gif.info.get("duration", 100)

    window.after(
        delay,
        animate_cat,
        (index + 1) % len(frames)
    )


animate_cat()

hearts = []

for i in range(20):
    x = random.randint(20, 980)
    y = random.randint(0, 700)

    heart = canvas.create_text(
        x, y,
        text="♥",
        fill=random.choice(["#FF4081", "#FF80AB", "#C2185B", "#FFFFFF"]),
        font=("Arial", random.randint(16, 30))
    )

    # create_text() рисует сердечко на холсте.

    hearts.append(heart)


def animate_hearts():
    for heart in hearts:
        canvas.move(heart, 0, -2)

        # canvas.move(heart, 0, -2) поднимает его на 2 пикселя.

        x, y = canvas.coords(heart)

        if y < -20:
            canvas.coords(
                heart,
                random.randint(20, 980),
                random.randint(720, 850)
            )

    window.after(30, animate_hearts)

    # window.after(30, animate_hearts) повторяет анимацию примерно каждые 30 миллисекунд.

animate_hearts()

canvas.tag_raise(cat)
# В результате сердечки будут непрерывно подниматься снизу вверх.
# Они могут проходить за текстом или кнопками, потому что Canvas у тебя служит фоном.

frame = tk.Frame(
    window,
    bg="pink",
    bd=0,
    highlightthickness=0
)
frame.place(relx=0.5, y=50, anchor="n")

text = tk.Label(
    frame,
    text="Ты меня любишь?",
    bg="pink",fg="#C2185B",
    bd=0,
    font=("Comic Sans MS", 28, "bold"),
    highlightthickness=0)
text.pack()


btn_frame = tk.Frame(
    bg="#C2185B",
    padx=3,
    pady=3
)
btn_frame.pack(side="left",pady=450, padx=90)


def say_yes():
    # Убираем обе кнопки
    btn_yes.place_forget()
    btn_no.place_forget()

    # Убираем обычного котика
    canvas.delete(cat)

    # Меняем надпись
    text.config(text="Я тебя тоже люблю! ❤️")

    love_gif = Image.open("cat.gif")

    love_frames = [
        ImageTk.PhotoImage(
            frame.copy().convert("RGBA").resize((250, 250))
        )
        for frame in ImageSequence.Iterator(love_gif)
    ]

    love_cat = canvas.create_image(
        500, 400,
        image=love_frames[0]
    )

    def animate_love(index=0):
        canvas.itemconfig(love_cat, image=love_frames[index])

        delay = love_gif.info.get("duration", 100)

        window.after(
            delay,
            animate_love,
            (index + 1) % len(love_frames)
        )

    animate_love()

btn_yes = Button(
    window,
    text="Да!!",
    bg="#ED4083",
    command=say_yes,
    font=("Comic Sans MS", 25, "bold"),
    width=8,
    bd=3,
    relief="solid",
    highlightthickness=0,
    activebackground="#ED4083",
    activeforeground="white",
)

btn_yes.place(x=250, y=550)


btn_no = Button(
    window,
    text="Нет",bg="#ED4083",
    font=("Comic Sans MS", 25, "bold"),
    width=8,
    bd=3,
    relief="solid",
    highlightthickness=0,
    activebackground="#ED4083",
    activeforeground="white",
)
btn_no.place(x=570, y=550)

btn_no.bind("<Enter>", move_no)

window.mainloop()