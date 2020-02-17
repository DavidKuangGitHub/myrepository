''' leetcode_test_ValidParentheses.py
'''
class SolutionFeb172020:
  def isValid(self,s:str) -> bool:
    st = []
    for i in s:
      if i in validOpen:
        st.append(i)
      else: 
        c = st.pop() if len(st) > 0 else "-"
        if i != validOpen[c]:
          return False
    return len(st) == 0
