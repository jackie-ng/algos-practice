# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         def postOrder(node):
#             if node is None:
#                 return
#             postOrder(node.left)
#             postOrder(node.right)
#             res.append(node.val)
        
#         postOrder(root)
#         return res
    
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> root -> right
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res