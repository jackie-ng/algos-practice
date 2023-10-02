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


#         ##### BFS #####    
#        if not root:
#            return 0
#         level = 0
#         q = collections.deque([root])
        
#         while q:
#             #traverse through the level
#             for i in range(len(q)):
#                 #pop q node
#                 node = q.popleft()
#                 #check the children of this node, add the children to the queue if it's not null
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
                
                
#             # after being done with the level traversal, add 1 to the level
#             level += 1
#         return level

        ##### DFS #####
            if not root:
                return 0
            stack = [[root, 1]]
            res = 1
            
            while stack:
                node, depth = stack.pop()
                
                if node:
                    res = max(res, depth) 
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])
            return res
                    