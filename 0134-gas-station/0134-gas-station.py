class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0 
        start = 0
        for i in range(len(gas)): # len(gas) = len(cost)
            diff = (gas[i] - cost[i])
            total += diff
            
            if total < 0:
                total = 0 # reset total to 0
                start = i + 1
        return start