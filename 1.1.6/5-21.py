#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

legs = 6
leglength = 70
legAngle = 380 / legs
spider.pensize(5)
legs2 = 0
while (legs2 < legs):
  spider.goto(0,0)
  spider.setheading(legAngle*legs2)
  spider.forward(leglength)
  legs2 = legs2 + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()