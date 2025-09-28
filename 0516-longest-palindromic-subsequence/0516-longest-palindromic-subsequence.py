"""
If s[i] == s[j], then one valid palindrome is to take both ends plus the best inside: L(i,j) = 2 + L(i+1, j-1).

Why correct: Any optimal palindromic subsequence either uses both these matching ends or it doesn't. If they match, taking both cannot make the best smaller because we can always place s[i] at the front and s[j] at the end of some palindrome inside s[i+1..j-1]. Hence at least 2 + L(i+1,j-1) is achievable. Optimality: any optimal palindrome that uses both ends has that form; if best does not use both ends, the next case covers it.

If s[i] != s[j], then at least one of s[i] or s[j] is not used in any palindrome that uses the other as its mirror; so the optimal must lie in either s[i+1..j] or s[i..j-1]. Therefore:

L(i,j) = max( L(i+1, j), L(i, j-1) ).


Formal induction: For substrings shorter than current length, assume L is correct. The recurrence enumerates the two mutually exclusive cases (matching ends or not) and picks the best — therefore by induction it is correct.
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # n = len(s)
        # @lru_cache(None)
        # def L(i: int, j: int) -> int:
        #     if i > j:
        #         return 0
        #     if i == j:
        #         return 1
        #     if s[i] == s[j]:
        #         return 2 + L(i+1, j-1)
        #     else:
        #         return max(L(i+1, j), L(i, j-1))
        # return L(0, n-1)
        # ----------------------
        n = len(s)
        t = s[::-1]
        # we will use two rows of length n+1
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev, curr = curr, prev  # reuse arrays (swap roles)
        return prev[n]