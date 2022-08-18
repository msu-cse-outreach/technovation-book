.. image:: ../img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Learning to Code: Functions
:::::::::::::::::::::::::::::::::::::::::::

If needed, you can see summaries of the ``turtle`` commands used in this section by
pressing the button below.

.. reveal:: re-turtle-commands-3-4
    :showtitle: Show a summary of commands
    :hidetitle: Hide the summary of commands
       
    ``import turtle``

        Import the ``turtle`` module, which defines a ``turtle`` and
        all of the ``turtle`` commands.
        
    ``turtle.speed(S)``
   
        Set the drawing speed to ``S``, a number between 0 (slow) and 10 (fast).
        
    ``turtle.color(C)``
   
        Set the pen color to be ``C``, a color string (https://trinket.io/docs/colors).
        
    ``turtle.setheading(A)``
    
        Set the direction of travel to ``A`` degrees (e.g., 0 = east, 90 = north,
        180 = west, 270 = south).
                
    ``turtle.hideturtle()``, ``turtle.showturtle()``
    
        Make the turtle invisible,
        make the turtle visible.
        
    ``turtle.begin_fill()``
    
        Begin drawing a shape to be filled.
    
    ``turtle.end_fill()``
    
        Fill the shape drawn since the last ``begin_fill()`` command.
        
    ``turtle.up()``,  ``turtle.down()``
   
        Do not leave a trail when moving,
        leave a trail when moving.
        
    ``turtle.goto(X, Y)``
    
        Move straight to the pixel with coordinates (``X``, ``Y``).
        
    ``turtle.forward(L)``, ``turtle.backward(L)``
    
        Move forward (in the direction of travel) by ``L`` pixels,
        move backward (opposite to the direction of travel) by ``L`` pixels
        
    ``turtle.left(D)``, ``turtle.right(D)``
    
        Rotate left (counter-clockwise) by ``D`` degrees, 
        rotate right (clockwise) by ``D`` degrees

    ``turtle.circle(R)``
    
        Move counter-clockwise in the direction of travel
        and in a circle of radius ``R`` pixels.
        

Run the code below to see what it draws.


 
    
    
    



   



