class Vector:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # print a nice text representation
  def __repr__(self):
    return "{}({} {})".format(self.__class__.__name__, self.x, self.y)

class CustomVector:

  def __init__(self, **coords):
    private_coords = { '_' + k: v for k,v in coords.items()}
    self.__dict__.update(private_coords)

  # this is called for every attribute call
  def __getattribute__(self, name: str):
    pass

  # this is called only when normal attribute lookup fails
  def __getattr__(self, name):
    private_name = '_'+name
    return self.__dict__[private_name]

  def __setattr__(self, name: str, value) -> None:
    raise AttributeError("Cannot find attribute named {!r}".format(name))

  def __delattr__(self, name: str) -> None:
    raise AttributeError("Cannot delete attribute named {!r}".format(name))

  def __repr__(self):
    return "{}({})".format(
      self.__class__.__name__, 
      ', '.join("{k}={v}".format(k=k[1:], v=self.__dict__[k]) for k in sorted(self.__dict__.keys()))
    )

class Resistor:

  # slots - to save memory
  __slots__ = ['reristance_ohms', 'tolerance_percent', 'power_watts']

  def __init__(self, reristance_ohms, tolerance_percent, power_watts):
    self.reristance_ohms = reristance_ohms
    self.tolerance_percent = tolerance_percent
    self.power_watts = power_watts


def main():
  v = CustomVector(p=5,q=6)
  print(v)
  print(dir(v))
  print(v.__dict__)
  print(v.q)
  v.q = 1000

if __name__ == '__main__':
  main()