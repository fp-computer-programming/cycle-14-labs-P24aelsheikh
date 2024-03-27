#Author: Alsir Elsheikh

import turtle

# Step 2: Create a turtle window with grey background
window = turtle.Screen()
window.bgcolor("grey")
window.setup(width=500, height=500)

# Step 3: Set title of the turtle window
window.title("Lab 3")

# Step 4: Create a turtle with favorite color line
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")  # Change "blue" to your favorite color

# Step 5: Draw an equilateral triangle with sides 200 units long
for _ in range(3):
    my_turtle.forward(200)
    my_turtle.left(120)

# Keep the window open until closed by the user
window.mainloop()
