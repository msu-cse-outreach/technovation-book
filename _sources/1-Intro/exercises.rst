.. image:: ../img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center

Practice Makes Perfect
:::::::::::::::::::::::::::::::::::::::::::

The only way to become comfortable coding is to practice.

Next meeting, we'll start teaching you the rules of coding in Python.
But for now, you can practice running and experimenting with programs
that others have written.

We've included some programs that you can run and experiment 
with below.

Checker Board
--------------

.. activecode:: checker_board
    :language: python
    :above:
    :nocodelens:
    :timelimit: 200000
    
    Run the program. Then run some experiments in which you: 
    
    - change the numbers in lines 7, 8 and 9
    
    - change the color-string names in lines 11 and 12
    
    - add a hash symbol (``#``) to the front of the ``turtle.hideturtle()`` instruction 
        (the last line)
    
    ~~~~
    
    # Import the turtle library
    import turtle
    # Set the speed to 10 (fast)
    turtle.speed(10)
    
    unit = 20
    rnum = 8
    cnum = 8
    
    last_col_color = last_row_color = "black"
    next_col_color = next_row_color = "white"

    # Move into the starting position (lower left corner)
    turtle.up()
    turtle.goto(-rnum*unit/2, -cnum*unit/2)
    turtle.down()

    # Draw the board
    for i in range(rnum):
        
        # Draw row i
        for j in range(cnum):
            # Draw square j of row i
            turtle.color("black", next_col_color)

            turtle.begin_fill()
            for k in range(4):
                turtle.forward(unit)
                turtle.left(90)

            turtle.end_fill()

            # Get ready to draw the next square
            turtle.forward(unit)
            next_col_color, last_col_color = last_col_color, next_col_color

        # Get ready to draw the next row
        turtle.up()
        turtle.goto(turtle.xcor()-cnum*unit, turtle.ycor()+unit)
        turtle.down()

        next_row_color, last_row_color = last_row_color, next_row_color
        next_col_color, last_col_color = next_row_color, last_row_color

    turtle.hideturtle()
    

Turtle Star
-----------

.. activecode:: turtle_star
    :language: python
    :above:
    :nocodelens:
    :timelimit: 20000
    
    Run the program. Then run some experiments in which you
    ~~~~
    
    # Import the turtle library 
    import turtle
    turtle.speed(10)
    
    size = 200
    
    # Go to the starting point
    turtle.up()
    turtle.goto(-(size//2), 0)
    turtle.down()

    # Set the pen color as red and the
    # fill color as yellow
    turtle.color("red", "yellow")
    
    # draw a 36-pointed star
    turtle.begin_fill()
    for i in range(37):
        turtle.forward(size)
        turtle.left(170)
    turtle.end_fill()
    
    turtle.hideturtle()

Spirograph
-----------

.. activecode:: spirograph
    :language: python
    :above:
    :nocodelens:

    Instructions
    ~~~~

    # Import the turtle library 
    import turtle

    # Set the pensize as 2 and speed of drawing as 10
    turtle.pensize(2)
    turtle.speed(10)

    size = 100
    rotate_amt = 10
  
    # Iterate six times in total
    for i in range(6):
    
        # Choose your color combination
        for color_name in ('red', 'magenta', 'blue', 
                  'cyan', 'green', 'white',
                  'yellow'):
        
            turtle.color(color_name)
          
            # Draw a circle of choosen size, 100 here
            turtle.circle(size)
          
            # Move rotate_amt pixels left to draw another circle
            turtle.left(rotate_amt)
      
    # Hide the turtle
    turtle.hideturtle()

 
