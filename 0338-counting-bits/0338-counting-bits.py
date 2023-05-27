class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        ans[0] = 0
        twoOffset = 1
        for i in range(1, n+1):
            if (twoOffset*2 == i):
                twoOffset = i
            ans[i] = 1 + ans[i- twoOffset]
        return ans
        
        