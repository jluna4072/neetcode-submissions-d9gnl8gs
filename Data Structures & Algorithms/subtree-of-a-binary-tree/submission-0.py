# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
iSubtree -> main dfs, iterate through the root. At each node, we check if starting from that root,
its the same tree starting from subroot

isSameTree -> main check to see if both roots are the same tree
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        same = self.isSameTree(root, subRoot)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return same or left or right

    def isSameTree(self, p, q):
        if (not q and p) or (not p and q) or (p and q and p.val != q.val):
            return False
        if not p and not q:
            return True

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
