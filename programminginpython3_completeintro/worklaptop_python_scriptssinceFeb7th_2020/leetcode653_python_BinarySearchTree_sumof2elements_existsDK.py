"""leetcode653_python_BinarySearchTree_sumof2elements_existsDK.py
Given the root of a BST (Binary Search Tree) and a target number k. Return true if there exists two elements in the BST
such that their sum is equal to the given target. Otherwise return Fase.
Example1.        5
          3            6
   2         4      (null)        7
Input: root = [5,3,6,2,4,null,7], k=9 Output: true
Example2. Input: root = [5,3,6,2,4,null,7], k=28 Output: false
Example3. Input: root = [2,1,3], k=4 Output: true
Example4. Input: root = [2,1,3], k=1 Output: false
Example5. Input: root = [2,1,3], k=3 Output: true
"""
import TreeNode
#from collections import deque
from collections import Counter
class BST_SumOfTwoElements_Verification(object):
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.res = []
        def helper(root):
            if not root:
                return []
            return [root.val]+helper(root.left)+helper(root.right)
        out = helper(root)
        d1 = Counter(out)
        for i in out:
            ans = [i,k-i]
            if k-i ==i and d1[i] >= sum([x==i for x in ans]):
                print(k-i,d1[i],sum([x==i for x in out] ))
                return True
            elif k-i!=i and k-i in out:
                return True
        return False

instanceOfBST_SOTEV = BST_SumOfTwoElements_Verification()
myRoot = [ 2 , 1 , 3 ]
myK = 4
print("Result Of UnitTest this class = ", instanceOfBST_SOTEV.findTarget(myRoot,myK))