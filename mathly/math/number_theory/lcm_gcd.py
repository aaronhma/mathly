def gcd(a: int, b: int) -> int:
  """
  Returns the Greatest Common Divisor of a and b using
  Euclid's Algorithm.
  """

  if b == 0:
    return a
    
  return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
  """
  Returns the LCM of a and b.
  """
  return (a * b) / gcd(a, b)
  
