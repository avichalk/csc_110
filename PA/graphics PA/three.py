from graphics import graphics
import random

def main():
    gui = graphics(600, 600, 'canvas')
    x = 0
    y1 = random.randint(50,550)
    y2=random.randint(50,550)
    y3=random.randint(50,550)
    while True:
        gui.clear()
        gui.rectangle(x,y1,50,50, fill='red')
        gui.triangle(x,y2,x+50,y2,x+25,y2+50, fill='blue')
        gui.ellipse(x+25,y3,50,50,fill='green')
        x=x+10
        if x>650:
            x=-50
            y1=random.randint(50,550)
            y2=random.randint(50,550)
            y3=random.randint(50,550)
        gui.update_frame(60)

main()