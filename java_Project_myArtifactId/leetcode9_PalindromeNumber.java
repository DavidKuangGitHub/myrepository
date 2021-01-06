/*leetcode9_PalindromeNumber.java
 *Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward and forward.
 *Example1. Input x = 121 Output: true
 *Example2. Input x = -121 Output: false
 *Example3. Input x = 10 Output: false  
 * */
class leetcode9_PalindromeNumber {
	public boolean isPalindrome(int x) {
		if (x >= 0 && x < 10) {
			return true;
		}
		if (x < 0 || x % 10 == 0) {
			return false;
		}
		int rev = 0;
		int copy = x;
		while (copy != 0) {
			int lsb = copy % 10;
			rev = (rev * 10) + lsb;
			copy /= 10;
		}
		if (rev == x) {
			return true;
		} else {
			return false;
		}
	}

	public static void main(String[] args) {
		leetcode9_PalindromeNumber mylc9_PN = new leetcode9_PalindromeNumber();
		int i = 121 /*-121 10*/;
		System.out
				.println("Check Result of PalindromeNumber: " + mylc9_PN.isPalindrome(i) + " when input = " + i + "!");
	}
}