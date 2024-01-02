class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # initialize the minimum abs different variable and the lookup dic
        minDiff = math.inf
        dic = collections.defaultdict(list)
        # sort the arr
        arr.sort()
        # loop through the sorted array
        for i in range(len(arr) - 1):
            # calculate the current diff and append the value to the dic
            diff = arr[i+1] - arr[i]
            dic[diff].append([arr[i], arr[i+1]])
            minDiff = min(minDiff, diff)
        return dic[minDiff]
    
#         # Initialize the auxiliary array `line`.
#         # Keep a record of the minimum element and the maximum element.
#         min_element = min(arr)
#         max_element = max(arr)
#         shift = -min_element
#         line = [0] * (max_element - min_element + 1)
#         answer = []
        
#         # For each integer `num` in `arr`, we increment line[num + shift] by 1.
#         for num in arr:
#             line[num + shift] = 1
        
#         # Start from the index representing the minimum integer, initialize the 
#         # absolute difference `min_pair_diff` as a huge value such as
#         # `max_element - min_element` in order not to miss the absolute 
#         # difference of the first pair.
#         min_pair_diff = max_element - min_element
#         prev = 0
        
#         # Iterate over the array `line` and check if line[curr] 
#         # holds the occurrence of an input integer.
#         for curr in range(1, max_element + shift + 1):
#             # If line[curr] == 0, meaning there is no occurrence of the integer (curr - shift) 
#             # held by this index, we will move on to the next index.
#             if line[curr] == 0:
#                 continue
                
#             # If the difference (curr - prev) equals `min_pair_diff`, we add this pair 
#             # {prev - shift, curr - shift} to the answer list. 
#             if curr - prev == min_pair_diff:
#                 answer.append([prev - shift, curr - shift])
#             elif curr - prev < min_pair_diff:
#                 # If the difference (curr - prev) is smaller than `min_pair_diff`, 
#                 # we empty the answer list and add the pair {curr - shift, prev - shift} 
#                 # to the answer list and update the `min_pair_diff`
#                 answer = [[prev - shift, curr - shift]]
#                 min_pair_diff = curr - prev
            
#             # Update prev as curr.     
#             prev = curr
            
#         return answer