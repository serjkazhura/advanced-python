def execute():
  items = [2, 36, 25, 9]
  divisor = 12

  for item in items:
    if item % divisor == 0:
      found = item
      break
  else: # nobreak
        # useful to hande a not found item
    items.append(divisor)
    found = divisor
  
  print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))
  # note the use of locals - this are all the local variables

if __name__ == '__main__':
  execute()