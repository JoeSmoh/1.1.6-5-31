#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#create body 

legs = 8
leglength = 70
legAngle = 160 / legs
spider.pensize(5)
legs2 = 0
#configure legs

#draw legs 
while (legs2 < legs):
  spider.goto(0,20)
  spider.setheading(legAngle*legs2-30)
  spider.forward(leglength)
  legs2 = legs2 + 2

legs2=0
while (legs2 < legs):
  spider.goto(0,20)
  spider.setheading(legAngle*legs2-30 +180)
  spider.forward(leglength)
  legs2 = legs2 + 2

#eyes
spider.goto(0,0)
spider.pencolor("white")
spider.circle(5)

spider.goto(10,5)
spider.pencolor("white")
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()