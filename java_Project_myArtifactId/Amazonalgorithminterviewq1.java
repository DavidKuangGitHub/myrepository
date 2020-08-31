/* find x that is the missing element of an array of positive numbers from 1 to n.
 * 3, 7, 1, 2, 8, 4, 5
 * n = 8, the missing number =6. should sort first.
 * */
public class Amazonalgorithminterviewq1 {
	static int getMissingNo(int a[], int n) {
		int i, total;
		total = (n + 1) * (n + 2) / 2;
		for (i = 0; i < n; i++)
			total -= a[i];
		return total;
	}

	public static void main(String[] args) {
		int dimension;
		/*
		 * int a[] = {1,2,4,5, 6}; dimension = 5;
		 */
		int a[] = { 3, 7, 1, 2, 8, 4, 5 };
		dimension = 7;
		int miss = getMissingNo(a, dimension);
		System.out.println("The missing number is " + miss + "!");
	}
}
