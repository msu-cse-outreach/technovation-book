======
Andrew
======

Welcome to Technovation! We're thrilled for you to join us this fall, and
think you'll have a blast.

Multiple Choice Questions
::::::::::::::::::::::::::


Q1
------

.. mchoice:: question1
    :correct: a
    :answer_a: Python
    :answer_b: Javascript
    :answer_c: HTML
    :answer_d: C++
    :feedback_a: Correct!
    :feedback_b: Try again.
    :feedback_c: Try again.
    :feedback_d: Try again.

    Which programming language will we be using in Technovation?

Q2
------

.. mchoice:: question2
    :correct: c
    :answer_a: Scikit-Learn
    :answer_b: Numpy
    :answer_c: Turtle
    :answer_d: TensorFlow
    :feedback_a: Try again.
    :feedback_b: Try again.
    :feedback_c: Correct!
    :feedback_d: Try again.

    Which package will we be using in Technovation?

Q3
------

.. mchoice:: question3
    :correct: b
    :answer_a: ``square``
    :answer_b: ``circle``
    :answer_c: ``oval``
    :answer_d: ``turn``
    :feedback_a: Try again.
    :feedback_b: Correct!
    :feedback_c: Try again.
    :feedback_d: Try again.

    Which command will draw a circle?



Fill in the Blank Questions
:::::::::::::::::::::::::::

Q4
---

.. fillintheblank:: question4
   
   Fill in the blank to create a for loop in Python:

   ``|blank| i in range(10):``

   -   :for: Correct.
       :x: Incorrect. Try ``for``.


Matching Questions
:::::::::::::::::::

Q5
---

.. dragndrop:: question5
   :feedback: Keep trying!
   :match_1: ____ in range(10):|||for
   :match_2: ____("This function takes user input.")|||input
   :match_3: ____("This function prints output.")|||print

   Match to create proper Python syntax.

Videos
:::::::::::::::::::

Q6
---

.. youtube:: fC9da6eqaqg

Code
::::::

Q7
---

.. activecode:: question7
   :language: python

   Write a function that adds two numbers.
   ~~~~
   def add(a, b):
   
   ====
   # unit tests

   from unittest.gui import TestCaseGui

   class addTests(TestCaseGui):

       def addTest(self):
           self.assertEqual(add(2,2), 4, "Message")
           self.assertAlmostEqual(add(2.0,3.0), 5.0, 5, "Message")
           self.assertEqual(add(3,-5), -2, "Message")

   addTests().main()

Q8
---

.. activecode:: question8
   :language: python

   Write a function that leads a Turtle in a square.
   ~~~~
   import turtle
   t = turtle.Turtle()

   def square():
       for i in range(4):
           t.forward(100)
           t.left(90)

   square()
   