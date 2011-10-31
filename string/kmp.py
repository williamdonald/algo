def kmppre(p):
  L = len(p)
  b = [0] *(L+1)
  b[0] = -1
  i = 1
  j = -1
  while i< L:
    while j>=0 and p[i] != p[j]:
      j = b[j]

    i = i+1
    j = j+1
    b[i] = j
  return b
                
        
def kmp(p,t):
  b = kmppre(p)
  i = 0
  j = 0
  m = len(p)
  n = len(t)
  while i < n:
    while j>=0 and t[i] != p[j]:
      j = b[j]
    i = i+1
    j = j+1
    if j == m:
      print ("found at: %d" % (i-j))
      j = b[j]
      
