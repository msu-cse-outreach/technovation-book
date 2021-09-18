.. image:: img/Technovation-yellow-gradient-background.png
    :width: 500
    :align: center

Cheat Sheet
:::::::::::::::::::::::::::::::::::::::::::

The tables below contain brief reminders of the instructions and operators that we use
in our examples. You can find more complete descriptions of these and many others online.

* `Turtle Instructions`_
* `Python Operators`_
* `Python Instructions`_


Turtle Instructions
------------------------------

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - Instruction
     - Effect
   * - `import turtle`
     - Brings `turtle` into the program to use with instructions.

       `turtle` will start in the middle of the screen, facing right (0 degrees),
       drawing when it moves, and using black for both drawing lines and filling regions.
   * - `turtle.forward(L)`
     - Moves `turtle` forward by `L` pixels.
   * - `turtle.backward(L)`
     - Moves `turtle` backward by `L` pixels.
   * - `turtle.right(D)`
     - Turns `turtle` clockwise by `D` degrees.
   * - `turtle.left(D)`
     - Turns `turtle` counter-clockwise by `D` degrees.
   * - `turtle.goto(X,Y)`
     - Moves `turtle` along a straight line to the point with coordinates `(X,Y)`
   * - `turtle.up()`
     - Makes `turtle` stop drawing as it moves.
   * - `turtle.down()`
     - Makes `turtle` draw as it moves.
   * - `turtle.color(C1,C2)`
     - Sets the color `turtle` uses for drawing lines to `C1` and the color
       `turtle` uses for filling regions to `C2`.

       If the instruction contains only one input (`C1`) then sets both colors
       to `C1`.
   * - `turtle.begin_fill()`
     - Marks the start of a region to be filled.
   * - `turtle.end_fill()`
     - Marks the end of a region to be filled.

       The region is determined as the smallest *convex* region
       containing all the points that `turtle` passes through in executing
       the instructions since the most recent `turtle.begin_fill()` instruction.
       (It is an error if `turtle.end_fill()` has already been executed since
       the most recent `turtle.begin_fill()` instruction or no prior `turtle.begin_fill()`
       instuction was executed.)
   * - `turtle.write(S, font=(N,Z,Y), align=A, move=B)`
     - Writes string `S` at the turtle's current position.
       Uses the font family named `N`, the *point size* `Z``, and *style* `Y`
       (e.g., `'normal'`, `'itallic'`, `'bold'`);
       aligns `S` as indicated by `A` (one of `'left'`, `'right'`, or `'center'`);
       and moves the turtle if `B` is `True`; does not move the turtle
       if `B` is `False`.

       Any of the assignments may be omitted, in which case the default values
       are used: `font=('Arial',8,'normal')`, `align='left'`, `move=False`.


Python Operators
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - Operator
     - Effect
   * - `int(S)`
     - Produces an `int` version of `S`, if `S` is a string denoting an integer.

       For example, `int("365")` produces the `int` 365.
   * - `float(S)`
     - Produces a `float` version of `S`, if `S` is a string denoting a `float`.

       For example `float("3.1416")` produces the `float` 3.1416.
   * - `str(N)`
     - Produces a `str` version of `N`.

       For example, `str(1/10)` produces "0.1".
   * - `a + b`
     - If `a` and `b` are numeric, produces the number obtained by adding them together.

       If `a` and `b` are strings, returns the string obtained by combining them
       into one, with the characters from `a` followed immediately by the characters
       from `b`.



Python Instructions
-------------------------

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - Instruction
     - Effect
   * - `var = exp`
     - Executes `exp` and assigns the value so produced to variable `var`.

       Creates `var` if it does not already exist; otherwise, updates the value
       of `var`.
