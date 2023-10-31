# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level[-1])
        return res