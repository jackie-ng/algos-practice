# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        ##### BFS #####    
#         if not root:
#             return 0
#         q = collections.deque([root])
#         level = 0
#         while q:
#             for i in range(len(q)):
#                 cur = q.popleft()
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
#             level += 1
#         return level
    
        ##### DFS #####
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0
        while stack:
            cur, depth = stack.pop()
            if cur:
                res = max(res, depth)
                stack.append([cur.left, depth + 1])
                stack.append([cur.right, depth + 1])
        return res