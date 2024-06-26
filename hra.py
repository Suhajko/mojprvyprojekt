from pygame import *


back = (210, 255, 265)
win_width = 700
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill

racket.png
tenis_ball.png

game = True
while game:
    pass
    for e in event.get():
        if e.type == QUIT:
            game = False

display.update()
