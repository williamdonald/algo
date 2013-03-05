def partition(seq):
        pi,seq=seq[0],seq[1:]
        lo=[x for x in seq if x <=pi]
        hi=[x for x in seq if x > pi]
        return lo,pi,hi
def quicksort(seq):
        if len(seq)<=1: return seq
        lo,pi,hi = partition(seq)
        return quicksort(lo)+[pi]+quicksort(hi)

        

def mergesort(seq):
  mid = len(seq)//2
	lft,rgt = seq[:mid],seq[mid:]
	if len(lft)>1: lft = mergesort(lft)
	if len(rgt)>1: rgt = mergesort(rgt)
	res=[]
	while lft and rgt:
		if lft[-1] >= rgt[-1]:
			res.append(lft.pop())
		else :
			res.append(rgt.pop())
	res.reverse()

	return (lft or rgt) +res
