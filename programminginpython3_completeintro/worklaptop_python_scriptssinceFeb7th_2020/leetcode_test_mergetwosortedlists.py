'''leetcode_test_mergetwosortedlists.py
Merge two sorted linked lists and return it as a new list.
Note: The new list should be made by splicing together the nodes of the first two lists.
Example: Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
#Definition for singly-linked list.
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class SolutionFeb132020:
  def mergeTwoLists(self, l1,l2):
    big_list = []
    head = l1

    while head:
      big_list.append(head.val)
      head = l1
    curr = 12
    while curr:
      big_list.append(curr.val)
      curr = curr.next

    big_list.sort()
    try:
      l3 = ListNode(big_list[0])
      head = l3
      counter =2

      head.next = ListNode(big_list[1])
      head = head.next
      while counter <= len(big_list) -1:
        head.next = ListNode(big_list[counter])
        head = head.next
        counter += 1
      return l3
    except Exception as e:
      if len(big_list) == 1:
        return ListNode(big_list[0])
      return ListNode('')
