# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        while cur:
            # If both p and q are greater than parent
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both p and q are lesser than parent
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # We have found the split point, i.e. the LCA node.
            else:
                return cur
            
#         # Value of current node or parent node.
#         parent_val = root.val

#         # Value of p
#         p_val = p.val

#         # Value of q
#         q_val = q.val

#         # If both p and q are greater than parent
#         if p_val > parent_val and q_val > parent_val:    
#             return self.lowestCommonAncestor(root.right, p, q)
#         # If both p and q are lesser than parent
#         elif p_val < parent_val and q_val < parent_val:    
#             return self.lowestCommonAncestor(root.left, p, q)
#         # We have found the split point, i.e. the LCA node.
#         else:
#             return root