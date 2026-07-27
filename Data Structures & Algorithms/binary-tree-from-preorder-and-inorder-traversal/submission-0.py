# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodeMap = defaultdict(int)
        for i,n in enumerate(inorder):
            nodeMap[n] = i
        preidx = 0

        def build(l, r):
            nonlocal preidx
            if l > r:
                return None
            
            root = TreeNode(preorder[preidx])
            preidx+= 1
            mid = nodeMap[root.val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        
        return build(0, len(inorder)-  1)
