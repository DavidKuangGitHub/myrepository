package eclipseJEE2020_6dk1;

/*Acodingq9_wayswithcoinsandatotalamount.java
How many ways can you make changes with coins and a total amount
Suppose we have coin denominations of [1,2,5] and the total amount is 7. Then we can make changes in the following 6 ways:
1 1 1 1 1 1 1
1 1 1 1 1 2
1 1 1 2 2
1 2 2 2
1 1 5
2 5
*/
class Acodingq9_wayswithcoinsandatotalamount {

	static int findWays(int[] coins, int sum) {
		int size = coins.length;
		int[][] arr = new int[size + 1][sum + 1];
		for (int i = 0; i < size + 1; i++)
			arr[i][0] = 1;
		for (int i = 1; i < size + 1; i++)
			for (int j = 0; j < sum + 1; j++)
				if (coins[i - 1] > j)
					arr[i][j] = arr[i - 1][j];
				else
					arr[i][j] = arr[i][j - coins[i - 1]] + arr[i - 1][j];
		return arr[size][sum];
	}

	public static void main(String args[]) {
		int coins[] = { 1, 2, 5 };
		int sum = 7;
		System.out.println(
				"Changes to total amount of " + sum + " could be made with " + findWays(coins, sum) + " ways.");
	}
}