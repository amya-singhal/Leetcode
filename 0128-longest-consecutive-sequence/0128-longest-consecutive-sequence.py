class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        unique = set(nums)
        while unique:
            l = h = unique.pop()
            while l-1 in unique or h+1 in unique:
                if l-1 in unique:
                    unique.remove(l-1)
                    l = l-1
                if h+1 in unique:
                    unique.remove(h+1)
                    h = h+1
            ans = max(ans, h-l+1)
        return ans
        
        