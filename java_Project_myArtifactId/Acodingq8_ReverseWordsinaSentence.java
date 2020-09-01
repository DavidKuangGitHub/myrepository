/*Acodingq8_ReverseWordsinaSentence.java
Reverse the order of words in a given sentence - an array of characters
Example: "Hello World" -> "World Hello"
*/

public class Acodingq8_ReverseWordsinaSentence {
	static String reverseWords(String[] Sentence) {
		String result = "";
		for (int i = Sentence.length - 1; i >= 0; i--)
			result += Sentence[i] + " ";
		return result;
	}

	public static void main(String[] args) {
		// String[] A = {"Hello", "Wolrd"};
		String A[] = "We like this program pretty much".split(" ");
		System.out.println("After reverse,it becomes " + reverseWords(A));
	}
}
