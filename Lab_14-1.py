#Author: Alsir Elsheikh

import turtle

# Create a turtle window
window = turtle.Screen()
window.title("Lab 1")
window.setup(width=1000, height=1000)

# Create a turtle
t = turtle.Turtle()

# Draw a rectangle
def draw_rectangle():
    t.penup()
    t.goto(0, 0)  # Top left corner
    t.pendown()
    for _ in range(2):
        t.forward(250)  # Length of the rectangle
        t.right(90)
        t.forward(100)  # Width of the rectangle
        t.right(90)

# Call the function to draw the rectangle
draw_rectangle()

# Keep the window open until it is closed by the user
window.mainloop()
