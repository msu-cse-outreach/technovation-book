.. image:: ../img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Learning to Code: If Commands
:::::::::::::::::::::::::::::::::::::::::::

User Input and Drawing
------------------------

Remember user input last week? 
We can let the user decide what the turtle will draw using *if commands* with user input. 
Making a program interactive makes it a lot more fun! 

For example, the code in the box below lets the user say if the
``turtle`` should draw a circle or not. 


.. activecode:: first_if
    :language: python
    :nocodelens:

    Run the code below twice.
    Enter ``yes`` at the prompt on one of the runs, and something else on the other.
    (If you are not able to press the ``Run`` button to start another run, try
    refreshing the page.)
    ~~~~
    # an example interactive program

    import turtle

    answer = input("Would you like me to draw a circle?\nEnter 'yes' or 'no': ")
    
    if answer == "yes":
        turtle.circle(50)


.. reveal:: re-first_if
    :showtitle: Show a line-by-line explanation of this code
    :hidetitle: Hide the line-by-line explanation

    ``import turtle``

        *Import* the code from the ``turtle`` module (a Python library program). 
        Importing a module allows you to use objects (functions, variables, etc.) 
        from that module in writing your own program.

    ``answer = input("Would you like me to draw a circle?\nEnter 'yes' or 'no': ")``

        Prompt the user to enter ``yes`` or ``no``, and save the answer in the variable 
        named ``answer``. 
        Remember variables from before? 
        The variable ``answer`` is like a container. 
        The label on the outside of the container is ``answer``,
        and inside the container is the string of characters that the user typed. 
        If the user typed ``yes``,
        then ``answer`` is equal to ``"yes"``, 
        and if the user typed ``no``, then ``answer`` is equal to ``"no"``. 
        
        The ``\n`` in the string is called a ``control character``. Specifically,
        it prints as a *new line*, like you get when you press the
        ``enter`` key on your keyboard. It causes the prompt in the input
        box to print on two lines.
        
        In a string, the *backslash* character (``\``) *escapes* the character that immediately follows it.
        The backslash and the following character make up a single, special character.
        Some useful control characters in Python include:
        
        * ``\n`` -- new line
        
        * ``\t`` -- horizontal tab
        
        * ``\b`` -- backspace
        
        * ``\\`` -- a single backslash
        
        * ``\'`` -- a single quote (``'``) 
        
        * ``\"`` -- a double quote (``"``)
        
        

    ``if answer == "yes":``

        The double equals operator checks to see if the value on its left and 
        the value on its right are equal. 
        So, if the user typed ``yes``, then the indented code is executed. 
        If the user didn't type ``yes`` then the indented code is skipped over. 
    

.. mchoice:: mc-first_if
    :random:

    What happens if you change line number 7 to say ``if answer == "no":``?
    Mark all the answers that are correct.
    (Hint: Try it!)
    
    - If you run the modified code and enter ``yes`` into the input box, 
      the ``turtle`` draws a circle.
      
      - No. The indented code is not executed
        since ``answer`` is not equal to ``"no"`` (it's equal to ``"yes"``).
        So the program terminates without drawing anything.
        
    - If you run the modified code and enter ``no`` into the input box, 
      the ``turtle`` draws a circle.
      
      + Yes. The ``turtle`` will execute the indented code since ``answer`` equals ``"no"``.

    - If you run the modified code and enter ``yes`` into the input box, 
      the program ends without drawing anything.
      
      + Yes. The indented code is not executed
        since ``answer`` is not equal to ``"no"`` (it's equal to ``"yes"``).
        So the program terminates without drawing anything.

    - If you run the modified code and enter ``no`` into the input box, 
      the program ends without drawing anything.
      
      - No. The ``turtle`` will execute the indented code since ``answer`` equals ``"no"``.
        So it will draw a circle and then terminate.

    - If you run the modified code and enter ``No`` into the input box, 
      the program ends without drawing anything.
      
      + Yes. The indented code is not executed
        since ``answer`` is not equal to ``"no"`` (it's equal to ``"No"``).
        So the program terminates without drawing anything.
        
Recall the ``draw_poly`` function from the lesson on functions?
Let's revisit it to see how we can use the ``if`` command to make the 
``draw_poly`` function more useful.

.. activecode:: ac-if-poly
    :nocodelens:
    :language: python

    The definition of ``draw_poly`` from the lesson on functions appears
    below. 
    Read over the function definition and the program that calls it. 
    Then run the code.
    ~~~~
    import turtle
    turtle.speed(10)

    def draw_poly( N, L, C ):
        """Draw a N-sided regular polygon with lower left corner at (X, Y),
        side length L, and pen color C"""
        # requires: N >= 3 and  L > 0

        turtle.color( C )    
        turn_angle = 360 / N

        turtle.begin_fill()
        
        for i in range( N ):
            turtle.forward( L )
            turtle.left( turn_angle )

        turtle.end_fill()
    
    # move to the start position without leaving a trail
    turtle.up()
    turtle.goto( -50, -150 )
    turtle.down()
    
    draw_poly( 10, 100, "purple")  
    draw_poly( 9, 100, "gold")
    draw_poly( 8, 100, "aqua")
    draw_poly( 7, 100, "blue")
    draw_poly( 6, 100, "green")
    draw_poly( 5, 100, "red")
    draw_poly( 4, 100, "orange")
    draw_poly( 3, 100, "black") 


To check your understanding, answer the questions below.
Ask your mentor any questions (after unmuting)
or type them into the chat. 

.. fillintheblank:: fb-draw-poly1

    During execution of the call ``draw_poly( 8, 100, "aqua")``:
    
    * What is the value of ``N``? |blank|
    
    * What is the value of ``L``? |blank|
    
    * What is the value of ``turn_angle``? |blank|
    
    * How many times is the body of the loop executed? |blank|
    
    - :8: Yes, the first argument (8) is assigned to the first parameter (``N``)
      :x: No, because ``N`` is the first parameter, it is assigned the value of the first argument, which is 8.
    - :100: Yes, the second argument (100) is assigned to the second parameter (``L``)
      :x: No, because ``L`` is the second parameter, it is assigned the value of the second argument, which is 100.
    - :45(.0)?: Yes, at line 10, ``N`` is ``8``, which makes ``360/N`` equal to ``45.0``; thus, line 10 assigns ``45.0`` to ``turn_angle``.
      :x: No, what is ``360/N`` in line 10.
    - :8: Yes, since ``N`` equals ``8``.
      :x: No, what is the value of ``N``?


Now suppose that we don't want the polygons to be filled:

.. image:: img/unfilled-polygons.png 
    :width: 50%
    :align: center
    :alt: turtle drawing of nested unfilled polygons of increasing number of sides
    
Or suppose we want some filled, but not others:

.. image:: img/some-filled-polygons.png
    :width: 50%
    :align: center
    :alt: turtle drawing of nested polygons of increasing number of sides, some filled, others not filled
