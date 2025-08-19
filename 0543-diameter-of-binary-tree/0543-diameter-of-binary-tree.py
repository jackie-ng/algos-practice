# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
The height of a node is the number of edges on the longest path from the node to a leaf.
The diameter of the tree is the maximum value of left_height + right_height for any node.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:      
        # Recursion 
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, (left + right))
            return 1 + max(left, right)
        dfs(root)
        return self.diameter

        # Iterative
        if not root:
            return 0
        diameter = 0
        stack = [root, False]
        depths = {}
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                left = depths.get(node.left, 0)
                right = depths.get(node.right, 0)
                depths[node] = 1 + max(left, right)
                diameter = max(diameter, left + right)
            else:
                # Post-order: push node back after children
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return diameter
