/*Acodingq11_FindAllSubsetsofagivensetofintegers.java
We are given a set of integers and we have to find all the possible subsets of this set of integers. The following example elaborates on this further.
Given set of integers: 2 3 4
All possible subsets for this given set of integers:
()(2)(3)(2,3)(4)(2,4)(3,4)(2,3,4)*/

public class Acodingq11_FindAllSubsetsofagivensetofintegers {
	static void printSubsets(int set[]) {
		int n = set.length;
		for (int i = 0; i < (1 << n); i++) {
			System.out.print("{ ");
			int m = 1;
			for (int j = 0; j < n; j++) {
				if ((i & m) > 0) {
					System.out.print(set[j] + " ");
				}
				m = m << 1;
			}
			System.out.println("}");
		}
	}

	public static void main(String[] args) {
		// int set[] = {1 ,2, 3};
		int set[] = { 2, 3, 4 };
		printSubsets(set);
	}
}
