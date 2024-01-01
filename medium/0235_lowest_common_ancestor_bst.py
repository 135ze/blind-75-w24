# 235. Lowest Common Ancestor of a Binary Search Tree
# Tree, DFS, BST, Binary Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and 
# q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# -----------------------------------------------

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curVal = root.val
        # both on same side of tree
        if curVal < p.val and curVal < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif curVal > p.val and curVal > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # one on each side of tree or on current node
        else:
            return curVal

# -----------------------------------------------
# Testcases
my_sol = Solution()

roots = [TreeNode(6, 
                TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                TreeNode(8, TreeNode(7), TreeNode(9))),
                TreeNode(6, 
                TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                TreeNode(8, TreeNode(7), TreeNode(9))),
                TreeNode(2, TreeNode(1))]

p = [TreeNode(2), TreeNode(2), TreeNode(2)]
q = [TreeNode(8), TreeNode(4), TreeNode(1)]

for i in range(3):
    print(my_sol.lowestCommonAncestor(roots[i], p[i], q[i]))