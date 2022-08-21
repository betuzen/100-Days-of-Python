from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    tim.right(15)


def move_counterclockwise():
    tim.left(15)


def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counterclockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
