from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def rec_move():
    print('rec')
    for x in range(50, 750 + 1, 10):
        render_frame(x, 90)
        
    for y in range(90, 550 + 1, 10):
        render_frame(750, y)
        
    for x in range(750, 50 -1, -10):
        render_frame(x, 550)

    for y in range(550, 90 -1, -10):
        render_frame(50, y)
    pass

def cir_move():
    print('cir')
    #일단 그림부터 그려보자
    
    #x = r * cos(s), y = r * sin(s)
    cx, cy, r = 400, 300 ,210
    for deg in range(270, -90, -5):
        x = r * math.cos(math.radians(deg))
        y = r * math.sin(math.radians(deg))
        render_frame(x + cx, y + cy)
        

while True:
    rec_move()
    cir_move()
    
close_canvas()
