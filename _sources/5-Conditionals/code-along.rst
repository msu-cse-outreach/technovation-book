.. image:: ../../_static/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Learning to Code
:::::::::::::::::::::::::::::::::::::::::::

User Input and Drawing
------------------------

Remember user input last week? We can use that to decide which way the turtle will move. 
Making a program interactive will be a lot of fun. 

For example, the code in the box below instructs the ``turtle`` to draw a square. 


.. activecode:: first_if
    :language: python
    :nocodelens:

    To run the code, press the green ``Run`` button. The result will be shown below this *Active Code* box. So you may need
    to scroll the browser view up to see it.
    ~~~~
    # a square with side-length 100 pixels

    import turtle

    u = input("Would you like me to draw a shape? Type yes or no: ")
    if u == "yes":
        turtle.circle(50)

.. reveal:: re-first_if
    :showtitle: Show a line-by-line explanation of this code
    :hidetitle: Hide the line-by-line explanation

    ``import turtle``

        *Import* the code from the ``turtle`` module, 
        which is a library program that comes with Python. 
        Importing a program allows you to use code from that program in writing your own program.

    ``u = input("Would you like me to draw a shape? Type yes or no: ")``

        Prompt the user to enter yes or no, and save the answer in the variable named u. Remember
        variables from before? It's like a container. The label on the outside of the container is u,
        and inside the container is the answer to the question that the user typed. If the user typed yes,
        then u is equal to yes, and if the user typed no, then u is equal to no. 

    ``if u == "yes":``

        The double equals sign checks to see if the thing on the left and the thing on the right 
        are equal. So, if the user typed yes, then our turtle will go ahead to do the code that's indented 
        below it. If the user didn't type yes then the turtle won't do the indented code. 
    

.. shortanswer:: sa-first_if
   :optional:

   Once you've run the code at least twice, and typed "yes" and "no", let's change it!
   What happens if you change line number 5 to say ``if u == "no"`` 
   (Hint: Try it -- and then run the program again...twice! Run it and type 'no' when 
   asked for input. Run it a second time, and type 'yes' when asked for input.)
