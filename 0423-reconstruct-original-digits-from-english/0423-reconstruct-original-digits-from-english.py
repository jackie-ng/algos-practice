class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        d = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
        
        res = [''] * 10
        for i in chain(range(0,10,2), range(1,10,2)):
            cur = Counter(d[i])
            if not cur - c:
                k = min(c[x] for x in cur)
                res[i] = str(i) * k
                for x in cur: c[x] -= k                  

        return ''.join(res)