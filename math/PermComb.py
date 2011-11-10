#permutation recursion way
###############property#######################################
#                                                            #
#                  | ai,P(a1,...,ai-1,ai+1,...aN) if N > 1   #
#P(a1,a2,...aN) =  |                                         #
#                  | aN                           if N = 1   # 
#                                                            #
###############property#######################################

def swap(a,x,y):
  t = a[x]
  a[x] = a[y]
  a[y] = t

#usage:perm([1,2,3],3)
def permimpl(a,n):
  if n==1:
    print (a)
    return
  #a special case is to swap n-1 with n-1!!!
  for i in range(n):
    #we use first element as pivot
    swap(a,i,0)
    permimpl(a,n-1)
    swap(a,0,i)
    #or you can use end as pivot
    #swap(a,i,n-1)
    #permimpl(a,n-1)
    #swap(a,n-1,i)

def perm(a):
  """
  usage: perm([1,2,3,4])
  """
  permimpl(a,len(a))
 

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

  
# recursive permutation solution is inefficient,
# another view of generating all permutations is
# like a journey from 123456789 to 987654321
# every neighour nodes throught the path just diff one bit,
# our algorithm is
# to find the next permutation according lexicographic order directly
# for example, if you can guess next permutation of 912758643 is
# 912763458, then you can understand the following algorithm

###
#base state: 3 is smaller than 4, 
#but our next phase should be a little bigger, so swap 3,4
#1234-->1243 

# usage:
# nextPerm([1,4,3,2])


def nextPerm(x):
  j = len(x) -2
  #find '5', since 8643 is the max 
  while x[j] > x[j+1]:
    j = j-1
  if j<0:
    print ('no next exist')
    return
  k = len(x) -1
  #locate '6', it is just bigger than 5
  while x[j]> x[k]:
    k = k-1
  #swap '5' and '6'
  t = x[j]
  x[j] = x[k]
  x[k] = t

  r = len(x)-1
  s = j+1
  #convert '8543' to '3458'
  while r>s:
    m = x[r]
    x[r] = x[s]
    x[s] = m
    r = r-1
    s = s+1

  print (x)    

#12345 choose 3 combintation
#123
#124
#125#
#134
#135#
#145#
#234
#235#
#245#
#345#

#usage:
#nextComb([1,2,3,6],6,4)
#nextComb([1,4,5],5,3)  
def nextComb(a,n,r):
  i = r-1
  #a[0]=3? a[1]=4? a[2] =5?
  while a[i] > n -r +i:
    i = i-1
    if i<0:
      print ('no next')
      return
  a[i] = a[i] +1
  j = i+1
  while j<=(r-1):
    a[j] = a[i]+(j-i)
    j=j+1
  print (a)
    

  
