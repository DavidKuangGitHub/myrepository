/*Acodingq12_Printbalancedbracecombinations.java
Print all braces combinations for a given value n, so that they are balanced.
For this solution, we may/will be using recursion
n=1 {}
n=2 {}{}, {{}}
n=3
*/
class Acodingq12_Printbalancedbracecombinations {
	static void _printParenthesis(char str[], int pos, int n, int open, int close) {
		if (close == n) {
			for (int i = 0; i < str.length; i++)
				System.out.print(str[i]);
			System.out.println();
			return;
		} else {
			if (open > close) {
				str[pos] = '}';
				_printParenthesis(str, pos + 1, n, open, close + 1);
			}
			if (open < n) {
				str[pos] = '{';
				_printParenthesis(str, pos + 1, n, open + 1, close);
			}
		}
	}

	static void printParenthesis(char str[], int n) {
		if (n > 0)
			_printParenthesis(str, 0, n, 0, 0);
		return;
	}

	public static void main(String[] args) {
		int n = 3;
		char[] str = new char[2 * n];
		printParenthesis(str, n);
	}
}
