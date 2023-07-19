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