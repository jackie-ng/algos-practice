# from collections import defaultdict, deque

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # # Create the adjacency list for the graph
        # adj = defaultdict(list)
        # for u, v, price in flights:
        #     adj[u].append((v, price))
        

        # # Distance array to store the minimum cost to reach each node
        # dist = [float('inf')] * n
        # dist[src] = 0

        # # Queue for BFS
        # q = deque([(src, 0)])  # (current node, current cost)
        # stops = 0

        # while stops <= k and q:
        #     sz = len(q)
        #     for _ in range(sz):
        #         node, cost = q.popleft()

        #         # Explore neighbors
        #         for neighbour, price in adj[node]:
        #             if cost + price < dist[neighbour]:
        #                 dist[neighbour] = cost + price
        #                 q.append((neighbour, dist[neighbour]))
        #     stops += 1

        # return dist[dst] if dist[dst] != float('inf') else -1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         # Bellman Ford
#         # Initialize an array to store the minimum cost to reach each airport.
#         costs = [float("inf")] * n

#         # The cost to reach the source airport is set to 0.
#         costs[src] = 0

#         # Perform Bellman-Ford algorithm for at most k+1 iterations.
#         for i in range(k + 1):
#             # Create a temporary array to store updated costs without modifying the original array.
#             temp = costs.copy()

#             # Iterate through each flight represented as (start, end, price).
#             for start, end, price in flights:
#                 # Check if the cost to reach the starting airport is not infinity.
#                 if costs[start] != float("inf"):
#                     # Update the temporary array with the minimum cost to reach the destination.
#                     # relax the nodes
#                     temp[end] = min(costs[start] + price, temp[end])

#             # Update the original costs array with the values from the temporary array.
#             costs = temp

#         # Return the cost to reach the destination, or -1 if it is still infinity (indicating no valid path).
#         return costs[dst] if costs[dst] != float("inf") else -1
    
        # Dijsktra
        # Dictionary to track visited nodes and their corresponding stops
        visited = {}
        
        # Adjacency list to represent the graph, where each node has a list of (neighbor, price) tuples
        adj = defaultdict(list)
        
        # Populate the adjacency list based on the given flights
        for s, d, p in flights:
            adj[s].append((d, p))
        
        # Priority queue to store tuples (cost, stops, node) for exploration
        pq = [(0, 0, src)]
        
        # Perform Dijkstra's algorithm using a priority queue
        while pq:
            cost, stops, node = heapq.heappop(pq)
            
            # Check if the current node is the destination and the number of stops is within the limit
            if node == dst and stops - 1 <= k:
                return cost
            
            # If the node has not been visited or has been visited with fewer stops
            if node not in visited or visited[node] > stops:
                # Update visited information for the current node
                visited[node] = stops
                
                # Explore neighbors and update the priority queue with new cost and stops
                for neighbor, price in adj[node]:
                    heapq.heappush(pq, (cost + price, stops + 1, neighbor))
        
        # If the destination is not reached within the specified stops, return -1
        return -1