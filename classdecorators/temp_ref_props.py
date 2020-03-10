import functools
from pprint import pprint as pp

def invariant(predicate):

  def invariant_checking_class_decorator(cls):

    method_names = [name for name, attr in vars(cls).items() if callable(attr)]
    for method_name in method_names:
      _wrap_method_with_invariant_checking_proxy(cls, method_name, predicate)

    property_names = [name for name, attr in vars(cls).items() if isinstance(attr, property)]
    for property_name in property_names:
      _wrap_property_with_invariant_checking_proxy(cls, property_name, predicate)

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

def _wrap_property_with_invariant_checking_proxy(cls, name, predicate):
  prop = getattr(cls, name)
  assert isinstance(prop, property)

  invariant_checking_proxy = InvariantCheckingPropertyProxy(prop, predicate)

  setattr(cls, name, invariant_checking_proxy)

####################

class InvariantCheckingPropertyProxy:

  # referent = property
  # predicate = property condition
  def __init__(self, referent, predicate):
    self._referent = referent
    self._predicate = predicate
  
  def __get__(self, instance, owner):
    if instance is None:
      return self._referent
    result = self._referent.__get__(instance, owner)
    if not self._predicate(instance):
      raise RuntimeError("Class invariant {!r} violated for {!r}".format(self._predicate.__doc__, instance))
    return result

  def __set__(self, instance, value):
    result = self._referent.__set__(instance, value)
    if not self._predicate(instance):
      raise RuntimeError("Class invariant {!r} violated for {!r}".format(self._predicate.__doc__, instance))
    return result

  def __delete__(self, instance):
    result = self._referent.__delete__(instance)
    if not self._predicate(instance):
      raise RuntimeError("Class invariant {!r} violated for {!r}".format(self._predicate.__doc__, instance))
    return result

####################

def not_below_absolute_zero(temp):
  """Temp not below absolute zero."""
  return temp._kelvin >= 0

def below_absolute_hot(temp):
  """Temp below absolute hot"""
  return temp._kelvin <= 1.416785e32

@invariant(below_absolute_hot)
@invariant(not_below_absolute_zero)
class Temperature:

  def __init__(self, kelvin):
    self._kelvin = kelvin
  
  def get_kelvin(self):
    return self._kelvin
  
  def set_kelvin(self, val):
    self._kelvin = val

  @property
  def celsius(self):
    return self._kelvin - 273.15
  
  @celsius.setter
  def celsius(self, value):
    self._kelvin = value + 273.15
  
  @property
  def fahrenheit(self):
    return self._kelvin * 9/5 - 459.67
  
  @fahrenheit.setter
  def fahrenheit(self, value):
    self._kelvin = (value + 459.67) * 5/9

###################

def main():
  t = Temperature(5.0)
  # t1 = Temperature(-6.0) # this will fail
  # t.set_kelvin(-10.0) # this fails as well
  # t.celsius = -300 # fails
  t.celsius = 1.516785e32 # does not fail because the 'below absolute hot' 
                          # is applied to a proxy of the property and not the property
  pp(vars(Temperature))

if __name__ == "__main__":
  main()