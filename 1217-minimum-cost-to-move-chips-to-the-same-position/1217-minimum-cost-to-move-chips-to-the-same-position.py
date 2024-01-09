class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # greedy: move all chips at even positions to position 0, 
        # and move all chips at the odd positions to position 1
        even_count = 0
        odd_count = 0
        for i in position:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return min(even_count, odd_count)