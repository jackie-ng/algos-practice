# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def inOrder(node):
#             if node is None:
#                 return
#             inOrder(node.left)
#             res.append(node.val)
#             inOrder(node.right)
                
#         inOrder(root)
#         return res
#         res = []
#         stack = [root]
        
#         while stack:
#             curr_node = stack.pop()
#             if curr_node:
#                 stack.append(curr_node.right)
#                 res.append(curr_node.val)
#                 stack.append(curr_node.left)
                
#         return res
    

        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res