import java.util.ArrayList;
import java.util.List;

/*Acodingq10_FindKthpermutation.java
Given a set of n elements, find their Kth permutation. Consider the following set of elements:
1 2 3
All permutations of the above elements are (with ordering):
1st 123
2nd 132
3rd 213
4th 231
5th 312
6th 321
*/
class Acodingq10_FindKthpermutation {
	static int factorial(int n) {
		if (n == 0 || n == 1)
			return 1;
		return n * factorial(n - 1);
	}

	static void find_kth_permutation(List<Character> v, int k, StringBuilder result) {
		if (v.isEmpty()) {
			return;
		}
		int n = v.size();
		int count = factorial(n - 1);
		int selected = (k - 1) / count;
		result.append(v.get(selected));
		v.remove(selected);
		k = k - (count * selected);
		find_kth_permutation(v, k, result);
	}

	static String get_permutation(int n, int k) {
		List<Character> v = new ArrayList<Character>();
		char c = '1';
		for (int i = 1; i <= n; ++i) {
			v.add(c);
			c++;
		}
		StringBuilder result = new StringBuilder();
		find_kth_permutation(v, k, result);
		return result.toString();
	}

	public static void main(String[] args) {
		int range = 3;
		System.out.println("While " + range + " elemetns in total: ");
		for (int i = 1; i <= factorial(range); ++i) {
			System.out.println(i + "th permutation = \t" + get_permutation(range, i));
		}
	}
}
