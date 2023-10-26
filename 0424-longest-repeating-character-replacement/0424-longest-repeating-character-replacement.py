class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        maxF = 0

        for r in range(len(s)):
            # for the character at the position r, increment the count of it. If it's already in the hashmap, increase it by 1. If not, set it as 0
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            # make sure the window is valid using while OR if. We use while in this case
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
                # set the result to the max that it's ever been = the size of the window = r - l + 1 
            res = max(res, r - l + 1)
        return res