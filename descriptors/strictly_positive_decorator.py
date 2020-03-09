from weakref import WeakKeyDictionary

class Positive:

  def __init__(self):
    self._instance_data = WeakKeyDictionary()

  def __get__(self, instance, owner):
    #that means that we are using class retrieval rather than instance retrieval
    if instance is None:
      return self
    return self._instance_data[instance]
  
  def __set__(self, instance, value):
    if value <= 0:
      raise ValueError("Value has to be > 0")
    self._instance_data[instance] = value
  
  def __delete__(self, instance):
    raise ArithmeticError("Cannot delete property")