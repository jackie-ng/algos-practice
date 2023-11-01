# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]
        res = []
        while stack:
            # while root:
            #     stack.append(root)
            #     root = root.left
            # root = stack.pop()
            # k -= 1
            # if not k:
            #     return root.val
            # root = root.right
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return res[k - 1]
            
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             k -= 1
#             if not k:
#                 return root.val
#             root = root.right
            
#             arr = []
            
#             def inOrder(node):
#                 if node is None:
#                     return
#                 inOrder(node.left)
#                 arr.append(node.val)
#                 inOrder(node.right)
#             inOrder(root)
#             return arr[k - 1]

        