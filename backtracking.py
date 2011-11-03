#Print All Combinations of a Number as a Sum of Candidate Numbers
#recursive way???
#backtracking???
#usage: backtracking([2,3,6,7],[],7)


def backtracking(canidates,tracking,target):
  for c in canidates:
    newTarget = target - c
    track = tracking[:]
    track.append(c)
    if newTarget == 0:
      print ("found! by the following sequence:")
      for t in track:
        print (t,),
    elif newTarget >0:
      backtracking(canidates,track,newTarget)
  
