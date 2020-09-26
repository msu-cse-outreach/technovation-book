import turtle

turtle.speed(10)

# draw green base triangle
turtle.up()
turtle.goto(-100, -50)
turtle.color("green")
turtle.down()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

# draw blue 60deg-rotated triangle
turtle.up()
# eye ball how far down to go (they don't know math module yet)
turtle.goto(0, -110)
turtle.left(60)
turtle.color("blue")
turtle.down()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

