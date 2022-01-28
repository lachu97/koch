import turtle
def koch_curve(t, iterations, length, shortening_factor, angle): 
     if iterations == 0:
          t.forward(length)
     else:
          iterations = iterations - 1
          length = length / shortening_factor    
          koch_curve(t, iterations, length, shortening_factor, angle)
          t.left(angle)
          koch_curve(t, iterations, length, shortening_factor, angle)
          t.right(angle * 2)
          koch_curve(t, iterations, length, shortening_factor, angle)
          t.left(angle)
          koch_curve(t, iterations, length, shortening_factor, angle)

t = turtle.Turtle()
t.hideturtle()
t.speed(50)
t2=turtle.Turtle()
t2.speed(70)
t2.penup()
t2.goto(-200, 0)
t2.pendown()
for i in range(200):
  koch_curve(t2, 4, 200, 2, 60)
  koch_curve(t, 4, 200, 3, 60)
  t.right(120)
  t2.right(120)
turtle.mainloop()