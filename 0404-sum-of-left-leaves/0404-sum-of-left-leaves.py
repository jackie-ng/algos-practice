# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(subtree, is_left):
            # Base case: If this subtree is empty, return 0
            if subtree is None:
                return 0
            
            # Base case: This is a leaf node.
            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0
            
            # Recursive case: return result of adding the left and right subtrees.
            return dfs(subtree.left, True) + dfs(subtree.right, False)

        return dfs(root, False)
            