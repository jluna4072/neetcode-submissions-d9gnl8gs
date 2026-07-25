# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Since this is a bst, we know tha that a node is a ancestor if borth nodes are on either side of it,
or if it itelf is one of teh nodes, since we cant go deeper
    
        
'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        if root and ((root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val)):
            return root
        elif root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p , q)
        elif root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        