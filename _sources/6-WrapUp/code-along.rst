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

    ``answer = input("Would you like me to draw a circle? Enter 'yes' or 'no': ")``

        Prompt the user to enter ``yes`` or ``no``, and save the answer in the variable 
        named ``answer``. 
        Remember variables from before? 
        The variable ``answer`` is like a container. 
        The label on the outside of the container is ``answer``,
        and inside the container is the string of characters that the user typed. 
        If the user typed ``yes``,
        then ``answer`` is equal to ``"yes"``, 
        and if the user typed ``no``, then ``answer`` is equal to ``"no"``. 

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
        

