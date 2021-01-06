"""leetcode657_python_robotreturnorigin.py
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
"""
class RobotReturnOrigin(object):
    def doesItReturnOrigin(self, moves: str) -> bool:
        travel = [0,0]
        for theString in moves:
            if theString == "U":
                travel[1] += 1
            if theString == "D":
                travel[1] += -1
            if theString == "L":
                travel[0] += -1
            if theString == "R":
                travel[0] += 1
        return [0,0] == travel

instanceOfRobotReturnOrigin = RobotReturnOrigin()
#moves = "UD"
#moves = "LL"
moves = "RLUUDDLLRRURDL"
print("Result of this class unit test = ", instanceOfRobotReturnOrigin.doesItReturnOrigin(moves))



