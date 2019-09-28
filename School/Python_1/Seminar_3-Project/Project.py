import turtle
import math

tr = turtle.Turtle()
tr.hideturtle()
tr.speed(0)
tr.penup()
tr.setpos(0, 100)
tr.pendown()


def poly(t, n, l, a):
    """Draws n line segments.

    t: turtle
    l: length of a segment
    a: angle (degrees) it curves
    """
    for i in range(n):
        t.forward(l)
        t.left(a)


def arc(t, r, a):
    """Draws an arc.

    t: turtle
    r: radius f the arc
    a: angle (degrees) of the arc
    """
    arc_l = 2 * math.pi * r * a / 360
    n = int(arc_l / 3) + 1
    step_l = arc_l / n
    step_a = a / n
    poly(t, n, step_l, step_a)


def petal(t, r, a):
    """Draws a petal.

    t: turtle
    r: radius
    a: angle (degrees)
    """
    for i in range(2):
        arc(t, r, a)
        t.left(180 - a)


def flower(t, petal_n, petal_length, petal_angle, stem_length, stem_angle, leaf_pitch, leaf_length, leaf_angle):
    # flower
    for petals in range(petal_n):
        petal(t, petal_length, petal_angle)
        t.lt(360.0 / petal_n)

    # stem
    t.setheading(270)
    t.right(stem_angle)
    arc(t, stem_length, 2 * stem_angle)

    # leaves
    t.setheading(0)
    t.left(leaf_pitch)
    poly(t, 15, leaf_length / 3, leaf_angle / 3)
    t.left(180 - 5 * leaf_angle)
    poly(t, 15, leaf_length / 3, leaf_angle / 3)
    t.setheading(180)
    t.right(leaf_pitch)
    poly(t, 15, leaf_length / 3, -leaf_angle / 3)
    t.right(180 - 5 * leaf_angle)
    poly(t, 15, leaf_length / 3, -leaf_angle / 3)


flower(tr, 7, 50, 60, 150, 40, 20, 10, 15)

turtle.mainloop()
