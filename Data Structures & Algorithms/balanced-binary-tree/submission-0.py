# #class TreeNode:
#     def __init__(self, val = 0, right = None, left = None) --> None:
#         self.val = val
#         self.right = right
#         self.left = left

'''
input: a tree node
output: true/false->if the tree is balanced(left and right subtree differ in hieght by no more than
1)

'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
            balanced = True
            def dfs(node):
                nonlocal balanced
                if not node:
                    return 0
            
                left = 1 + dfs(node.left)
                right = 1 + dfs(node.right)
                print(right)
                print(left)
                balanced = balanced and abs(left - right) <= 1

                return max(left,right) 

            dfs(root)
            return balanced
        

            


        


