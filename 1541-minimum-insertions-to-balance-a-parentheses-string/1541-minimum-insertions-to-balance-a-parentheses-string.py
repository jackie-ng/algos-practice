class Solution:
    def minInsertions(self, s: str) -> int:
        # res represents the number of left/right parentheses already added.
        # right represents the number of right parentheses needed.
        res = right = 0
        for c in s:
            # 2) case (
            # If we meet a left parentheses,
            # we check if we have odd number ')' before.
            # If we right, we have odd ')' before,
            # but we want right parentheses in paires.
            # So add one ')' here, then update right--; res++;.
            # Note that this part is not necessary if two consecutive right parenthesis not required.

            # Because we have ), we update right += 2.
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            # 1) case )
            # If we meet a right parentheses , right--.
            # If right < 0, we need to add a left parentheses before it.
            # Then we update right += 2 and res++
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
    
# Record the number of '(' in an open bracket count int.
# If there is a '))' or a ') 'then open bracket count -= 1
# If there is a '))' or a ') and open bracket count = 0 an '(' must be inserted
# If there is a single ')' another ')' must be inserted
# At the end of the program and if open bracket count >0 then an '))' must be added for each unmatched '('



