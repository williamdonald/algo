#pseudo code recursive way???
#The sequence of permutations for a given number n can be formed
#from the sequence of permutations for n − 1
#by placing the number n into each possible position in each of the shorter permutations.


def perm(head,tail=''):
  if len(head) ==0:
    print (tail)
  else:
    for i in range(len(head)):
      perm(head[0:i]+head[i+1:],tail+head[i])

 

#TODO 
#permutation Geometric interpretation
#The set of all permutations of n items may be represented geometrically by a permutohedron


#how many ONE(1) exist in binary x
def countBits(x):
  c = 0
  for j in range(32):
    if (x & (1<<j)):
      print ("location %d is 1" % j)
      c = c+1

  return c    
