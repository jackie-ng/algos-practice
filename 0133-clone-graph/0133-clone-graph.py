"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # # Recursive
        # if not node:
        #     return None
        # seen = {}
        # def dfs(cur):
        #     if cur in seen:
        #         return seen[cur]
        #     copy = Node(cur.val, []) # set the copy node
        #     seen[cur] = copy # add to the seen hashmap
        #     for nei in cur.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        # return dfs(node)
        # Iterative
        if not node:
            return None
        seen = {node: Node(node.val, [])}
        stack = [node]
        while stack:
            cur = stack.pop()
            cur_copy = seen[cur]
            for nei in cur.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val, [])
                    stack.append(nei)
                cur_copy.neighbors.append(seen[nei])
        return seen[node] 
#time complexity: O(N+M)
#space complexity: O(N)