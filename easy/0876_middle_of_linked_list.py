from typing import Optional

# 876. Middle of the Linked List
# Linked List, Two Pointers

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -----------------------------------------------
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        middle = head
        while head:
            size += 1
            head = head.next
            if size % 2 == 0: # middle node will move half as fast
                middle = middle.next
        
        return middle
        
        # better sol: slow and fast pointers
        # after each, slow = slow.next and fast = fast.next.next, then return slow
# -----------------------------------------------
# Testing
my_sol = Solution()

heads = [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))]

for i in range(2):
    print(my_sol.middleNode(heads[i]))