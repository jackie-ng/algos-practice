# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root: 
                return [True, 0]
            # Check subtrees to see if they are balanced. 
            left, right = dfs(root.left), dfs(root.right)
            # balanced if the left subtree, the right subtree and the root are balanced
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            # If the subtrees are balanced, check if the current tree is balanced
            # using their height
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
    
    # height(node) = -1 or 1 + max(height(node.left), height(node.right))