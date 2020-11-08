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
You can think of the argument of an ``input`` command as a message, or *prompt*, for the user.

To execute an ``input`` command, the interpreter displays an
*input box* in which it prints the argument (prompt). 
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

To do this, replace the string ``"red"`` with  

    ``input( "Enter a color: ")``

Now, when the interpreter gets to line 7, it should
bring up a dialog box containing the prompt.
Type the name of a different color (without quotes) 
into the dialog box and then press ``enter``.

In addition to the bead color, a user might like to say how long a string
they want and the number of beads they want on it.

To let the user choose the length, try replacing the ``300`` with something like:

    ``input( "Enter a length (in pixels): " )``

.. shortanswer:: sa-type-error

    What happens when you run the program after making the suggested replacement?
    See if you are can answer the following questions  
    
    




.. raw:: html

    <div align="middle">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/m7szVmMta-o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    
    
    





