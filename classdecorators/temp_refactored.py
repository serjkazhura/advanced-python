import functools

def invariant(predicate):

  def invariant_checking_class_decorator(cls):

    method_names = [name for name, attr in vars(cls).items() if callable(attr)]
    for method_name in method_names:
      _wrap_method_with_invariant_checking_proxy(cls, method_name, predicate)
    return cls
  
  return invariant_checking_class_decorator

def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
  method = getattr(cls, name)
  assert callable(method)

  @functools.wraps(method)
  def invariant_checking_method_decorator(self, *args, **kwargs):
    result = method(self, *args, **kwargs)
    if not predicate(self):
      raise RuntimeError("Class invariant {!r} violated for {!r}".format(predicate.__doc__, self))
    return result

  setattr(cls, name, invariant_checking_method_decorator)

####################

def not_below_absolute_zero(temp):
  """Temp not below absolute zero."""
  return temp._kelvin >= 0


@invariant(not_below_absolute_zero)
class Temperature:

  def __init__(self, kelvin):
    self._kelvin = kelvin
  
  def get_kelvin(self):
    return self._kelvin
  
  def set_kelvin(self, val):
    self._kelvin = val

###################

def main():
  t = Temperature(5.0)
  # t1 = Temperature(-6.0) # this will fail
  t.set_kelvin(-10.0) # this fails as well

if __name__ == "__main__":
  main()