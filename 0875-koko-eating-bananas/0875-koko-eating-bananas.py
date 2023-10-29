class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # try 1 pile/hr to the max(piles)/hr
        res = r # we're trying to find the minimum => initialize the result to the r -- max(piles). Then work all the way down

        while l <= r:
            m = (l + r) // 2 
            hours = 0 # for this value m, how many hours does it take to eat all of these banana?
            for p in piles: # go through every pile in the input array piles
                hours += math.ceil(p / m) # p / k = hours it took, round up using math.ceil(  )
            if hours <= h:
                res = min(res, m)
                r = m - 1 # set pointer to the smaller amount m - 1 => search for the smaller portion
            else:
                l = m + 1 # set left pointer to the larger amount => search for the larger portion
        return res 