def longestPalindrome(s):
  p = [1]
  n = len(s)
  mx = 0
  mid = 0
  i = 1
  while i< n:
    if mx > i:
      p.append(min(p[2*mid-i],mx-i));
    else:
      p.append(1)

    while (i-p[i]>=0) and (i+p[i]<n) and (s[i+p[i]] == s[i-p[i]]) :
      p[i] = p[i]+1

    if p[i]+i > mx:
      mx = p[i] + i
      mid = i

    i = i+1
  return (max(int(x) for x in p)-1)

  
      
  
  
