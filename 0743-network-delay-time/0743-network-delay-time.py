class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra: O(E * logV)
        
        # Construct adjacency list
        adj = defaultdict(list)
        for src, dst, c in times:
            adj[src].append((dst, c)) 
        
        queue = [(0, k)] #(cost, node)
        visited = set()
        max_time = 0
            
        while queue:
            #Always pop the min value
            time, node = heapq.heappop(queue)
            if node in visited: # if node is already in visited, skip it
                continue
                
            visited.add(node)
            
            max_time = max(max_time, time)
            
            for new_node, new_time in adj[node]:
                if new_node not in visited:
                    curr_time =  time + new_time
                    heapq.heappush(queue, (curr_time, new_node))

        return max_time if len(visited) == n else -1