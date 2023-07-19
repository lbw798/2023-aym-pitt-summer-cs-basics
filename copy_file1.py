# Copy and paste from copy_file1.py starting here ..............................
screen.tracer(0, 0)
turtle.hideturtle()
turtle.up()
turtle.color('red')
score_turtle = turtle.Turtle()
score_turtle.color('red')
score_turtle.up()
score_turtle.hideturtle()
turtle.goto(0.350 * screen_width, 0.400 * screen_height)
turtle.write('Score: ',
             align='center',
             font=('Courier', int(round(0.025 * screen_width)), 'normal'))

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-0.500 * screen_width, -0.500 * screen_height)
mypen.pendown()
mypen.pensize(3)
mypen.color('blueviolet')
for side in range(4):
  mypen.forward(screen_width)
  mypen.left(90)
mypen.hideturtle()
screen.update()

min_speed = 0.5
max_speed = 2
letters = []
speeds = []
pos = []
lts = []
n = 10
game_over = False
score = 0
# Copy and paste from copy_file1.py ending here ................................