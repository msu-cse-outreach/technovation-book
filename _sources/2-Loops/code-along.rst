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

``for`` **loop** --

Recall the example program from last week to draw a square?
A skeleton versed in Python will think to itself...

.. image:: img/talkingSkeleton.png
   :alt: A skeleton saying "By golly… must be a new coder… somebody's got to teach ‘em about LOOPS!"
   :align: center
   :width: 300

Why? 
Because the code we wrote repeats the same two instructions four
times in a row.
A ``for`` loop is meant for such situations.



If you can figure out the number of times the interpreter
should repeat some code before starting a loop.





.. raw:: html
         
    <div align="middle">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/QPX6fED8j4s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



