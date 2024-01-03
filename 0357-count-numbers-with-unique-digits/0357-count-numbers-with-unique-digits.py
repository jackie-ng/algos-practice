# class Solution:
#     def countNumbersWithUniqueDigits(self, n: int) -> int:
#         choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#         ans, product = 1, 1
        
#         for i in range(min(n, 10)):
#             product *= choices[i]
#             ans += product
            
#         return ans
    

# Dynamic Programming

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp = [1, 10] # 10 choices for single digit number
        for i in range(2, n+1):
            # for a 2 digit number, there are 9 options for the first digit (any digit from 1 to 9) and 9 options for the second digit (any digit from 0 to 9 excluding the first digit), giving us 9*9=81 unique 2 digit numbers.T
            tmp = 81 
            # For each j in this range, it multiplies tmp by (9 - j). This is because for each additional digit, we have (9 - j) options (any digit from 0 to 9 excluding the already chosen digits).
            for j in range(1, i-1):
                tmp *= (9 - j)
            ans = dp[i-1] + tmp
            dp.append(ans)
        return dp[n]