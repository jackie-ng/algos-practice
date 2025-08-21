# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
If both are None → equal at this position.
If exactly one is None → not equal.
If both exist but values differ → not equal.
Otherwise, both exist and values match 
→ recursively/iteratively compare left and right children.
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # Recursion
        # if not q and not p:
        #     return True
        # if not q or not p:
        #     return False
        # if q and p and q.val != p.val:
        #     return False
        # if q and p and q.val == p.val:
        #     return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        # Iterative
        stack = [(p, q)]
        while stack:
            subtreeQ, subtreeP = stack.pop()
            if not subtreeQ and not subtreeP:
                continue
            if not subtreeQ or not subtreeP:
                return False
            if subtreeQ.val != subtreeP.val:
                return False
            if subtreeQ.val == subtreeP.val:
                stack.append((subtreeQ.left, subtreeP.left))
                stack.append((subtreeQ.right, subtreeP.right))
        return True