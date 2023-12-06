class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)
            
        def dfs(origin):
            destList = flightMap[origin]
            while destList:
                #while we visit the edge, we trim it off from graph.
                nextDest = destList.pop()
                dfs(nextDest)
            result.append(origin)
            

        result = []
        dfs('JFK')
        # reconstruct the route backwards
        return result[::-1]
