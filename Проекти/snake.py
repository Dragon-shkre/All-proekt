import tkinter as tk
import random as rnd

window = tk.Tk()

window.title("Змейка")
window.geometry('400x400')


canvas = tk.Canvas(window, height=400, width=400)
canvas.pack()

canvas.create_rectangle(0, 0, 400, 400, fill="gray")

snake = canvas.create_rectangle(190, 190, 210, 210, fill="green")
snake_body = [snake]


second_body = canvas.create_rectangle(170, 190, 190, 210, fill="green")
third_body = canvas.create_rectangle(150, 190, 170, 210, fill="green")


snake_body.append(second_body)
snake_body.append(third_body)

food_x = rnd.randrange(10, 380, 20)
food_y = rnd.randrange(10, 380, 20)

food = canvas.create_rectangle(
    food_x,
    food_y,
    food_x + 20,
    food_y + 20,
    fill="red"
)
direction = "Right"
score = 0
score_text = canvas.create_text(50, 20, text="Score: 0")

def move(event):
    global direction
    if event.keysym == "Left" and direction != "Right":
        direction = "Left"
    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"
    elif event.keysym == "Up" and direction != "Down":
        direction = "Up"
    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"

def game_loop():
    food_coords = canvas.coords(food)
    head = canvas.coords(snake)
    if head[0] <= 0 or head[1] <= 0 or head[2] >= 400 or head[3] >= 400:
        print("GAME OVER")
        return
    for i in range(len(snake_body) -1, 0, -1):
        canvas.coords(snake_body[i], canvas.coords(snake_body[i - 1]))
    if direction == "Right":
        canvas.move(snake, 20, 0)
    elif direction == "Left":
        canvas.move(snake, -20, 0)
    elif direction == "Up":
        canvas.move(snake, 0, -20)
    elif direction == "Down":
        canvas.move(snake, 0, 20)
    head = canvas.coords(snake)
    if head[0] == food_coords[0] and head[1] == food_coords[1]:
        print("СЬЕЛ")
        global score
        score += 1
        canvas.itemconfig(score_text, text="Score: " + str(score))

        food_x = rnd.randrange(10, 380, 20)
        food_y = rnd.randrange(10, 380, 20)

        canvas.coords(food, food_x, food_y, food_x + 20, food_y + 20)
        tail_coords = canvas.coords(snake_body[-1])
        new_body = canvas.create_rectangle(tail_coords[0], tail_coords[1], tail_coords[2], tail_coords[3], fill="green")
        snake_body.append(new_body)

    head = canvas.coords(snake)

    for part in snake_body[1:]:
        body_coords = canvas.coords(part)

        if head[0] == body_coords[0] and head[1] == body_coords[1]:
            print("GAME OVER")
            return



    window.after(100, game_loop)
    print(canvas.coords(snake))



game_loop()


window.bind_all("<Key>", move)

window.mainloop()