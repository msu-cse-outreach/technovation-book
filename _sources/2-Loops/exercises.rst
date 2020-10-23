.. image:: ../img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center
    :alt: Technovation logo


Practice Makes Perfect
:::::::::::::::::::::::::::::::::::::::::::

.. table:: Turtle Commands
   :widths: auto
   :align: left

   ==========================  ========================
   Command                     What does it do?
   ==========================  ========================
   ``forward( distance )``     Move forward a specified distance
   ``backward( distance )``    Move backward a specified distance
   ``left(90)``                Turns 90 degrees to the left (you can use any angle, not just 90!)
   ``right(90)``               Turns 90 degrees to the right
   ``circle( radius )``        Draws a circle with the specified radius
   ``penup()``                 Stop leaving a trail
   ``pendown()``               Start drawing a trail
   ``for i in range( n ):``    Repeat *n* times
   ==========================  ========================

If you don't remember what they do, give them a try below!

.. activecode:: command-review-wk2
   :language: python
   :nocodelens:
   
   import turtle
   
   turtle.forward(100)
   turtle.backward(100)

   # try out some other commands here!


|
|
|
| Let's take another look at drawing a square. How could we re-write it using a loop?

.. activecode:: square-loop
   :language: python
   :nocodelens:
   
   import turtle
   
   turtle.forward(100)
   turtle.left(90)
   
   turtle.forward(100)
   turtle.left(90)

   turtle.forward(100)
   turtle.left(90)

   turtle.forward(100)
   turtle.left(90)

|
|

.. image:: img/dashed-line.png
   :alt: Image of dashed line drawn with Python Turtle
   :align: center
   :width: 300

| Let's use what we know about loops to draw a dashed line across the entire box!
| The code below draws two dashes. See if you can modify it to use a loop!

.. activecode:: dashed-line
   :language: python
   :nocodelens:
   
   import turtle
   
   # draw the first dash
   turtle.forward(10)

   # pick the pen up to leave white space between dashes
   turtle.penup()   
   turtle.forward(10)

   # put the pen down and draw the second dash
   turtle.pendown()
   turtle.forward(10)

   turtle.penup()
   turtle.forward(10)

|
|

.. image:: img/triangle.png
   :alt: Image of a triangle drawn with Python Turtle
   :width: 33 %
.. image:: img/pentagon.png
   :alt: Image of a pentagon drawn with Python Turtle
   :width: 33 %
.. image:: img/hexagon.png
   :alt: Image of a hexagon drawn with Python Turtle
   :width: 33 %

| Why stop with squares? Shapes with any number of sides can be drawn using a loop!
| Start with your code that draws a square. Then, change the number of times the loop
  repeats and the angle that you turn each time to see if you can draw these shapes.

.. activecode:: shapes-loop
   :language: python
   :nocodelens:
   
   import turtle

|
|

.. image:: img/circle-row.png
   :alt: Image of a row of cirlces drawn with Python Turtle
   :align: center
   :width: 300

| Try converting you dashed line into a row of circles! Let's draw 20 circles, each with a radius of 10.

.. activecode:: circle-row
   :language: python
   :nocodelens:
   
   import turtle

|
|

.. image:: img/square-row.png
   :alt: Image of a row of squares drawn with Python Turtle
   :align: center
   :width: 300

| Try drawing a row of squares!

.. reveal:: square-row-hint
   :showtitle: Show hint
   :hidetitle: Hide hint
    
    For this problem, try using two loops! One to draw each square
    (same as in the first problem on this page), and another to draw
    the square *multiple times*

.. activecode:: square-row
   :language: python
   :nocodelens:
   
   import turtle

|
|

.. image:: img/plus.png
   :alt: Image of a plus sign drawn with Python Turtle
   :align: center
   :width: 300

| Try drawing a plus sign using a loop!
| If you're not sure how to do it with a loop, try writing it out line by line first.
  Once you've got it drawing a plus sign, see if you can put any repeated code in a loop!

.. activecode:: plus
   :language: python
   :nocodelens:
   
   import turtle
   
|
|

.. image:: img/asterisk.png
   :alt: Image of an asterisk drawn with Python Turtle
   :align: center
   :width: 300

| Now try modifying your code from the plus sign into an asterisk!
| Hint: you'll need to change the number of repetitions and the angle that you're turning each time

.. activecode:: asterisk
   :language: python
   :nocodelens:
   
   import turtle