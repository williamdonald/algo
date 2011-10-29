#by shift and induction

def divide(x,y):
  result = (0,0)

  if x ==0 :
    return result
  
  resultsub = divide(x/2,y)
  q = 2 * resultsub[0]
  r = 2 * resultsub[1]
  if x%2 == 1:
    r = r+1
  if r >= y:
    r = r-y
    q = q+1

  return (q,r)  
  
def multiply(x,y):
  if y ==0:
    return 0
  z = multiply(x,y/2)
  if y%2 ==0:
    return 2*z
  else:
    return x +2*z

#bitwise
def powerof2(x):
  return x&(x-1) ==0
  
#bitwise 
def isKbitSet(x,k):
  return (x & 1<<(k-1)) != 0
