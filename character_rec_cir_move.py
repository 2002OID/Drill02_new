from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def rec_move():
    print('rec')
    pass

def cir_move():
    print('cir')
    #일단 그림부터 그려보자
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)

    
    pass

while True:
    rec_move()
    cir_move()
    break
    
close_canvas()
