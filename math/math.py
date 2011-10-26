def divide(x,y):
  #
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
  
