#Author: Alsir Elsheikh

import turtle

# Step 2: Create a default-size turtle window
window = turtle.Screen()
window.title("Lab 4")

# Step 4: Change the speed and color of the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(2)  # Change speed as desired
my_turtle.color("green")  # Change color as desired

# Step 5: Create a stamp of the turtle at the origin
my_turtle.stamp()

# Step 6: Create a square with top-left vertex at position (100, 100)
my_turtle.penup()
my_turtle.goto(100, 100)
my_turtle.pendown()

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Step 7: Fill the square with another color
my_turtle.fillcolor("yellow")  # Change color as desired
my_turtle.begin_fill()
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.end_fill()

# Keep the window open until closed by the user
window.mainloop()
