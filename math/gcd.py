#
#Euclid's algorithm. 
#If p > q, the gcd of p and q is the same as the gcd of q and p % q.
#
#
def gcd(m,n):
  """
  precondition: m>n
  """
  if n == 0:
    return m
  return gcd(n,m%n)
