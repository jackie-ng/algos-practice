class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Dijkstra
        # Build adj_list: u -> list of (v, prob)
        adj_list = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            adj_list[a].append((b, p))
            adj_list[b].append((a, p))

        # best[node] = best probability to reach node so far
        best = [0.0] * n
        best[start] = 1.0

        # max-heap simulated via negative probabilities
        heap = [(-1.0, start)]   # (-prob, node)
        visited = set()

        while heap:
            neg_prob, node = heapq.heappop(heap)
            prob = -neg_prob
            visited.add(node)

            # early exit: first time we pop 'end' is optimal
            if node == end:
                return prob

            for nei, p in adj_list[node]:
                if nei in visited:
                    continue
                np = prob * p
                if np > best[nei]:
                    best[nei] = np
                    heapq.heappush(heap, (-np, nei))

        return 0.0
#         # Bellman Ford
#         max_prob = [0] * n
#         max_prob[start] = 1
        
#         for i in range(n - 1):
#             # If there is no larger probability found during an entire round of updates,
#             # stop the update process.
#             has_update = 0
#             for j in range(len(edges)):
#                 u, v = edges[j]
#                 path_prob = succProb[j]
#                 if max_prob[u] * path_prob > max_prob[v]:
#                     max_prob[v] = max_prob[u] * path_prob
#                     has_update = 1 
#                 if max_prob[v] * path_prob > max_prob[u]:
#                     max_prob[u] = max_prob[v] * path_prob
#                     has_update = 1
#             if not has_update:
#                 break
        
#         return max_prob[end]