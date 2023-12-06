class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim
        size = len(points)
        visited = set()
        min_heap = [(0, 0)] # Priority queue to store (cost, vertex) pairs
        
        result = 0
        
        while min_heap:
            cost, vertex = heapq.heappop(min_heap)
            
            if vertex not in visited:
                visited.add(vertex)
                
                result += cost
                
                for i in range(size):
                    if i not in visited:
                        # calculate Manhattan distance
                        distance = abs(points[vertex][0] - points[i][0]) + abs(points[vertex][1] - points[i][1])
                        heapq.heappush(min_heap, (distance, i))
        return result