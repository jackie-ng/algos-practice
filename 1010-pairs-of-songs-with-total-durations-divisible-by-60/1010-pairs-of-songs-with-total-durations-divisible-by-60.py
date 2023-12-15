class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 60
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res
    
        # remainders = collections.defaultdict(int)
        # res = 0
        # for t in time:
        #     if t % 60 == 0: # check if a%60==0 && b%60==0
        #         res += remainders[0]
        #     else: # check if a%60+b%60==60
        #         res += remainders[60-t%60]
        #     remainders[t % 60] += 1 # remember to update the remainders
        # return res