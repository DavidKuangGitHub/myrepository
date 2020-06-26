"""leetcode_pythonq_38_CountandSay.py
Given an integer n where 1<= n <= 30, generate the nth term of the count-and-say sequence.Like: 1=>1[one 1]; 2=>11[two 1s]; 3=>21; 4=>1211; 5=>111221 
Example1:Input: 1
Output: 1
Explanation: This is the base case
Example2:Input: 4
Output: 1211
Explanation: This is the base case"""
class SolutionJun26_2020:
    def countAndSay(self, n: int) -> str:
        l = ['1']
        mark = 0
        for x in range(0,n):
            s = ''
            mark = 0
            for i in range(len(l[x])):
                if i != (len(l[x]) - 1) and l[x][i] == l[x][i+1]:
                    continue
                else:
                    med = l[x][mark:i+1]
                    s += (str(med.count(med[0])) + med[0] )
                    mark = i+1
            l.append(s)
        return l[n-1]
        
"""mySolutionJun26_2020 = SolutionJun26_2020()
n=5
print("ResultOfmySolutionJun26_2020 =", mySolutionJun26_2020.countAndSay(n))"""
