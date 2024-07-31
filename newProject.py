from turtle import *  # Import all the turtle graphics functions
import colorsys  # Import the colorsys module for color conversions

bgcolor("black")  # Set the background color to black
tracer(500)  # Set the tracer speed to reduce the delay in drawing

def draw():
    h = 0  # Initialize hue for colorsys
    for i in range(75):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB
        h += 0.0133  # Increment the hue (original increment was too high)
        
        up()  # Lift the pen up
        goto(0, 0)  # Move the turtle to the origin
        down()  # Put the pen down
        
        color('black')  # Set the pen color to black
        fillcolor(c)  # Set the fill color
        begin_fill()  # Start filling
        
        rt(98)  # Turn right by 98 degrees
        circle(i, 12)  # Draw part of a circle
        fd(290)  # Move forward by 290 units
        fd(i)  # Move forward by 'i' units
        lt(29)  # Turn left by 29 degrees
        
        for j in range(129):
            fd(i)  # Move forward by 'i' units
            circle(j, 299, steps=2)  # Draw a circle with 'steps' for the jagged effect
        
        end_fill()  # End filling

draw()  # Call the draw function
done()  # Finish the turtle graphics
