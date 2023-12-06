class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Bellman Ford
        max_prob = [0] * n
        max_prob[start] = 1
        
        for i in range(n - 1):
            # If there is no larger probability found during an entire round of updates,
            # stop the update process.
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1 
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1
            if not has_update:
                break
        
        return max_prob[end]
    
#         # Dijkstra
#         graph = defaultdict(list)
#         for i, (u, v) in enumerate(edges):
#             graph[u].append((v, succProb[i]))
#             graph[v].append((u, succProb[i]))
        
#         max_prob = [0.0] * n
#         max_prob[start] = 1.0
        
#         pq = [(-1.0, start)]    
#         while pq:
#             cur_prob, cur_node = heapq.heappop(pq)
#             if cur_node == end:
#                 return -cur_prob
#             for nxt_node, path_prob in graph[cur_node]:

#                 if -cur_prob * path_prob > max_prob[nxt_node]:
#                     max_prob[nxt_node] = -cur_prob * path_prob
#                     heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
#         return 0.0