class Solution:
    def reorganizeString(self, S: str) -> str:
        res, c = [], Counter(S)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ""
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0: # still has element to pop, add back to the heap
                heapq.heappush(pq, (p_a, p_b))
            a += 1 # maxHeap => deduct 1 element
            p_a, p_b = a, b 
        res = ''.join(res)
        if len(res) != len(S): return ""
        return res
            
  # https://leetcode.com/problems/reorganize-string/discuss/3949276/ex-amazon-explains-a-solution-with-python-javascript-java-and-c/