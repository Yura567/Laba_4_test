from tkinter import *
# импортируем библиотеку random
import random
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.105', 1673))

data = client.recv(2048)

print(data.decode())
# Добавляем глобальные переменные

# глобальные переменные
# настройки окна
WIDTH = 300
HEIGHT = 300

# настройки ракеток

# ширина ракетки
PAD_W = 10
# высота ракетки
PAD_H = 100





# Счет игроков
PLAYER_1_SCORE = 0


# Добавим глобальную переменную отвечающую за расстояние
# до правого края игрового поля
right_line_distance = WIDTH - PAD_W


def update_score(player):
    global PLAYER_1_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)





# устанавливаем окно
root = Tk()
root.title("PythonicWay Pong")

# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

# элементы игрового поля

# правая линия
c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="white")

# установка игровых объектов

# создаем мяч

# правая ракетка
RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="yellow")

p_1_text = c.create_text(WIDTH - WIDTH / 6, PAD_H / 4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")





# зададим глобальные переменные скорости движения ракеток
# скорось с которой будут ездить ракетки
PAD_SPEED = 20
# скорость левой платформы
# скорость правой ракетки
RIGHT_PAD_SPEED = 0


# функция движения обеих ракеток
def move_pads():
    # для удобства создадим словарь, где ракетке соответствует ее скорость
    PADS = {
            RIGHT_PAD: RIGHT_PAD_SPEED}
    # перебираем ракетки
    for pad in PADS:
        # двигаем ракетку с заданной скоростью
        c.move(pad, 0, PADS[pad])
        # если ракетка вылезает за игровое поле возвращаем ее на место
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])


def main():
    move_pads()
    # вызываем саму себя каждые 30 миллисекунд
    root.after(30, main)


# Установим фокус на Canvas чтобы он реагировал на нажатия клавиш
c.focus_set()


# Напишем функцию обработки нажатия клавиш
def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED


# Привяжем к Canvas эту функцию
c.bind("<KeyPress>", movement_handler)


# Создадим функцию реагирования на отпускание клавиши
def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0


# Привяжем к Canvas эту функцию
c.bind("<KeyRelease>", stop_pad)

# запускаем движение
main()

# запускаем работу окна
root.mainloop()