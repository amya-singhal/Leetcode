class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        ls3 = len(s3)
        if ls1 + ls2 != ls3:
            return False
        cache = {}
        def helper(i,j,k):
            if k == ls3:
                return True
            if (i,j) in cache:
                return cache[(i,j)]
            ans = False
            if i < ls1 and s1[i] == s3[k]:
                ans = ans or helper(i+1, j, k+1)
            if j < ls2 and s2[j] == s3[k]:
                ans = ans or helper(i, j+1, k+1)
            cache[(i,j)] = ans
            return ans
        return helper(0,0,0)