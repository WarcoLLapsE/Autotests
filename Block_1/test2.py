import turtle


def hexagon(side):
    turtle.shape('turtle')
    angle = 0
    for _ in range(6):
        turtle.setheading(angle)
        turtle.forward(side)
        angle += 60


# angle_honeycomb = 0
# while angle_honeycomb != 360:
#     hexagon(80)
#     turtle.heading(angle_honeycomb)
#     angle_honeycomb += 30

hexagon(80)
turtle.forward(160)
hexagon(80)
