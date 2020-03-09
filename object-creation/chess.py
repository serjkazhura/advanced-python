class ChessCoordinate:
  # cls - class
  def __new__(cls, *args, **kwargs):
    print("args=", repr(args))
    print("kwargs=", repr(kwargs))
    obj = super().__new__(cls)
    print("id(obj) = ", id(obj))
    return obj

  def __init__(self, file, rank):
    print("id(self) = ", id(self))
    if len(file) != 1:
      raise ValueError("file")
    if file not in 'abcdefgh':
      raise ValueError("file")
    if rank not in range(1,9):
      raise ValueError("rank")
    self._file = file
    self._rank = rank

  @property
  def file(self):
    return self._file
  
  @property 
  def rank(self):
    return self._rank

  def __repr__(self):
    return "{}(file={}, rank={})".format(self.__class__.__name__, self.file, self.rank)

  def __str__(self):
    return "{}{}".format(self.file, self.rank)


class ChessCoordinateMemOptimized:

  # interning is a powerful mechanism for memory allocation optimization
  # but it should only be used for IMMUTABLE objects!
  _interned = {}

  # cls - class
  def __new__(cls, file, rank):

    if len(file) != 1:
      raise ValueError("file")

    if file not in 'abcdefgh':
      raise ValueError("file")

    if rank not in range(1,9):
      raise ValueError("rank")

    key = (file, rank)

    if key not in cls._interned:
      obj = super().__new__(cls)
      obj._file = file
      obj._rank = rank
      cls._interned[key] = obj

    return cls._interned[key]

  @property
  def file(self):
    return self._file
  
  @property 
  def rank(self):
    return self._rank

  def __repr__(self):
    return "{}(file={}, rank={})".format(self.__class__.__name__, self.file, self.rank)

  def __str__(self):
    return "{}{}".format(self.file, self.rank)


########################

def main():
  white_queen = ChessCoordinate('d', 4)
  print(white_queen)

if __name__ == '__main__':
  main()