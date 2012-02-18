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
#multiply2(x,y)
def multiply2(x,Y):
    if(y==0): return 0
    r = 0 
    while(x !=0):
        if(x%2 !=0 ): r +=y
        x = x/2
        y = 2y
    return r

#bitwise
def powerof2(x):
  return x&(x-1) ==0
  
#bitwise 
def isKbitSet(x,k):
  return (x & 1<<(k-1)) != 0

#lowest bit set off
#for any integer x, it diffs with x-1 on lowest bit 
def lowestoff(x):
  return x & (x-1)

#extract,based on
#1 ^ 0 = 1
#0 ^ 0 = 0
def extractLowestBit(x):
  return x ^ (x &(x-1))

#toggle, based on
#0 ^ 1 = 1 (0->1)
#1 ^ 1 = 0 (1->0)
def toggleKbitInX(x,k):
  return x ^ 1<<(k-1)

#force, based on
#0 | 1 = 1
#1 | 1 = 1
def forceKbitSet(x,k):
  return x | 1<<(k-1)

#for 32 bit integer
#1000 0000 0000 0000 0000 0000 0000 0000
#1100 0000 0000 0000 0000 0000 0000 0000
#1111 0000 0000 0000 0000 0000 0000 0000
#1111 1111 0000 0000 0000 0000 0000 0000
#1111 1111 1111 1111 0000 0000 0000 0000
#1111 1111 1111 1111 1111 1111 1111 1111
def setMostSignificantBitOnly(x):
  y = x
  y = y | (y>>1)
  y = y | (y>>2)
  y = y | (y>>4)
  y = y | (y>>8)
  y = y | (y>>16)
  y = (y+1)>>1
  return y

################################
#The captain of the ship TITANIC is a little .... off the track.
#He needs to select the crew for the ship.
#But everyone seems to be eligible.
#So to test their intelligence, he plays a game. 
#The contestants have to stand in a line.
#They are given the numbers in the order in which they stand, starting from 1.
#The captain then removes all the contestants that are standing at an odd position. 
#Initially, standing people have numbers  1,2,3,4,5...
#After first pass, people left are  2,4,...
#After second pass  4,....
#And so on.
#You want to board the ship as a crew member.
#Given the total number of applicants for a position, find the best place to stand in the line so that you are selected.
################################


#   4321 round
#   |||| flag=1 killed in this round
#   ||||
# 8 1000
# 7 0111
# 6 0110
# 5 0101
# 4 0100
# 3 0011
# 2 0010
# 1 0001


# or based on math induction: return 2 ** math.floor(math.log(x,2))
def jTitanic(x):
  return setMostSignificantBitOnly(x)







