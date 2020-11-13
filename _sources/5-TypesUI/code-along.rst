.. image:: ../img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Learning to Code: User Input
:::::::::::::::::::::::::::::::::::::::::::

How useful would computers be if you couldn't interact
with a program while it was running? 

*User input* refers to information that a user provides when
running a program in order to affect what the program does.

.. shortanswer:: sa-input-example

    For example, a computer game may ask you to input the number of 
    players and a name for each.
    What do you think the game might use this information for?
    

Python provides the ``input`` command for user input.
It must be called with one *string* argument---any number of characters enclosed in quotations.
The interpreter expects this argument to be a message, or *prompt*, 
that you want it to print.

To execute an ``input`` command, the interpreter displays an
*input box* in which it prints the prompt (argument). 
It then waits for the user to type something into the box and press either
the ``enter`` key or the ``OK`` button, which signals that the user is done. 
The interpreter uses the string of characters typed by the user into the input box
as the input value.

You will usually want to assign the input value to a variable so that
you can use the value in later commands.

.. activecode:: ac-input
    :language: python
    :nocodelens:
    
    The program below shows the typical way to get and 
    use input. 
    Run it three or more times; 
    each time, type a different name, phrase, or whatever
    you would like into the input box.
    Then press either the ``enter`` key or the ``OK`` button.
    
    (Be sure to scroll your window so you can see the *output box* that the
    interpreter creates when it executes the ``print`` command.)
    ~~~~
    name = input("Enter a player name: ")
    print("Hello", name + "!")
    
.. reveal:: rv-print-concat
    :showtitle: Show explanation of ``print`` and ``+``
    :hidetitle: Hide explanation of ``print`` and ``+``
    
    ``print(exp1, exp2, ..., expN)``
    
        Prints the expressions ``exp1`` through ``expN``, each separated 
        from the next by a space, in
        an output box.
        
    ``str1 + str2``
    
        If ``str1`` and ``str2`` are strings: creates the string containing all
        the characters of ``str1`` immediately followed by all the characters
        of ``str2``. 
        

Let's explore how you might use input in a Turtle Graphics program.

.. activecode:: ac-TG-input 
    :language: python
    :nocodelens:
    
    Read the program below and predict what it will draw.
    Then run it to verify that you understand how the program works.
    If you are uncertain, chat with a mentor about it. 
    You should understand the program before proceeding any further.
    ~~~~
    # draw a string of beads
    import turtle
    turtle.speed(10)

    s_length = 300               # length of the string
    b_number = 20                # number of beads
    b_color = "red"              # color of beads

    b_diameter = s_length/b_number
    b_radius = b_diameter/2

    turtle.up()
    turtle.goto( -(s_length/2), 0 )
    turtle.color( b_color )
    turtle.down()

    for i in range( b_number ):
        turtle.begin_fill()
        turtle.circle(b_radius)
        turtle.end_fill()
        turtle.up()
        turtle.forward(b_diameter)
        turtle.down()

    turtle.hideturtle()

This program will always draw a string of red beads.
A more useful program might let the user decide what color to make the beads.

To do this, replace the string ``"red"`` in line 7 of ac-TG-input_ with  

    ``input( "Enter a color: ")``

Now, when you run the program and the interpreter gets to line 7, it will
bring up a dialog box containing the prompt and wait for you to type
something into the box.
Type the name of a different color (without any quotes) 
into the dialog box and then press ``enter``.
If you typed a color name that the interpreter knows, 
it draws the string of beads in this color.
How cool is that!

In addition to the bead color, you might like to let the user 
decide how long the string of beads should be and how
many beads it should contain.

To let the user choose the length, try replacing the ``300`` 
in ac-TG-input_ with:

    ``input( "Enter a length (in pixels): " )``

.. shortanswer:: sa-type-error

    What happens when you run the program in ac-TG-input_ 
    after making the suggested replacement?
    
See if you are can find answers to the following questions by reading what
it says in the *error box* (the light red box) now displayed below the editor window.

.. mchoice:: mc-err-line
    :random:
    
    At what line did the interpreter find an error?
    
    - the line containing ``s_length = input( "Enter a length (in pixels): " )``
    
      - No, this command assigned the string of characters that you typed into the 
        input box to ``s_length``. Look at the contents of the line number mentioned 
        in the error box.
    
    - the line containing ``b_color = input( "Enter a color: ")``
    
      - No, this command assigned the string of characters that you typed into the input 
        box to ``b_color``. Look at the contents of the line number mentioned in the error box.        
    
    - the line containing ``b_diameter = s_length/b_number``
    
      + Yes! The interpreter was not able to calculate ``s_length/b_number`` because 
        ``s_length`` holds a string value --- that is, a sequence of characters ---
        and division is not defined for strings.
    
    - the line containing ``b_radius = b_diameter/2``
    
      - No, the interpreter stopped executing the program when the error occurred. 
        So it never even executed this line
          
.. mchoice:: mc-err-type
    :random:
    
    What is the *name* of the error that occurred?
    
    - TypeError
    
      + Yes! Many different kinds of errors can occur. The name indicates what 
        kind of error happened. The interpreter shows the kind of error at the
        very start of the error message.
    
    - NameError
    
      - No. Many different kinds of errors can occur. The name indicates what 
        kind of error happened. The interpreter shows the kind of error at the
        very start of the error message.
    
    - DivisionError
    
      - No. Many different kinds of errors can occur. The name indicates what 
        kind of error happened. The interpreter shows the kind of error at the
        very start of the error message.
    
    - Gross Error
    
      - No. Many different kinds of errors can occur. The name indicates what 
        kind of error happened. The interpreter shows the kind of error at the
        very start of the error message.

    
To understand the problem we are bumping into, we need to talk about the *types*
of values.

Every programming language provides different types of values.
Python provides four *primitive data types*:

* ``int``

  - For representing whole numbers (*integers*)
    
  - Examples:
  
    ::
  
        0     2020     -35     

* ``float``

  - For representing decimals (*floats*)
    
  - Examples: 
  
    ::
    
        0.0     3.1416      -.75     

* ``str``

  - For representing text (*strings*)
    
  - Examples:
  
    ::
    
       'Coders rule!' 
       
       "Practice makes perfect."
       
       """12/25/2020"""
       
       """Only tripled quoted strings can go for
          more than one line."""

* ``bool``

  - For representing a yes-no decision (*booleans*)
    
  - There are only two values of type ``bool``: 
  
    ::
    
       True      False

Mike's rap about variables and types may help you remember them, and maybe even 
understand them a bit better.
But keep in mind that
Mike's raps is about languages like Java, and 
types in Python are a bit simpler than types in Java.
In particular, Python does *not*
have a ``char`` type and it does *not* let you write the type 
at the beginning of an assignment
statement.

.. raw:: html

    <div align="middle">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/m7szVmMta-o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

.. reveal:: rv-types-explanation
    :showtitle: Show why types?
    :hidetitle: Hide why types?
    
    Under construction.
    
.. Reminder that we said a variable is like a container for a value -- more accurately,
   it's the address in computer memory of the first bit representing the value is stored.
   The conventions for representing different types of data are different -- integers
   can be represented exactly using binary notation. But floats cannot. They can only
   be approximated. Computers essentially use scientific notation to represent floats.
   A float is represented by two integers--one for the mantissa and the other for the
   exponent. The number of bits used for each is fixed. String could be any number of
   characters, so can be of arbitrary length and each character is represented by their
   binary ascii code. So just knowing the address where the value of a var starts isn't
   enough to know how many bits make up the value or what the value is.
       
.. Maybe do a concrete example of the rep for a short string in memory assuming a very
   small word-size and what that same seq of bits would produce if interpreted as an
   int and/or as a float? Or for bool -- anything but all 0's is true.

       
Let's look again at the program we are working on and the error it produces:

.. activecode:: ac-TG-input-error 
    :language: python
    :nocodelens:
    
    The program is copied below and the ``input`` commands are added.
    Run it to see the error that it produces.
    Type a whole number in the first input box and a color name in the second.
    ~~~~
    # draw a string of beads
    import turtle
    turtle.speed(10)

    s_length = input( "Enter a length (in pixels): " )  # length of the string
    b_number = 20                # number of beads
    b_color = input( "Enter a color: ")                 # color of beads

    b_diameter = s_length/b_number
    b_radius = b_diameter/2

    turtle.up()
    turtle.goto( -(s_length/2), 0 )
    turtle.color( b_color )
    turtle.down()

    for i in range( b_number ):
        turtle.begin_fill()
        turtle.circle(b_radius)
        turtle.end_fill()
        turtle.up()
        turtle.forward(b_diameter)
        turtle.down()

    turtle.hideturtle()

The error message tells you
that the interpreter could not execute the instruction on line 9 because of 
a type error (``TypeError``).
It also tells you that it cannot perform
division (``Div``) on values of type ``str`` and ``int``.
Looking at line 9, you can see that your code says to divide the value of
``s_length`` by the value of ``b_number`` and assign the result to ``b_diameter``.
So the problem is that ``b_number`` stands for a string at line 9, not a number!

Why? 
**Because the ``input`` command always produces a string value.**
For example, suppose you type ``300`` into the first input box when you run the program,
then the value of ``b_number`` at line 9 will be the string ``"300"``, not the 
number ``300``!

How can we fix this problem?
Python provides an ``int`` function for exactly this kind of situation.
You call ``int`` with an argument that denotes a number and it returns the ``int``
representation of that number.
For example, ``int("300")`` is ``300``.


In ac-TG-input-error_, add the following assignment *after* line 5:

::

   b_number = int(b_number)
   
Then run the program and check that it no longer produces an error, and that you can
get it to draw longer and shorter strings of beads of different colors.

Finally, modify the program to also ask the user for the number of beads.
Chat with your mentor if you encounter any additional issues.
Your final program should ask the user for the length to make the string,
the number of beads to use, and the color.
Then it should draw a string of beads of the given length and containing
the given number of beads of the given color.




       
    
    





