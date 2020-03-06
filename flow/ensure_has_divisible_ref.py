def can_divide(items, divisor):
  for item in items:
    if item % divisor == 0:
      return item

  items.append(divisor)
  return divisor

def execute():
  items = [2, 36, 25, 9]
  divisor = 12
 
  divident = can_divide(items, divisor)
  
  print("{items} contains {divident} which is a multiple of {divisor}".format(**locals()))
  # note the use of locals - this are all the local variables

if __name__ == '__main__':
  execute()