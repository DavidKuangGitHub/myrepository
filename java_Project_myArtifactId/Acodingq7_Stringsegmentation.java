import java.util.HashSet;
import java.util.Set;

/*Acodingq7_Stringsegmentation.java
You’re given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the program further. 
Given a dictionary of words: apple  apple pear pie
input string of ‘applepie’ can be segmented into dictionary words. apple pie;
input string apple peer cannot be segmented into dictionary words apple peer
*/
class Acodingq7_Stringsegmentation {

  public static boolean canSegmentString(String s, Set <String> dictionary) {
    for (int i = 1; i <= s.length(); ++i) {
      String first = s.substring(0, i);
      if (dictionary.contains(first)) {
        String second = s.substring(i);

        if (second == null || second.length() == 0 || dictionary.contains(second) || canSegmentString(second, dictionary)) {
          return true;
        }

      }
    }
    return false;
  }

  public static void main(String[] args) {
    Set < String > dictionary = new HashSet < String > ();
    String s = new String();
    s = "applepie";
    //s = "applepeer";
    
    dictionary.add("apple");
    dictionary.add("apple");
    dictionary.add("pear");
    dictionary.add("pie");
    if (canSegmentString(s, dictionary)) {
      System.out.println("String Can be Segmented");
    } else {
      System.out.println("String Can NOT be Segmented");
    }
  }
}
