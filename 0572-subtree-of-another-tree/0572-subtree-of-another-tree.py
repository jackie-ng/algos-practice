# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Subproblem: LC 100: Same Tree
"""
class Solution:
    # # Recursion
    # def sameTree(self, a, b):
    #     if not a and not b:
    #         return True
    #     if not a or not b or a.val != b.val:
    #         return False
    #     return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     # Recursion
    #     if not root:
    #         return False # constraint: subRoot has at least 1 node
    #     if root.val == subRoot.val and self.sameTree(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def sameTree(self, a, b):
        stack = [(a, b)]
        while stack:
            x, y = stack.pop()
            if not x and not y:
                continue
            if not x or not y or x.val != y.val:
                return False
            stack.append((x.left, y.left))
            stack.append((x.right, y.right))
        return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        target = subRoot.val
        while stack:
            node = stack.pop()
            if node.val == target and self.sameTree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False