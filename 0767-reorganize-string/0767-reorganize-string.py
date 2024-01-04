class Solution:
    def reorganizeString(self, S: str) -> str:
        res, c = [], Counter(S)
        pq = [(-value,key) for key,value in c.items()]
        heapq.heapify(pq)
        # previous frequency p_a and previous character p_b
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            # If the previous frequency p_a is less than 0, push the previous character p_b and its frequency back into the heap.
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1 # since it's a maxHeap
            # Update the previous frequency p_a and previous character p_b to a and b respectively.
            p_a, p_b = a, b
        res = ''.join(res)
        if len(res) != len(S): return ""
        return res

  