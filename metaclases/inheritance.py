class MetaA(type):
  pass

class MetaB(type):
  pass

class MetaC(MetaA, MetaB):
  pass

class A(metaclass=MetaA):
  pass

class B(metaclass=MetaB):
  pass

# in order to inherit from A and B we have to create a MetaC class that will be used as a metaclass, because python
# does not know if to choose metaA or metaB
class C(A, B, metaclass=MetaC):
  pass

# btw super() delegates to the next class in the method resolution order (e.g. MRO)