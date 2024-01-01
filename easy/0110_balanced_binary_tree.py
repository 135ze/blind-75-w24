from typing import Optional

# 110. Balanced Binary Tree
# Tree, DFS, Binary Tree

# Given a binary tree, determine if it is height balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------
# taken from solutions :\ TODO: retry on my own

class Solution:
     def isBalanced(self, root):
            
        def findDepth(root):
            if not root:
                return 0
            left  = findDepth(root.left)
            right = findDepth(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return findDepth(root) != -1