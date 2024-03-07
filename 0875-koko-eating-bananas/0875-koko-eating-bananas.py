class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [3,6,7,11], h = 8
        # k in the range between [1, 11]
        # try k in the range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            m = (l+r)//2
            hours = 0
            for p in piles:            
                hours += math.ceil(p / m) # k = m, hours it takes for Koko to eat. Round up 
            # print(hours)
            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res