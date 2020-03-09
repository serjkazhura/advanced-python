class TracingMeta(type): # our metaclss has to be a subclass of type (or any other existing metaclass)

  # create a dictionary aka a namespace ake mapping object associated with the class
  # override it if you  want to:
  # customize the type of initial value of the namespace mapping
  @classmethod
  def __prepare__(mcs, name, bases, **kwargs):
    print("TracingMeta.__prepare__(name, base, **kwargs)")
    print(" mcs=", mcs)
    print(" name=", name)
    print(" bases=", bases)
    print(" kwargs=", kwargs)
    namespace = super().__prepare__(name, bases) # call parent to do the actual work
    print("<--- namespace =", namespace)
    print()
    return namespace
  
  # create the new class object
  # override it if:
  # you want to allocate and optionally configure new class object
  def __new__(mcs, name, bases, namespace, **kwargs):
    print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
    print(" mcs=", mcs)
    print(" name=", name)
    print(" bases=", bases)
    print(" namespace=", namespace)
    print(" kwargs=", kwargs)
    cls = super().__new__(mcs, name, bases, namespace) # call parent to do the actual work
    print("<-- cls=", cls)
    print()
    return cls

  # configure newly created class object
  # override it if:
  # you want to configure existing class object
  def __init__(cls, name, bases, namespace, **kwargs):
    print("TracingMeta.__init__(mcs, name, bases, namespace, **kwargs)")
    print(" cls=", cls)
    print(" name=", name)
    print(" bases=", bases)
    print(" namespace=", namespace)
    print(" kwargs=", kwargs)
    super().__init__(name, bases, namespace) # call parent to do the actual work
    print()

  def metamethod(cls):
    print("TracingMeta.metamethod(cls)")
    print(" cls = ", cls)

  def __call__(cls, *args, **kwargs):
    print("TracingMeta.__call__(cls, *args, **kwargs)")
    print(" cls=", cls)
    print(" args=", args)
    print(" kwargs=", kwargs)
    print(" About to call type.__call__()")
    obj = super().__call__(*args, **kwargs)
    print(" Returned from type.__call__()")
    print(" <--- obj=", obj)
    print()
    return obj

#####################################

class EntriesMeta(type):

  def __new__(mcs, name, bases, namespace, num_entries, **kwargs):
    print("Entries.__new__(mcs, name, bases, namespace, **kwargs)")
    print(" kwargs=", kwargs)
    print(" num_entries=", num_entries)
    namespace.update({chr(i): i for i in range(ord('a'), ord('a')+num_entries)})
    cls = super().__new__(mcs, name, bases, namespace)
    return cls

  # note that u need __new__ and __init__ to have the same signature
  def __init__(cls, name, bases, namespace, num_entries, **kwargs):
    super().__init__(name, bases, namespace)


####################################

class Widget(metaclass=TracingMeta):
  def action(self, message):
    print(message)
  the_answer=42

####################################

class Reticulator(metaclass=TracingMeta, tension=496): # tension is kwarg, use to configure the class object. 
                                                       # like a class factory
  def reticulate(self, spline):
    print(spline)
  cubic = True

####################################

class AtoZ(metaclass=EntriesMeta, num_entries=26):
  pass

####################################

def main():
  # this is in fact:
  # w = TracingMeta.__call__(Widget, *args, **kwargs)
  w = Widget()
  print("MAIN")
  print(type(w))
  print(type(Widget))
  Widget.metamethod()
  # w.metamethod() # this will fail
  a = AtoZ()
  print(a)

if __name__ == "__main__":
  main()