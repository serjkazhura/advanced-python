def is_comment(item):
  return isinstance(item, str) and item.startswith('#')

def execute(program):
  while program: # evaluates to true if the collection is not empty
    item = program.pop()
    if not is_comment(item):
      program.append(item)
      break
  else: # nobreak
    print("Empty")
    return

  pending = []

  while program:
    item = program.pop()
    if callable(item):
      try:
        result = item(*pending) # calling the item passing pending as arguments - *pending
                                # e.g. a collection will be a collection of arguments
      except Exception as e:
        print("Error", e)
        break
      program.append(result)
      pending.clear()
    else:
      pending.append(item)
  else: # nobreak
    print("Program successful")
    print("Results", pending)

  print("Finished")

if __name__ == '__main__':
  import operator

  program = list(
    reversed(
      (
        "# A short stack program to add",
        "# and multiply the constants",
        5,
        2,
        operator.add,
        3,
        operator.mul
      )
    )
  )

  execute(program)

