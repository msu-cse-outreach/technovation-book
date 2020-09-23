.. image:: ../../_static/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Learning to Code
:::::::::::::::::::::::::::::::::::::::::::

Why learn Coding?
---------------------

.. image:: ../../_static/computerScienceClipartKeyDOTcom_3061179.png
    :width: 400
    :align: center
    :alt: image of children and benefits of learning to code (ClipartKey.com 3061179)

* Develop critical thinking skills

* Learn how to *create* --- not just use --- technology

* Fuel innovation and discovery in *all* disciplines 

Terminology
---------------------

*Code* refers to a list of intructions which a computer can follow to complete some job.

Code is commonly also called a *program*. 

*Coding* is the process of writing a program (code).

A computer *executes* a program to complete the job described by the program.

A *programming language* gives the words and the rules to use for writing a program.



The distinctions between these terms can be illustrated by analogy. What do you think?

.. image:: ../../_static/cooking-clipart-libraryDOTcomClipart26transparent.png
    :width: 300
    :align: center
    :alt: image of teens following a recipe (clipart-library.com/clipart/26)

.. dragndrop:: dnd-terminology-recipe
    :match_1: Rules for writing down recipes|||Programming language
    :match_2: A pizza recipe|||A program (code)
    :match_3: Cooking a cheese pizza|||Executing the program
    :match_4: Writing down the recipe for your favorite pizza|||Programming (coding)

    Drag the phrase on the left to the coding concept it is most analogous to.


.. image:: ../../_static/teachingDogTricksCoolCLIPS_vc016297.png
    :width: 300
    :align: center
    :alt: clipart of dog pondering an equation involving bones (CoolCLIPS_vc016297)


.. dragndrop:: dnd-terminology-pet-tricks
    :match_1: The gestures and sounds that your dog understands the meaning of|||Programming language
    :match_2: A series of gestures and sounds that you can give your dog to get it to perform a stupid pet trick|||A program (code)
    :match_3: Commanding your dog to perform a stupid pet trick|||Executing the program
    :match_4: Writing an email message telling a friend how to get your dog to perform a stupid pet trick|||Programming (coding)

    Drag the phrase on the left to the coding concept it is most analogous to.


.. image:: ../../_static/teachingDogTricksClipartsDOTzoneClipart675010.png
    :width: 300
    :align: center
    :alt: image of a trainer trying to get a dog to jump through a hoop (Cliparts.zone/clipart/675010)



Tracy the Turtle
------------------

We'll be learning Python by writing programs which teach Tracy the Turtle how
to draw pictures! Think of Tracy as your new virtual pet---instead of teaching her to roll over or sit with
gestures like you might do to train a dog, however, you'll be teaching Tracy new tricks with computer programs.

For example, we might want to teach Tracy how to draw a square with a computer program.
The following snippet of code does exactly that!

.. activecode:: tracy_square
    :language: python
    :nocodelens:

    Press the green "Run" button to watch Tracy draw a square by following the instructions in our program!
    ~~~~
    import turtle
    tracy = turtle.Turtle()

    tracy.forward(100)
    tracy.left(90)

    tracy.forward(100)
    tracy.left(90)

    tracy.forward(100)
    tracy.left(90)

    tracy.forward(100)
    tracy.left(90)

Pretty neat, isn't it? 

What happens when you modify these instructions by changing the numbers on
lines 5 and 6? Give it a shot!

Our First Program
-------------------

Let's try to teach Tracy how to draw a triangle instead of a square. We'll work together, but
make sure to write down our code in your window and run it yourself!

.. activecode:: tracy_triangle
    :language: python
    :nocodelens:

    Write a program to instruct Tracy to draw a triangle.
    ~~~~
    import turtle
    tracy = turtle.Turtle()

    # your code here

That wasn't so bad, was it?

Adding Complexity
------------------

Can we teach Tracy how to draw a hexagon? Let's give it a shot!

.. activecode:: tracy_hexagon
    :language: python
    :nocodelens:

    Write a program to instruct Tracy to draw a hexagon.
    ~~~~
    import turtle
    tracy = turtle.Turtle()

    # your code here

What about a Figure 8? Let's try it out!

.. activecode:: tracy_fig8
    :language: python
    :nocodelens:

    Write a program to instruct Tracy to draw a Figure 8.
    ~~~~
    import turtle
    tracy = turtle.Turtle()

    # your code here