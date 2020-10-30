/*leetcode242_ValidAnagram.java
Given two strings s and t, write a function to determine if t is an anagram of s. You may assume the string contains only lowercase alphabets.
Here anagram is different words however being consisted by same letters in total. Example1: 
Input: s = "anagram", t = "nagaram"
Output: true
Example2:
Input: s = "rat", t = "car"
Output: false
*/
class leetcode242_ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        int[] c = new int[129];
        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();
        int len = s.length();
        for(int i = 0; i < len ; i++){
            c[sChar[i]]++; 
            c[tChar[i]]--;
        }
        for(int i = 0; i < 129 ; i++)
            if(c[i]!= 0)
                return false;
        return true;
    }
    
    public static void main(String[] args) {
    	leetcode242_ValidAnagram myLeetcode242_ValidAnagrm = new leetcode242_ValidAnagram();
    	/*String s = "anagram";
    	String t = "nagaram";
    	String s = "rat";
    	String t = "car";*/
    	String s = "smoke";
    	String t = "kemos";
    	System.out.print("Result: "+ myLeetcode242_ValidAnagrm.isAnagram(s, t) );
    }
}
