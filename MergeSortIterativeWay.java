import java.util.LinkedList;

/**
 * Observed from recursive mergesort algorithm, actually the merge sort happens in this way.
 * <pre>
 * Q = [] EMPTY QUEUE
 * for i = 1 to n:
 * 		inject(Q,a[i])
 * while |Q|>1:
 * 		inject(Q,merge(eject(Q),eject(Q)))
 * return eject(Q)
 * </pre>
 *
 */
public class MergeSortIterativeWay {
	
	static int[] sort(int[] tobe){
		LinkedList<LinkedList<Integer>> q = new LinkedList<LinkedList<Integer>>();
		for (int i = 0; i < tobe.length; i++) {
			LinkedList<Integer> ll = new LinkedList<Integer>();
			ll.add(tobe[i]);
			q.add(ll);
		}
		
		while(q.size()>1){
			LinkedList<Integer> first = q.pop();
			LinkedList<Integer> second = q.pop();
			q.add(merge(first,second));
			
		}
		
		LinkedList<Integer> only = q.getFirst();
		int[] result = new int[only.size()];
		int i = 0;
		for (Integer integer : only) {
			result[i++] = integer.intValue();
		}
		return result;
		
	}
	
	static LinkedList<Integer> merge(LinkedList<Integer> first,LinkedList<Integer> second){
		LinkedList<Integer> result = new LinkedList<Integer>();
		while(true){
			if(first.isEmpty()||second.isEmpty()){
				break;
			}
			Integer f1 = first.peek();
			Integer s1 = second.peek();
			if(f1>=s1){
				result.add(second.pop());
			}else {
				result.add(first.pop());
			}
		}
		if(!first.isEmpty()){
			result.addAll(first);
		}
		if(!second.isEmpty()){
			result.addAll(second);
		}
		
		return result;
	} 

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] a = {3,2,5,9,7,8,1,6,4};
		int[] r = sort(a);
		for (int i : r) {
			System.out.print(""+i+",");
			
		}
	}

}
