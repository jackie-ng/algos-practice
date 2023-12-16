class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
# Intuition
# Count res the Number Without Repeated Digit
# Then the number with repeated digits = N - res

# Similar as
# 788. Rotated Digits
# 902. Numbers At Most N Given Digit Set

# Explanation:
# Transform N + 1 to arrayList
# Count the number with digits < n
# Count the number with same prefix
# For example,
# if N = 8765, L = [8,7,6,6],
# the number without repeated digit can the the following format:
# XXX
# XX
# X
# 1XXX ~ 7XXX
# 80XX ~ 86XX
# 870X ~ 875X
# 8760 ~ 8765

# Time Complexity:
# the number of permutations A(m,n) is O(1)
# We count digit by digit, so it's O(logN)
# https://leetcode.com/problems/numbers-with-repeated-digits/discuss/258212/Share-my-O(logN)-C%2B%2B-DP-solution-with-proof-and-explanation
        L = list(map(int, str(N + 1)))
        n = len(L)
        res = sum(9 * perm(9, i) for i in range(n - 1))
        s = set()
        for i, x in enumerate(L):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, n - i - 1)
            if x in s: break
            s.add(x)
        return N - res
    
    