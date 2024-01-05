from typing import Optional

# 104. Maximum Depth of Binary Tree
# Tree, DFS, BFS, Binary Tree

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # empty node
        if not root:
            return 0
        
        # increment max of left and right paths
        left_distance = self.maxDepth(root.left)
        right_distance = self.maxDepth(root.right)
        return 1 + max(left_distance, right_distance)
        
# -----------------------------------------------
# Testing
my_sol = Solution()

roots = [TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), TreeNode(1, None, TreeNode(2))]

for i in range(2):
    print(my_sol.maxDepth(roots[i]))