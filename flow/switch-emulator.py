def go_east(prev_position):
  i, j = prev_position
  position = (i + 1, j)
  return position

def go_south(prev_position):
  i, j = prev_position
  position = (i, j - 1)
  return position

def go_north(prev_position):
  i, j = prev_position
  position = (i, j + 1)
  return position

def go_west(prev_position):
  i, j = prev_position
  position = (i - 1, j)
  return position

def look(prev_position):
  return prev_position 

def quit(prev_position):
  return None

def play():
  position = (0,0)
  alive = True

  while position:
    locations = {
      (0,0): lambda: print("u r in a maze of twisty passages, all alike"),
      (1, 0): lambda: print("u r on the road in a dark forest. to the north u can see a tower"),
      (1, 1): lambda: print("there is a tall tower here, with no obvious door. a path leads east")
    }

    try: 
      location_action = locations[position]
    except KeyError:
      print("There is nothing here")
    else:
      location_action()

    command = input() # read a string from stdio

    actions = {
      'N': go_north,
      'E': go_east,
      'S': go_south,
      'W': go_west,
      'L': look,
      'Q': quit
    }

    try:
      command_action = actions[command]
    except KeyError:
      print("I don't understand")
    else:
      position = command_action(position)

  print("Game over")

if __name__ == '__main__':
  play()