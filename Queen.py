#eight queen problem solution
#use recursion and backtracking

#why backtracking?

#we can decompose one instance of our problem into serveral possible subproblems
#That is, each time we make a recursive call, we will have to make a choice as 
#to which decomposition to use.  If we choose the wrong one, we will eventually run into a 
#dead end and find ourselves in a state from which we are unable to solve the problem 
#immediately and unable to decompose the problem any further; when this happens, we 
#will have to backtrack to a "choice point" and try another alternative.  

#usage: xQueen([-1,-1,-1,-1,-1,-1,-1,-1],0)

#init board as [-1,-1,-1,-1,-1,-1,-1,-1]
# -1 means we haven't place any queen in the column
#board [7, 3, 0, 2, 5, 1, 6, 4]
#means for the first column, we put the queen at row 7, which is the first queen
#means for the second column, we put the queen at row 3, which is the second queen
#means for the third column, we put the queen at row 0, which is the third queen
#etc.
def isSafe(board,rowToTry,colToTry):
  for col, row in enumerate(board):
    if row!=-1:
      if rowToTry ==row or colToTry-rowToTry==col-row or colToTry+rowToTry ==col+row:
        return False
  return True


def placeQueen(board,rowToTry,colToTry):
  #print ("place Queen {0} at row {1}".format(colToTry, rowToTry))
  board[colToTry] =  rowToTry

def removeQueen(board,rowToTry,colToTry):
  #print ("remove Queen {0} at row {1}".format(colToTry, rowToTry))
  board[colToTry] = -1

def xQueen(board,colToTry):
  if colToTry>=len(board):
    #found a case, but if we have iterated all rows, we are done.
    #temporarily, return false
    print (board)
    return False
  #for every iteration, we must try all rows, ineffcient?
  for rowToTry in range(len(board)):
    if isSafe(board,rowToTry,colToTry):
      placeQueen(board,rowToTry,colToTry)
      #if subprobem done, we are done.
      #otherwise, we need to clean our ass, and try next row
      if xQueen(board,colToTry+1):
        return True
      removeQueen(board,rowToTry,colToTry)

  #If and Only if all rows failed, return false to trigger backtracking
  return False

  
      
