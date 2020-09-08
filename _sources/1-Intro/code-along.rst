Code Along
:::::::::::::::::::::::::::::::::::::::::::

We know how boring online classes are when the teacher shares their screen and walks through a PowerPoint---after all,
we're students ourselves! Rather than bore you with a formal lecture, we're going to make
Virtual Technovation interactive. This page *is* today's lesson---we'll work through the definitions, explanations,
examples and exercises together!

What is Programming?
---------------------

**Programming** is the process of writing computer **programs**, which are nothing more than
*a set of instructions which tell a computer how to accomplish a task.* In this sense,
programming isn't all that different from dog training---just as you would show your dog a set
of gestures to teach it a new trick, you can write a program to teach a computer a new trick!

A programming **language** is nothing more than the words and phrases you use to write a computer
program. Just as we can say "Hola, me llamo Andrew" in Spanish to mean the same thing as "Hello, my name is Andrew"
in English, we can give computers instructions in different languages. In Technovation, we'll be
learning the programming language Python.

To recap:

    **Programming**: the process of writing computer programs

    **Program**: a set of instructions which tell a computer how to accomplish a task

    **Programming Language**: the specific words and phrases used to write a program


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