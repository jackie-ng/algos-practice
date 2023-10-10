# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # def dfs(node, maxVal):
        #     if not node:
        #         return 0
        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(maxVal, node.val)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        #     return res
        # return dfs(root, root.val)
        #         num_good_nodes = 0
        
        # Use collections.deque for efficient popping
        num_good_nodes = 0
        queue = collections.deque([(root, float("-inf"))])
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
        
        return num_good_nodes