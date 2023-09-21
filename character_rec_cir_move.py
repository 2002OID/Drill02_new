from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def rec_move():
    print('rec')
    for x in range(50, 750 + 1, 10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        delay(0.01)

    for x in range(750, 50 -1, -10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,550)
        delay(0.01)
    pass

def cir_move():
    print('cir')
    #일단 그림부터 그려보자
    
    #x = r * cos(s), y = r * sin(s)
    cx, cy, r = 400, 300 ,210
    for deg in range(270, -90, -5):
        x = r * math.cos(math.radians(deg))
        y = r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x + cx,y + cy)
        delay(0.01)
        

while True:
    rec_move()
    #cir_move()
    break
    
close_canvas()
