# Author: Alsir Elsheikh

import turtle

# Create a turtle window
window = turtle.Screen()

# Set window dimensions
window.setup(width=500, height=500)

# Set window title
window.title("Lab 2")

# Create a turtle
t = turtle.Turtle()

# Draw an equilateral triangle
for _ in range(3):
    t.forward(100)  # Move turtle forward by 100 units
    t.left(120)     # Turn turtle left by 120 degrees

# Keep the window open until it's closed by the user
window.mainloop()
