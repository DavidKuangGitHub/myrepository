
/*Amazonalgorithminterviewq2.java
Determine if the sum of two integers is equal to the given value. Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 
Return true if the sum is exists and return false if it does not. Example
{5, 7, 1, 2, 8, 4, 3}
True for 10 as 7+3 2+8
False for 19
*/
import java.util.Arrays;

public class Amazonalgorithminterviewq2 {
	static boolean hasArrayTwoCandidates(int A[], int sum) {
		int l, r, arr_size = A.length;
		Arrays.sort(A);
		l = 0;
		r = arr_size - 1;
		while (l < r) {
			if (A[l] + A[r] == sum)
				return true;
			else if (A[l] + A[r] < sum)
				l++;
			else
				r--;
		}
		return false;
	}

	public static void main(String[] args) {
		// int A[] = {1,4, 45, 6, 10, -8};
		int A[] = { 5, 7, 1, 2, 8, 4, 3 };
		int sumtest = /* 16 */ 10 /* 19 */;
		System.out.println("Result of " + sumtest + " would be " + hasArrayTwoCandidates(A, sumtest) + "!");
	}
}
