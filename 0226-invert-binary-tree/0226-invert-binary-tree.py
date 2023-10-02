# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         ### Recursion ###
#         if not root:
#             return None
#         # swap the children
#         tmp = root.left
#         root.left = root.right
#         root.right = tmp
        
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root

#         if not root:
#             return None
#         queue = collections.deque([root])
        
#         while queue:
#             current = queue.popleft()
#             current.left, current.right = current.right, current.left
            
#             if current.left:
#                 queue.append(current.left)
                
#             if current.right:
#                 queue.append(current.right)
                
#         return root

            stack = [root]
            while stack:
                cur = stack.pop()
                if cur:
                    cur.left, cur.right = cur.right, cur.left
                    
                    stack.append(cur.right)
                    stack.append(cur.left)
                
            return root