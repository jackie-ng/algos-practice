class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # # initialize the minimum abs different variable and the lookup dic
        # minDiff = math.inf
        # dic = collections.defaultdict(list)
        # # sort the arr
        # arr.sort()
        # # loop through the sorted array
        # for i in range(len(arr) - 1):
        #     # calculate the current diff and append the value to the dic
        #     diff = arr[i+1] - arr[i]
        #     dic[diff].append([arr[i], arr[i+1]])
        #     minDiff = min(minDiff, diff)
        # return dic[minDiff]
    
        min_element = min(arr)
        max_element = max(arr)
        
        shift = -min_element
        line = [0] * (max_element - min_element + 1)
        answer = []
        
        for num in arr:
            line[num + shift] = 1
        
        minDiff = max_element - min_element
        prev = 0
        for curr in range(1, max_element + shift + 1):
            if line[curr] == 0:
                continue
            if curr - prev == minDiff:
                answer.append([prev - shift, curr - shift])
            # else if we find new minDiff => clear answer/add new pair to answer, update minDiff
            elif curr - prev < minDiff:
                answer = [[prev - shift, curr - shift]]
                minDiff = curr - prev
            # update prev as curr
            prev = curr
        
        return answer