from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def rec_move():
    print('rec')
    pass

def cir_move():
    print('cir')
    pass

while True:
    rec_move()
    cir_move()
    
close_canvas()
