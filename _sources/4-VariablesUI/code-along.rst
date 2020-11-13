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

The input value is usually assigned to a variable in order that
it can be used in later commands.

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

.. activecode:: ac-TG-input-example 
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

This program will only draw a string of red beads.
A more useful program might let the user decide what color to make the beads.

To do this, replace the string ``"red"`` in line 7 of ac-TG-input-example_ with  

    ``input( "Enter a color: ")``

Now, when the interpreter gets to line 7, it should
bring up a dialog box containing the prompt.
Type the name of a different color (without quotes) 
into the dialog box and then press ``enter``.

In addition to the bead color, a user might like to say how long a string
they want and the number of beads it should contain.

To let the user choose the length, try replacing the ``300`` 
in ac-TG-input-example_ with something like:

    ``input( "Enter a length (in pixels): " )``

.. shortanswer:: sa-type-error

    What happens when you run the program in ac-TG-input-example_ 
    after making the suggested replacement?
    
See if you are can guess answers to the following questions by reading what
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

    - Used to represent integers
    
    - One or more digits with no punctuation or spaces, possibly
      preceded by a minus sign (``-``), e.g. ``0`` or ``2020`` or ``-35``

* ``float``

    - Used to represent decimal numbers
    
    - One or more digits and a period (``.``) with no other punctuation
      or spaces, possibly
      preceded by a minus sign (``-``), e.g., ``0.0`` or ``3.1416`` or ``-.75``

* ``str``

    - Used to represent text
    
    - Zero or more characters enclosed in either single quotes (``'...'`),
      double quotes (``"..."``), or triple quotes (``"""..."""``), e.g.,
      ``'Coders rule!'" or ``"Practice makes perfect."`` or ``"""Keep on keepin' on."""``

* ``bool``

    - Used to represent the outcome of a yes-no decision (``bool`` is short for 
      ``Boolean``, which comes from the name of the man who invented the study of Logic.)
    
    - There are only two values of type ``bool``: ``True`` and ``False``

Mike's rap about variables and types may help you remember them, and maybe even 
understand them a bit better.
But keep in mind that,
unlike the programming languages that Mike raps about, Python does not
have a ``char`` type and it does not make you write the type in the assignment
statement.

.. raw:: html

    <div align="middle">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/m7szVmMta-o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

 .. reveal:: rv-types-explanation
    :showtitle: Show why programming languages define types
    :hidetitle: Hide why programming languages define types
    
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
       
       
       
       
       
    
    





