class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Memoization dictionary to store results of subproblems
        memo = {}

        def recursiveEditDistance(i, j):
            # Check if the result is already memoized
            if (i, j) in memo:
                return memo[(i, j)]

            # Base case: if one of the words is empty, insert/delete characters to match the other word
            if i == len(word1):
                result = len(word2) - j
            elif j == len(word2):
                result = len(word1) - i
            else:
                # Recursive cases for insert, delete, and replace operations
                if word1[i] == word2[j]:
                    result = recursiveEditDistance(i + 1, j + 1)
                else:
                    insert_op = 1 + recursiveEditDistance(i, j + 1)
                    delete_op = 1 + recursiveEditDistance(i + 1, j)
                    replace_op = 1 + recursiveEditDistance(i + 1, j + 1)
                    result = min(insert_op, delete_op, replace_op)

            # Memoize the result before returning
            memo[(i, j)] = result
            return result

        # Start the recursive process with initial indices (0, 0)
        return recursiveEditDistance(0, 0)        

    
    ### Select the shortest word, say of size S
    ### Create an array lastRow of size S + 1
    ### a. Compute the next row currRow from left to right, using the results ##in lastRow
    ### b. Save the current row lastRow = currRow
    ### c. Repeat steps 3 for each char of the other word
    ### Return the bottom-right value of the table return lastRow[S]
    ### The space complexity of this version then becomes $$\mathcal O(S)$$, where S = min(N, M).

#         l1, l2 = len(word1), len(word2)

#         # If word1 is longer than word2, flip them
#         if l1 > l2:
#             return self.minDistance(word2, word1)

#         # First row is [0, 1, 2, 3, 4, ...]
#         last_row = [i for i in range(l1 + 1)]

#         # Compute all the rows of the table
#         for i in range(1, l2 + 1):
#             # First column should be [0, 1, 2, 3, 4, ...], hence [i]
#             row = [i]
#             for j in range(1, l1 + 1):
#                 val = min(1 + row[j - 1], # Delete char of word1\
#                           1 + last_row[j],# Delete char of word2\
#                          (0 if word1[j - 1] == word2[i - 1] else 1) + last_row[j - 1]) # Replace if necessary

#                 row.append(val)

#             last_row = row

#         return last_row[-1] # Return bottom-right value of the table