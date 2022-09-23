#Author: Avichal `Kaul
#Description: does a landscape that you can move a mouse around on and enjoy playing with because it's displaying a parallax effect
## but i spent three hours trying to ge the animations to work and they didn't so im sad
#Comments: I'm starting this on a friday night after a nightmarish week,
## and I can already feel that it's going to be a long one
from graphics import graphics
import random

def main():
    gui=graphics(500,500,'bruh')
    color1 = gui.get_color_string(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    color2 = gui.get_color_string(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    color3 = gui.get_color_string(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    while True:
        gui.clear()
        gui.rectangle(-100,-100,800,800,'light blue')
        gui.ellipse(320+0.02*gui.mouse_x, 50+0.02*gui.mouse_y, 60, 60, 'yellow')
        gui.triangle(150+0.03*gui.mouse_x, 400+0.03*gui.mouse_y, 350+0.03*gui.mouse_x, 400+0.03*gui.mouse_y, 250+0.03*gui.mouse_x, 50+0.03*gui.mouse_y, color1)
        gui.triangle(-200+0.11*gui.mouse_x, 600+0.11*gui.mouse_y, 500+0.11*gui.mouse_x, 600+0.11*gui.mouse_y, 100+0.11*gui.mouse_x, 100+0.11*gui.mouse_y, color2)
        gui.triangle(100+0.11*gui.mouse_x, 600+0.11*gui.mouse_y, 700+0.11*gui.mouse_x, 600+0.11*gui.mouse_y, 400+0.11*gui.mouse_x, 100+0.11*gui.mouse_y, color3)
        gui.rectangle(-100+0.19*gui.mouse_x,400+0.19*gui.mouse_y,800,200,'light green')
        gui.line(-100+0.19*gui.mouse_x,400+0.19*gui.mouse_y,600+0.19*gui.mouse_x,400+0.19*gui.mouse_y,)
        x=-100
        while x<=600:
            gui.rectangle(x+0.19*gui.mouse_x,400+0.19*gui.mouse_y,5,-20, 'light green')
            x=x+10
        x=50
        y=50
        while y<=100:
            gui.line(x,y,x+20,y+10)
            gui.line(x+20,y+10,x+40,y)
            x=x+60
            y=y+10
        gui.rectangle(350+0.19*gui.mouse_x,450+0.19*gui.mouse_y,25,-50, 'brown')
        gui.ellipse(363+0.19*gui.mouse_x, 370+0.19*gui.mouse_y, 80, 110, 'green')
        gui.update_frame(30)

main()