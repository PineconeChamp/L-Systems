import turtle

def draw_thing(moves: list, branch_count: int):

  little_guy = turtle.Turtle()
  little_guy.speed(0)
  little_guy.setheading(90)

  for i in range(branch_count):
    for x in range(len(moves[i])):
      little_guy.pendown()
      match moves[i][x]:
        case 'A':
          little_guy.forward(22)
        case 'B':
          little_guy.right(5)
        case 'C':
          little_guy.left(5)
          
    little_guy.penup()
    little_guy.setpos(0,0)
    little_guy.setheading(90)
  turtle.done()