"""leetcode_pythonq_155_MinStack.py"""
""" Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
-push(x): Push element x onto stack
-pop(): Removes the element on top of the stack
-top(): Get the top element
-getMin(): Retrieve the minimum element in the stack
Example: 
MinStack myMinStack = new MinStack()
"""
class MinStack:
  def __init__(self):
    self.stack = list()
    self.minstack = list()
    
  def push(self, x: int) -> None:
    self.stack.append(x)
    if len(self.minstack) == 0 or x <= self.minstack[-1]:
      self.minstack.append(x)
      
  def pop(self) -> None:
    e = self.stack.pop()
    if e == self.minstack[-1]:
      self.minstack.pop()
 
  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minstack[-1]
"""
myMinstack = MinStack()
myMinstack.push(-2)
myMinstack.push(0)
myMinstack.push(-3)
print("ResultOfMinimum = ", myMinstack.getMin())
myMinstack.pop()
print("ResultOf_myMinstack.top() = ", myMinstack.top())
print("After all actions above done, the new ResultOfMinimum2 = ", myMinstack.getMin())"""
