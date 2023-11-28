class Solution:
    def numDecodings(self, s: str) -> int:
#         memo = { len(s) : 1 }
        
#         def dfs(i):
#             if i in memo:
#                 return memo[i]
#             ### if it's not the end of the string
#             # invalid
#             if s[i] == "0": 
#                 return 0
            
#             # valid
#             res = dfs(i + 1)
#             if(i + 1 < len(s) and # if the digit is inbound
#                (s[i] == "1" or  # if the num is from 10-19
#                 s[i] == "2" and s[i + 1] in "0123456")): # if the num is from 20-26 
                
#                 res += dfs(i + 2)
#             memo[i] = res
#             return res
        
#         return dfs(0)

    


            # Edge case: an empty string has 0 ways to decode
            if not s:
                return 0

            # Initialize two variables to keep track of counts
            current_count = 1
            previous_count = 1

            for i in range(len(s)):
                # If the current digit is '0', update current count to 0
                if s[i] == '0':
                    current_count = 0

                # If the previous two digits form a valid number (between '10' and '26'), update current count
                if i > 0 and (s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6')):
                    current_count, previous_count = current_count + previous_count, current_count
                else:
                    # Otherwise, update previous count to the current count
                    previous_count = current_count

            return current_count