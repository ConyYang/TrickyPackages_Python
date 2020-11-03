import turtle

s = turtle.Screen()
t = turtle.Turtle()


def draw_polygons():
    for i in range(4):
        t.right(90)
        t.forward(100)


# t.rt() instead of t.right()
# t.fd() instead of t.forward()
# t.lt() instead of t.left()
# t.bk() instead of t.backward()


def quadrants():
    # t is initially at (0,0)
    t.goto(100, 100)
    # bring turtle back to home
    t.home()


def circle():
    t.circle(radius=60)


def dot():
    t.dot(20)


def change_color():
    s.bgcolor("blue")


def change_Turtle(shape=False, color=False):
    if shape:
        t.shapesize(stretch_wid=1, stretch_len=5, outline=10)
        t.shapesize(stretch_wid=10, stretch_len=5, outline=1)
        t.shapesize(stretch_wid=1, stretch_len=10, outline=5)
        t.shapesize(stretch_wid=10, stretch_len=1, outline=5)
    if color:
        t.shapesize(3, 3, 3)
        t.fillcolor("red")
        t.pencolor("green")
        t.color("green", "red")


def change_pensize():
    t.pensize(5)
    t.forward(100)


def fill_shape():
    t.begin_fill()
    t.begin_fill()


if __name__ == '__main__':
    while True:
        change_Turtle(color=True)
