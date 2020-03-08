def main():
  bytes = 0b11110000
  print(bytes)
  bytes2 = bin(240) # cast to binary via bin command
  print(bytes2)
  xor = bin(0b11110000 ^ 0b00110011)
  print(xor)
  compliment = bin(~0b11110000)
  print(compliment)
  compliment = bin(twos_compliment(~0b11110000, 8))
  print(compliment)

def twos_compliment(x, num_bits):
  if x < 0:
    return x + (1 << num_bits)
  return x

if __name__ == '__main__':
  main()