import turtle


user_color = turtle.textinput("Color Chooser", "Enter a color (red, blue, etc.):")
if not user_color:
    user_color = "red"


user_angle = turtle.numinput("Angle Picker", "Enter an angle (0-180):", default=170, minval=0, maxval=180)


if user_angle is None:
    user_angle = 170

turtle.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.color(user_color)

for i in range(5000):

    t.forward(i * 0.5)
    t.left(user_angle)
    t.forward(i * 0.5)

t.color("black")
turtle.done()
