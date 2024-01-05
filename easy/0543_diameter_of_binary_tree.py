from typing import Optional
# 543. Diameter of Binary Tree
# Trees, DFS, Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # finds max depth from left and right of given node
        def findMaxDepth(node: Optional[TreeNode]) -> int:
            # empty node
            if not node:
                return 0
            
            # find max of left and right paths
            left_distance = findMaxDepth(node.left)
            right_distance = findMaxDepth(node.right)

            # compare with current max
            if left_distance + right_distance > self.cur_max_diameter:
                self.cur_max_diameter = left_distance + right_distance

            # increment depth by one layer
            return (1 + max(left_distance, right_distance))
        
        self.cur_max_diameter = 0
        findMaxDepth(root)
        return self.cur_max_diameter
        
# -----------------------------------------------
# Testing
my_sol = Solution()

roots = [TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), TreeNode(1, TreeNode(2))]

for i in range(2):
    print(my_sol.diameterOfBinaryTree(roots[i]))