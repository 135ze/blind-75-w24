from typing import Optional
# 206. Reverse Linked List
# Linked List, Recursion

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -----------------------------------------------
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # place values into stack
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        # pop off each value into a new list
        newList = ListNode() # first node is empty
        curHead = newList
        while stack:
            curHead.next = ListNode(stack.pop())
            curHead = curHead.next
        
        return newList.next # ignore empty first node

# -----------------------------------------------
# Testing
my_sol = Solution()

lists = [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(1, ListNode(2))]

for list in lists:
    result = my_sol.reverseList(list)
    while list:
        print(list.val)
        list = list.next