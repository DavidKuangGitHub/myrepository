import java.util.Arrays;

/*leetcode657_java_RobotReturnOrigin.java
 There is a robot starting at position (0,0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0,0) after it completes its moves.
The move sequence is represented by a string, and the character moves[i] represents its ith move.
Valid moves are R(Right), L(Left), U(Up), and D(Down).
If the robot returns to the origin after it finishes all of its moves, return True. Otherwise, return False.
Note: The way that the robot is 'facing' is irrelevant. 'R' will always make the robot move to the absolute right once. 'L' the absolute left once, etc.
Also, assume that the magnitude of the robot's movement is the same for each move.
Example1: Input: moves = "UD" output: true
Example2: Input: moves = "LL" output: false
Example3: Input: moves = "RL" output: true
  */
class leetcode657_java_RobotReturnOrigin {
	public boolean judgeCircle(String s) {
		int[] originalMoves = {0,0};
		int[] moves = {0,0};
		for (int i=0; i <= s.length()-1; i++ ) {
			char c = s.charAt(i);
			if ((Character.compare(c, 'L') == 0) || (Character.compare(c, 'l') == 0)) 
				moves[0] -= 1;
			if ((Character.compare(c, 'R') == 0) || (Character.compare(c, 'r') == 0)) 
				moves[0] += 1;
			if ((Character.compare(c, 'U') == 0) || (Character.compare(c, 'u') == 0)) 
				moves[1] += 1;
			if ((Character.compare(c, 'D') == 0)|| (Character.compare(c, 'd') == 0))  
				moves[1] -= 1; 
		}
		return Arrays.equals(originalMoves, moves);
	}
	
	public static void main(String[] args) {
		leetcode657_java_RobotReturnOrigin mylc657_RRO = new leetcode657_java_RobotReturnOrigin();
		String myString = "rLuUDdLlRRURDL" /*"RL" "LL" "UD"*/;
		System.out.println("ResultUnitTestofClass = "+ mylc657_RRO.judgeCircle(myString)+" !");
		
	}

}
