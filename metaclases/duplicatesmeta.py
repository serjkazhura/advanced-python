
class OneShotClassNamespace(dict):

  def __init__(self, name, existing=None):
    super().__init__()
    self._name = name
    if existing is not None:
      for k, v in existing:
        self[k] = v
      
  def __setitem__(self, key, value):
    if key in self:
      raise ValueError("Cannot reassign existing class attribute {!r} of {!r} class".format(key, self._name))
    super().__setitem__(key, value)

#############

class ProhibitDuplicatesMeta(type):

  @classmethod
  def __prepare__(mcs, name, bases):
    return OneShotClassNamespace(name)

#############

class Dodgy(metaclass=ProhibitDuplicatesMeta):

  def method(self):
    return "first definition"

  def method(self):
    return "second definition"
    
############

def main():
  d = Dodgy()
  print(d.method())

if __name__ == "__main__":
  main()