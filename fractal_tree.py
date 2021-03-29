import turtle

size = 10
width, height = 600 + 4, 600 + 8
rotation = 25
length = 120

class fractalTree(object):

    def __init__(self, level, t):
        self.level = level
        t.hideturtle()
        t.speed('fastest')
        t.pencolor('white')
        t.pensize(size)
        t.penup()
        t.setpos((300, 50))
        t.pendown()
        t.left(90)
        t.forward(length)
        self.drawTree(length, level, t)

    def drawTree(self, length, level, t):
        size = t.pensize()
        t.pensize(size * 0.60)
        length *= 0.75
        t.left(rotation)
        t.forward(length)

        if level > 0:
            self.drawTree(length, level-1, t)

        t.back(length)
        t.right(2 * rotation)
        t.forward(length)

        if level > 0:
            self.drawTree(length, level-1, t)

        t.back(length)
        t.left(rotation)

        t.pensize(size)


def main():
    level = int(input('Level: '))
    t = turtle.Turtle()
    print('DRAWING...')
    turtle.bgcolor('black')
    screen = turtle.Screen()
    screen.setup(width + 4, height + 8)  # due to the window borders & title bar
    screen.setworldcoordinates(0, 0, width, height)
    tree = fractalTree(level, t)
    print('DONE!')
    turtle.done()
    print('GOODBYE!')

if __name__ == '__main__':
    main()