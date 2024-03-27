#Author: Alsir Elsheikh

import turtle

# Initialize turtle
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling key presses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def move_forward():
    tess.forward(30)


def move_backward():
    tess.backward(30)


def turn_left():
    tess.left(90)


def turn_right():
    tess.right(90)


# Set up the keys for movement
wn.onkey(move_forward, "Up")
wn.onkey(move_backward, "Down")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")

wn.listen()  # Listen for key presses
wn.mainloop()
