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
   
        Set the pen color to be ``C``, a color string.
                
    ``turtle.hideturtle()``, 
    
        Make the turtle invisible.
        
    ``turtle.begin_fill()``
    
        Begin drawing a shape to be filled.
    
    ``turtle.end_fill()``
    
        Fill the shape drawn since the last ``begin_fill()`` command.
        
    ``turtle.up()``
   
        Do not leave a trail when moving. 
        
    ``turtle.down()``
   
        Leave a trail when moving.
        
    ``turtle.goto(X, Y)``
    
        Move straight to the pixel with coordinates (``X``, ``Y``).
        
    ``turtle.forward(L)``
    
        Move forward (in the direction of travel) by ``L`` pixels
        
    ``turtle.left(D)``
    
        Rotate left (counter-clockwise) by ``D`` degrees

    ``turtle.circle(R)``
    
        Move in a circle of radius ``R`` pixels, counter-clockwise in the direction of travel

Run the code below to see what it draws.

.. activecode:: ac-house-no-funcs
    :language: python
    :nocodelens:
    
    import turtle
    turtle.speed(10)

    # draw the frame for house
    turtle.up()
    turtle.goto(-150,-150)
    turtle.down()

    turtle.color("blue")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
    turtle.end_fill()

    # draw the front door
    turtle.up()
    turtle.goto(-30, -150)
    turtle.down()

    turtle.color("brown")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

    # draw the bottom right window
    turtle.up()
    turtle.goto(60, -110)
    turtle.down()

    turtle.color("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()                  

    # draw the bottom left window
    turtle.up()
    turtle.goto(-120, -110)
    turtle.down()

    turtle.color("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()                  

    # draw the top left window
    turtle.up()
    turtle.goto(-120, -30)
    turtle.down()

    turtle.color("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()                  

    # draw the top middle window
    turtle.up()
    turtle.goto(-30, -30)
    turtle.down()

    turtle.color("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()                  

    # draw the top right window
    turtle.up()
    turtle.goto(60, -30)
    turtle.down()

    turtle.color("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(60)
        turtle.left(90)
    turtle.end_fill()                  

    # draw the roof
    turtle.up()
    turtle.goto(-175, 50)
    turtle.down()

    turtle.color("gray")
    turtle.begin_fill()
    turtle.goto(175, 50)
    turtle.goto(0, 150)
    turtle.goto(-175, 50)
    turtle.end_fill() 

    # draw the door knob
    turtle.up()
    turtle.goto( -10, -100)
    turtle.down()

    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()

    # hide the turtle 
    turtle.hideturtle()

Before writing the code, we designed the house on a graph paper.
We counted each square as 10 pixels.

.. image:: img/house-sketch.jpg
    :width: 400
    :align: center
    :alt: Drawing of a house on graph paper
    
When writing the code, we added a comment at the start of the code that 
draws the different parts of the house --- the frame, door,
windows, roof, and door knob ---
to help us remember how the code works.
Do you see how the hand-drawn design and
the sections of code match up?
    
.. shortanswer:: sa-compare-code-1
   :optional: 
   
   Compare the section of code that draws the frame of the house (lines 5--16) 
   with the section of code that draws the door (lines 19--30).
   What do you notice about these two sections of code?
   (Suggestion: Drag the bottom right corner of the code editor window
   down farther to see more of the program without needing to scroll.)
   
.. shortanswer:: sa-compare-code-2
   :optional:    
   
   Compare the section of code that draws the top left window (lines 57--66)
   with the section
   of code that draws the top middle window (lines 69--78). 
   What do you notice about these two sections of code?

Maybe you aren't surprised that the sections of code are so similar. 
The house and the door are both colored rectangles,
and the two windows are both colored squares,
so you might expect code to draw them would be almost the same.

But this might also make you wonder: 
Wouldn't code for drawing this house be much easier to write (and read)
if there were commands for drawing colored rectangles, squares
and triangles?

FUNCTIONS TO THE RESCUE: 
We can create functions to teach the interpreter new commands!

A function is kind of like a recipe.
If you write down a recipe for making jelly from 
berries, a sweetner and some liquid,
then you can use that recipe to create different kinds of fruit jellies.
You can make cherry jelly from a bushel of cherries, refined sugar and water.
And you can also make blueberry jelly from a basket of blueberries,
unrefined sugar, and apple juice.
And so on.

The recipe just says what you do to "fruit" and "a sweetner" and "the liquid"
to make fruit jelly. 
But when you follow the recipe, you use actual fruit that you bought or
collected where it says "fruit" and the sugar you have on hand
where it says "the sweetener" and tap water where it says "the liquid". 

.. activecode:: ac-func-warmup
    :language: python
    :nocodelens:
    
    To see how code can be like a recipe, run the program below.
    Then use it in answering the questions that follow.
    
    ~~~~
    import turtle
    
    X = -150
    Y = -150
    W = 300
    H = 200
    C = "blue"
    
    turtle.up()
    turtle.goto(X, Y)
    turtle.down()

    turtle.color(C)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(W)
        turtle.left(90)
        turtle.forward(H)
        turtle.left(90)
    turtle.end_fill()
    

.. fillintheblank:: fb-recipe-1

    What values should you assign to the variables in the above program 
    to get it to draw a brown door (with no door knob) at the position and 
    size of the one in our drawing?
    
    X = |blank| 
    Y = |blank| 
    W = |blank| 
    H = |blank| 
    C = |blank|
    
    - :-30: Correct!
      :x: Incorrect. Run the code to see where the rectangle begins 
          if you use  this ``X`` value. 
          Then try another value.
    - :-150: Correct!
      :x: Incorrect. Run the code to see where the rectangle begins if you use  
          this ``Y`` value.
          Then try another value.
    - :60: Correct!
      :x: Incorrect. Run the code to see how wide the rectangle is if you use 
          this ``W`` value.
          Then try another value.
    - :100: Correct!
      :x: Incorrect. Run the code to see how high the rectangle is if you use 
          this ``H`` value.
          Then try another value.
    - :"brown": Correct!
      :x: Incorrect. This should be the fill color (``"brown"``).
          Don't forget the quotes.



.. fillintheblank:: fb-recipe-2

    What values should you assign to the variables in the above program 
    to get it to draw a purple square that is centered in the canvas
    and is 200 pixels on each side?
    
    X = |blank| 
    Y = |blank| 
    W = |blank| 
    H = |blank| 
    C = |blank|
    
    - :-100: Correct!
      :x: Incorrect. Run the code to see where the shape begins if you use this ``X`` value. 
          Then try another value.
    - :-100: Correct!
      :x: Incorrect. Run the code to see where the shape begins if you use  this ``Y`` value.
          Then try another value.
    - :200: Correct!
      :x: Incorrect. Run the code to see how wide the shape is if you use  this ``W`` value.
          Then try another value.
    - :200: Correct!
      :x: Incorrect. Run the code to see how high the shape is if you use  this ``H`` value.
          Then try another value.
    - :"purple": Correct!
      :x: Incorrect. This should be the fill color (``"purple"``).
          Don't forget the quotes.

 
So, in a way, the code

.. raw:: html
    
    <div>
        <pre>
    turtle.up()
    turtle.goto(X, Y)
    turtle.down()

    turtle.color(C)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(W)
        turtle.left(90)
        turtle.forward(H)
        turtle.left(90)
    turtle.end_fill()
        </pre>
    </div>

is like a recipe for an interpreter
to draw a colored rectangle and values for the variables are 
like ingredients to use when following the recipe: 
If you give the interpreter the ingredients to use (values for the variables) and
tell it what recipe (function) you want it to use,
the interpreter performs the assignments and then follows the recipe 
(executes code in the *function body*) to draw a rectangle.

In Python, you write a *function definition* to teach the interpreter a new command.
The active code below contains an example of a function definition for a ``draw_rectangle`` 
command. 

.. activecode:: ac-draw-rect
    :language: python
    :nocodelens:
    
    Run this program to define a ``draw_rectangle`` function.
    
    ~~~~
    
    import turtle
    
    def draw_rectangle(X, Y, W, H, C):
        "draw a rectangle with lower left corner at (X, Y), width W, height H, and color C"
        
        turtle.up()
        turtle.goto(X, Y)
        turtle.down()

        turtle.color(C)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(W)
            turtle.left(90)
            turtle.forward(H)
            turtle.left(90)
        turtle.end_fill()
        
It doesn't * *look like* * running the program does anything.
But it does: Running the program teaches the interpreter a new command, 
called ``draw_rectangle``. 

To see this, add the following commands starting on line 20 in the code editor.
Be careful **not** to indent either command.
They both need to start in the first column.

.. raw:: html
    
    <div>
        <pre>
    draw_rectangle(-150, -150, 300, 200, "blue")
    draw_rectangle(-30, -150, 60, 100, "brown")
        </pre>
    </div>
    
    

   



