#convert an integer to binary
#without using stack to track previous info
#put sub recursion before print
#to implement print less significant bits later
def convert(n):
  if n == 0:
    return
  convert(n/2);
  print (n%2);
  #tail recursion is not what we want
  #print (n%2)
  #convert(n/2)
