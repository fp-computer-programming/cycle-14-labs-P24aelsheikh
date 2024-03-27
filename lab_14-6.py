#Author Alsir Elsheikh

import turtle

# Prompt the user for a color
color = input("Enter a color: ")

# Prompt the user for a size with constraints
while True:
    size = input("Enter a size (1-5): ")
    try:
        size = int(size)
        if 1 <= size <= 5:
            break
        else:
            print("Size must be between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Change the turtle to be the color and size that the user input
turtle.color(color)
turtle.pensize(size)

# Function to draw a filled square when clicked
def draw_square(x, y):
    turtle.penup()
    turtle.goto(x - 50, y + 50)  # Adjusting for the center of the square
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

# Create an onclick event so a 100 units x 100 units filled in square is drawn when the user clicks
turtle.onscreenclick(draw_square)

turtle.mainloop()
