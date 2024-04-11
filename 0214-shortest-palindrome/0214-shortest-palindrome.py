class Solution:
    # https://leetcode.com/problems/shortest-palindrome/discuss/4766688/Python3-Brute-Force-greater-KMP-greater-Rabin-Karp-(Rolling-Hash)-Simple-Solutions
    def shortestPalindromeBF(self, s: str) -> str:
        t = s[::-1]

        for i in range(len(t)):
            if s.startswith(t[i:]):
                return t[:i] + s

        return t + s
    
    # KMP:find the longest prefix of s match with the suffix of r => it is KMP
    def shortestPalindrome(self, s: str) -> str:
        # Reverse the input string
        r = s[::-1]

        # Combine the original string, a separator (#), and the reversed string
        ts = s + "#" + r
        print(ts)
        n = len(ts)

        # Longest Prefix Suffix (LPS) array using Manacher's Algorithm
        pi = [0 for _ in range(n)]  # pi[i] stores the length of the longest prefix suffix ending at index i

        # Calculate LPS for the combined string
        for i in range(1, n):
            j = pi[i - 1]  # Start with the LPS length of the previous character
            while j > 0 and ts[i] != ts[j]:  # Keep going back as long as characters don't match
                j = pi[j - 1]  # Move to the previous LPS

            if ts[i] == ts[j]:  # If characters match, increase the LPS length
                j += 1
            pi[i] = j

        # The shortest palindrome is the reversed part of the string (r) excluding the characters covered by the LPS at the end (pi[-1])
        return r[: len(r) - pi[-1]] + s
    
#     ts	a	a	c	e	c	a	a	a	#	a	a	a	c	e	c	a	a	a
																		
#     pi	0	1	0	0	0	1	2	2	0	1	2	2	3	4	5	6	7	0
# 							j ->	i ->										
#     r[: len(r) - pi[-1]] = r[0:8-7] = r[0:1]																		