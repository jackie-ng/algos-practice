# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
# #         # Valid Range: Recursion
#         def valid(node, left, right):
#             if not node:
#                 return True
#             if not (node.val < right and node.val > left):
#                 return False

#             return (valid(node.left, left, node.val) and
#                     valid(node.right, node.val, right))
#         return valid(root, float("-inf"), float("inf"))
            
            # Recursive: runtime-16ms

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output =[]
        self.inorder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1]>= output[i]:
                return False
        
        return True
    
    # Time complexity of inorder traversal is O(n)
    # Fun fact: Inorder traversal leads to a sorted array if it is 
    # a Valid Binary Search. Tree.
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)