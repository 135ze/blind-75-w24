from typing import Optional

# 226. Invert Binary Tree
# Tree, DFS, BFS, Binary Tree

# Given the root of a binary tree, invert the tree, and return its root.
# -----------------------------------------------

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # invert both branches
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

# -----------------------------------------------
# Testcases

def print_tree(root):
    if root:
        print(str(root.val), end = ", ")
        if root.left or root.right:
            print_tree(root.left)
            print_tree(root.right)

my_sol = Solution()

roots = [TreeNode(
    4,
    TreeNode(2, TreeNode(1), TreeNode(3)), 
    TreeNode(7, TreeNode(6), TreeNode(9))),
    TreeNode(2, TreeNode(1), TreeNode(3))]

for root in roots:
    inverted = my_sol.invertTree(root)
    print("\ninverted tree:")
    print_tree(inverted)