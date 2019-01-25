import rosegraphics as rg
import random

def main():

    window = rg.RoseWindow(500, 500)

    for k in range(1000):

        randcolor = rg.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        line = rg.Line(rg.Point(random.randint(0, 500), random.randint(0, 500)), rg.Point(random.randint(0, 500), random.randint(0, 500)))
        line.thickness = random.randint(1, 5)
        line.color = randcolor
        line.attach_to(window)

        circle = rg.Circle(rg.Point(random.randint(0, 500), random.randint(0, 500)), random.randint(0, 30))
        circle.fill_color = randcolor
        circle.attach_to(window)

        window.render()

    window = window.close_on_mouse_click()

main()