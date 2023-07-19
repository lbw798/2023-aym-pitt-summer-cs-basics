"""
  Welcome to the 2023 AYM Pittsburgh Summer Stem Camp.

  In this session we will walkthrough creating is a typing game using Python
  with Turtle.
    
  Python with Turtle lets you make graphics easily in Python.

  Check out the official docs here: https://docs.python.org/3/library/turtle.html

  Source Code for this game here: https://pythonturtle.academy/typing-game-with-python-and-turtle-source-code-included/

  This version was written by: Lucky
"""

import turtle
import random

screen = turtle.Screen()
screen_width = 700
screen_height = screen_width
screen.setup(screen_width, screen_height)
screen.bgcolor('beige')
turtle.bgpic('2023-aym-pitt-summer-cs-basics/admin/space_turtle.gif')
# Copy and paste from copy_file1.py starting here ..............................
screen.tracer(0, 0)
turtle.hideturtle()
turtle.up()
turtle.color('violet')
score_turtle = turtle.Turtle()
score_turtle.color('gold')
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


def increase_difficulty():
  global min_speed, max_speed
  min_speed += 1
  max_speed += 1
  screen.ontimer(increase_difficulty, 5000)


# Copy and paste from copy_file2.py starting here ..............................
def draw_game_over():
  turtle.goto(0, 0)
  turtle.color('red')
  turtle.write('GAME OVER',
               align='center',
               font=('Courier', int(round(0.050 * screen_width)), 'normal'))
  turtle.goto(0, -150)
  turtle.color('orange')
  turtle.write('Your Score is {}'.format(score),
               align='center',
               font=('Courier', int(round(0.040 * screen_width)), 'normal'))
  screen.update()


def draw_score():
  score_turtle.clear()
  score_turtle.goto(0.420 * screen_width, 0.400 * screen_height)
  score_turtle.write('{}'.format(score),
                     align='center',
                     font=('Courier', int(round(0.025 * screen_width)),
                           'normal'))
  screen.update()


def draw_letters():
  global game_over
  for i in range(len(letters)):
    lts[i].clear()
    lts[i].goto(pos[i])
    lts[i].write(letters[i],
                 align='center',
                 font=('courier', int(round(0.030 * screen_width)), 'normal'))
    pos[i][1] -= speeds[i]
    if pos[i][1] < -0.500 * screen_height:
      game_over = True
      draw_game_over()
      return
  screen.update()
  screen.ontimer(draw_letters, 50)


def get_random_letter():
  return chr(ord('a') + random.randrange(26))


def get_random_position():
  global screen_width, screen_height
  return [
    random.uniform(-0.450 * screen_width, 0.450 * screen_width),
    0.500 * screen_height
  ]


def key_press_handler(c):
  global score
  if c in letters:
    score += 1
    k = letters.index(c)
    while True:
      l = get_random_letter()
      if l not in letters:
        letters[k] = l
        break
    pos[k] = get_random_position()
    speeds[k] = random.uniform(min_speed, max_speed)
  else:
    score -= 1
  draw_score()


draw_score()
# Copy and paste from copy_file2.py ending here ................................

for _ in range(n):
  lts.append(turtle.Turtle())
  while True:
    l = get_random_letter()
    if l not in letters:
      letters.append(l)
      break
  speeds.append(random.uniform(min_speed, max_speed))
  pos.append(get_random_position())

for i in range(n):
  lts[i].speed(0)
  lts[i].hideturtle()
  lts[i].up()
  lts[i].color('black')

draw_letters()

# Copy and paste from copy_file3.py starting here ..............................
screen.onkey(lambda: key_press_handler('a'), 'a')
screen.onkey(lambda: key_press_handler('b'), 'b')
screen.onkey(lambda: key_press_handler('c'), 'c')
screen.onkey(lambda: key_press_handler('d'), 'd')
screen.onkey(lambda: key_press_handler('e'), 'e')
screen.onkey(lambda: key_press_handler('f'), 'f')
screen.onkey(lambda: key_press_handler('g'), 'g')
screen.onkey(lambda: key_press_handler('h'), 'h')
screen.onkey(lambda: key_press_handler('i'), 'i')
screen.onkey(lambda: key_press_handler('j'), 'j')
screen.onkey(lambda: key_press_handler('k'), 'k')
screen.onkey(lambda: key_press_handler('l'), 'l')
screen.onkey(lambda: key_press_handler('m'), 'm')
screen.onkey(lambda: key_press_handler('n'), 'n')
screen.onkey(lambda: key_press_handler('o'), 'o')
screen.onkey(lambda: key_press_handler('p'), 'p')
screen.onkey(lambda: key_press_handler('q'), 'q')
screen.onkey(lambda: key_press_handler('r'), 'r')
screen.onkey(lambda: key_press_handler('s'), 's')
screen.onkey(lambda: key_press_handler('t'), 't')
screen.onkey(lambda: key_press_handler('u'), 'u')
screen.onkey(lambda: key_press_handler('v'), 'v')
screen.onkey(lambda: key_press_handler('w'), 'w')
screen.onkey(lambda: key_press_handler('x'), 'x')
screen.onkey(lambda: key_press_handler('y'), 'y')
screen.onkey(lambda: key_press_handler('z'), 'z')

screen.listen()
# Copy and paste from copy_file3.py ending here ................................

increase_difficulty()
screen.mainloop()
