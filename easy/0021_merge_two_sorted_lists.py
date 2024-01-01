from typing import Optional

# 21. Merge Two Sorted Lists
# Linked List, Recursion

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# -----------------------------------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], \
                    list2: Optional[ListNode]) -> Optional[ListNode]:
    # temp fake list to acc on
    fakeList = ListNode()
    myList = self.accLists(list1, list2, fakeList)
    return myList
  
  def accLists(self, head1: Optional[ListNode], head2: Optional[ListNode], \
               newList: Optional[ListNode]) -> Optional[ListNode]:
      if not head1: # head1 done
          return head2
      elif not head2: # head2 done
          return head1
      elif head1.val < head2.val: # take from head1
          newList = ListNode(head1.val, self.accLists(head1.next, head2, newList))
      else: # take from head2
          newList = ListNode(head2.val, self.accLists(head1, head2.next, newList))
      return newList

# -----------------------------------------------
# Testcases

my_sol = Solution()

list1s = [
    ListNode(1, ListNode(2, ListNode(4))),
    None,
    None
]
list2s = [
    ListNode(1, ListNode(3, ListNode(4))),
    None,
    ListNode(0, ListNode(5))
]

for i in range(3):
    merged_list = my_sol.mergeTwoLists(list1s[i], list2s[i])

    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print("None")
