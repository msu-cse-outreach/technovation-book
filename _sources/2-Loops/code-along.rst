.. image:: ../img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Learning to Code
:::::::::::::::::::::::::::::::::::::::::::

Variables and assignment
-------------------------------------------

A *variable* is a name that you use in your program to stand for a data object. 
You should choose meaningful names.
For example, you might use ``radius`` to stand for the length to make the radius
of a circle and ``area`` to stand for its area.
You use variables in your program to form *expressions*.
Informally, an expression is just code that an *interpreter* can evaluate to 
produce a data object.
For example, if ``radius`` stands for ``50``, then ``2 * radius``
stands for ``100``, which is the diameter of a circle of radius ``50``.


In Python, a variable name must start with a letter (``a``--``z``, ``A``--``Z``) or
an underscore (``_``), and can contain only letters, digits (``0``--``9``) and 
underscores.

.. clickablearea:: variablenames
   :question: Click on the names that you could use for a variable in Python.
   :table:
   :correct: 1,1;1,2;1,3;2,2;3,1
   :incorrect: 2,1;2,3;3,2;3,3

   
   +------------+------------+------------+
   | x          | area51     | _square    |
   +------------+------------+------------+
   | l3.x       | Zero       | area-51    |
   +------------+------------+------------+
   | __16_      | a 1        | 6_dozen    |
   +------------+------------+------------+




An *assignment* instruction has the form ``var = expression``
where ``var`` stands for a variable name and ``expression`` stands for an expression.
Executing the assignment makes ``var`` stand for the data object produced
by evaluating ``expression``.
After the assignment, ``var`` can be used as a "stand in" for this data object.
We refer to the data object that a variable stands for more simply as 
the variable's *value*.

A variable is like a *container* (e.g., a desk drawer or a file folder) 
that can hold just one object and that is labelled by the variable name. 
In this analogy, an assignment to the variable is like putting something in 
this container.
The term "variable" is used because the value can change---since 
only one object fits in the container (variable), assigning it a new object
(value) replaces any object (value) already in it.


We illustrate this analogy using *Python Tutor*, 
a tool for visualizing how an interpreter executes a Python program. 
It lets you *step* through your program one line at a time and shows
you how the values of variables change.


.. codelens:: circle_calculations
   
   # Calculate the diameter, circumference and area of
   # a circle of radius 50
   
   from math import pi      # the constant pi
   
   radius = 50
   diameter = 2 * radius
   circumference = diameter * radius
   area = 2 * pi * radius * radius


There is a lot more to learn about variables and assignment to become expert
in programming.
Mike's "Data Types and Variables" rap touches on the very important notion of
the *data type* of an object.

.. raw:: html

   <div align="middle">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/m7szVmMta-o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   </div>

But one thing in this rap is different in Python: Unlike most languages, you
do not say what the type of a data object is in a Python program;
rather, the interpreter figures out the data type of an object based on how your 
program creates and uses it.
We won't go into further details now since we can do a lot with Turtle Graphics
with just a basic understanding of these notions.



Loops
-----------------------

Do you ever get tired of repeating the same instructions over and over and over and over and over and ... over again? Or, after too many repetitions, do you start making mistakes?

One good thing about computers is that they don't! 
*Loops* are instructions that tell the interpreter to repeat a
section of code as many times as needed.
Python has two kinds of loop instructions--``for`` loops and ``while`` loops.

**The** ``for`` **loop**:

Recall the example program from last week to draw a square?
A skeleton versed in Python will mutter to itself...

.. image:: img/talkingSkeleton.png
   :alt: A skeleton saying "By golly… must be a new coder… somebody's got to teach ‘em about LOOPS!"
   :align: center
   :width: 300

Why? 
Because the code we wrote repeats the same two instructions four
times in a row.
A ``for`` loop is meant exactly for such situations.

Our skeleton would write this program as shown below.
Run this code to see that it draws a square.

.. activecode:: ac-for-loop-square
    :language: python
    :nocodelens:
    
    # draw a square of a given side length
    import turtle
    
    side_len = 100
    
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)

The moral: If you can figure out the number of times the interpreter
should repeat some code, then use a ``for`` loop!

The simplest kind of ``for`` loop has the general form:

| ``for var in range(int_exp):``
|       ``loop_body_code``

where ``var`` stands for a variable, ``int_exp`` stands for an *integer
expression* (an expression that produces an integer when evaluated), 
and ``loop_body_code`` stands
for code that should be executed ``int_exp`` number of times.

Some important terminology and rules:

* The words ``for`` and ``in`` are called *keywords*.
  We'll learn lots more keywords in the meetings ahead.
  Never use a keyword for the name of a variable because the interpreter 
  uses keywords to figure out what kind of instruction you want it to execute.
  
* The code ``loop_body_code`` is called the *body* of the loop.
  It consists of one or more Python instructions.
  Each instruction in the body *must* be indented and the indentation
  must be consistent (the same number of spaces) throughout the entire program.
  The interpreter tells where the body of a loop
  starts and ends by the indentation.

  
**Code Along**

.. activecode:: ac-for-loop-triangle
   :language: python
   :nocodelens:
   
   Replace the last comment with a for-loop that 
   draws an equilateral triangle (with side-lenth 200 pixels).
   
   ~~~~
   
   # draw a triangle of side length 200 (pixels)
   
   import turtle
   
   side_length = 200
   
   # replace the comment with a for loop


Some more important terminology and rules:
  
* The word ``range`` is the name of a Python *standard library function*.
  We'll learn about functions next week.
  For now, you just need to know that evaluation of ``range(int_exp)`` 
  produces a sequence of ``int_exp`` integers.
  Specifically, it produces the sequence:
  ``0``, ``1``, ``2``, ... , ``int_exp - 1``.
  (In computer science, it is convenient to start counting at ``0`` instead
  of ``1``.)
  
* The variable in the first line of a ``for`` loop is called the *loop variable*. 
  
* Each execution of the loop body is called an *iteration* of the loop.
  
* Just before each loop iteration (execution of the loop body), the
  interpreter assigns ``var`` a value from ``range(int_exp)``, starting
  with ``0`` and increasing in order.
  
The last of these rules allows the code performed on each iteration of a
loop to depend on what iteration is being executed.
The following example illustrates this capability.

.. activecode:: ac-bulls-eye
   :language: python
   :nocodelens:
   
   # "bull's eye" - three concentric cirles spaced 50 pixels apart
   import turtle
   
   spacing = 50
   
   for n in range(3):
   
       # set the radius for this iteration of the loop
       radius = (n+1) * spacing
       
       # get into position
       turtle.up()
       turtle.goto(0, -radius)
       
       turtle.down()
       turtle.circle(radius)
   

NOTE: THE FOLLOWING IS A SANDBOX I'M USING IN DEVELOPING
EXERCISES. I'M USING IT TO DEVELOP A PARSONS PROBLEM --
YOU CAN IGNORE IT. THE RAP IS PROBABLY GOING TO COME OUT, TOO

.. activecode:: ac-stacked-circles
   :language: python
   :nocodelens:
   
   import turtle
   
   small_radius = 25
   turtle.setposition(0, 4*small_radius)
   
   for n in range(3):
       radius = (n+1) * small_radius
       turtle.circle(radius)

   
   






.. raw:: html
         
    <div align="middle">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/QPX6fED8j4s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



