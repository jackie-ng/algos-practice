# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot = Null => subroot is subtree of root
        if not subRoot:
            return True
        # not vice versa. The order of the conditions matters
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        #what if it's not same tree???
        return (self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot))
        
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        # Check if both trees are the same
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and \
                    self.sameTree(root.right, subRoot.right))
        return False