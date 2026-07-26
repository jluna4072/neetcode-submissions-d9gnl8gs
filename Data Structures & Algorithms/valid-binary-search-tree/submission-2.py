# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, base, top):
            if not node:
                return True
            
            if node.val >= top or node.val <= base:
                return False

            right = dfs(node.right, node.val, top)
            left = dfs(node.left, base, node.val)

            return right and left
        
        return dfs(root, float("-inf"), float("inf"))
            